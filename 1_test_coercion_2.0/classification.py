from import_data import import_data
list_lemma_inflected, entity_verb_association_NCC = import_data() 
from fill_mask_mlm import fill_mask_mlm
import pandas as pd
import re


def get_experimental_items(): #get sheet
    df = pd.read_csv("data_for_task/experiment_coercion - log_meto_with_context.csv")
    df.columns = df.iloc[3]
    df = df.iloc[4:]
    df = df[~(df["cat_letter"].str.contains('a'))]
    return df
    
def assembly_sentence(items):
    condition_letter = items['cat_letter']
    entity_lemma = re.sub("-\w+", "", items['item'])
    event_top_predict = items['pred_event']
    subj = items['SUBJ']
    sent = items['PRE_CONTEXT'] + " " + items['SUBJ'].capitalize() + " " + '[VERB]' + " " + '[PREP]' + " " + items['ARG'] + " " + items['POST_CRIT'] + items['EOS']
    return sent, subj, event_top_predict, entity_lemma, condition_letter



def start_classification(model, model_type, tokenizer, with_context,  model_ltg): #preparing sentences to be tested
    list_model_used = []
    list_entities_ = []
    list_predictions = []
    list_logits = []
    list_masked_tokens_found = []
    output_text = [] #list of sentences in output
    list_subjects, list_verbs, list_prepositions = [], [], []
    soft_max = []
    list_same_index_logits_softmax = []
    condition_letter_list = [] #only for classification with context
    
    ### For creating conytext-neutral sentences
    subjects = [("Kim", 0)]
    verbs = ["begynte", "startet", "fortsatte", "avsluttet"]
    prepositions = ["på", "med", ""]

    
################################## NO CONTEXT ##################################
    if with_context == False:
        print("Classification WITHOUT context")

        for entity_lemma, entity_inflected in zip(entity_verb_association_NCC, list_lemma_inflected["0"].tolist()): 
            for subj in subjects:
                subj = subj[0]
                for verb in verbs:
                    for prep in prepositions:
                        
                        if model_type == 0: ####AUTOENCODER####

                            if model_ltg == 1:   
                                sentence = f"{subj} {verb} {prep} {entity_inflected}. Det som {subj} {verb} å gjøre, var å[MASK].".replace("  ", " ")
                            else:
                                sentence = f"{subj} {verb} {prep} {entity_inflected}. Det som {subj} {verb} å gjøre, var å [MASK].".replace("  ", " ")

                            print(sentence) ###   


                            output_text_list, list_prob_events, list_probabilities, list_probabilities_logits, same_index_logits_softmax = \
                            fill_mask_mlm(tokenizer, model, sentence,entity_lemma)
                            
                        elif model_type == 1: ####AUTOREGRESSIVE####
                            
                            sentence = f"{subj} {verb} {prep} {entity_inflected}. Det som {subj} begynte å gjøre, var å".replace("  ", " ")
                            print(sentence)
                            list_prob_events, list_probabilities, list_probabilities_logits, output_text_list, same_index_logits_softmax = \
                                model.fill_mask_gpt(sentence, entity_lemma)


                        list_model_used.append(model.model_name)
                        output_text.append(output_text_list)
                        list_entities_.append(entity_lemma)
                        list_predictions.append(list_prob_events)
                        list_subjects.append(subj)
                        list_verbs.append(verb)
                        list_prepositions.append(prep)
                        soft_max.append(list_probabilities)
                        list_logits.append(list_probabilities_logits)
                        list_same_index_logits_softmax.append(same_index_logits_softmax)
                        


        return list_model_used, output_text, list_entities_, list_predictions, list_subjects, list_verbs, list_prepositions, soft_max, list_logits, list_same_index_logits_softmax, condition_letter_list

################################## WITH CONTEXT ##################################

        
    elif with_context == True:
        df_dataset_coercion = get_experimental_items() #call the dataset with experimental items
        print("Classification WITH context")

        for idx, items in df_dataset_coercion.iterrows():
            sent, subj, event_top_predict, entity_lemma, condition_letter  = assembly_sentence(items)

            for verb in verbs:
                for prep in prepositions:
                    sent2 = sent.replace('[VERB]', verb).replace('[PREP]', prep).replace('[SUBJ]', subj.capitalize())
                    sent3 = re.sub("(\s)?%", "", sent2)
                    sent3 = re.sub("^\s", "", sent3)
                    
                    if model_type == 0: ####AUTOENCODER####
                        
                        if model_ltg == 1: 
                            sentence = sent3 + f" Det som {subj} {verb} å gjøre, var å[MASK].".replace("  ", " ")
                        else:
                            sentence = sent3 + f" Det som {subj} {verb} å gjøre, var å [MASK].".replace("  ", " ")

                        sentence = re.sub("\s\s", " ", sentence)
                        print("SENT: ", sentence) ###

                        
                        output_text_list, list_prob_events, list_probabilities, list_probabilities_logits, same_index_logits_softmax = fill_mask_mlm(tokenizer, model, sentence,entity_lemma)
                                                    
                    elif model_type == 1: ####AUTOREGRESSIVE####
                        
                        sentence = sent3 + f" Det som {subj} {verb} å gjøre, var å"
                        print("SENT: ", sentence) ###

                        list_prob_events, list_probabilities, list_probabilities_logits, output_text_list, same_index_logits_softmax = model.fill_mask_gpt(sentence, entity_lemma)
                        
                    
                    list_model_used.append(model.model_name)
                    output_text.append(output_text_list)
                    list_entities_.append(entity_lemma)
                    list_predictions.append(list_prob_events)
                    list_subjects.append(subj)
                    list_verbs.append(verb)
                    list_prepositions.append(prep)
                    soft_max.append(list_probabilities)
                    list_logits.append(list_probabilities_logits)
                    list_same_index_logits_softmax.append(same_index_logits_softmax)
                    condition_letter_list.append(condition_letter)



        return list_model_used, output_text, list_entities_, list_predictions, list_subjects, list_verbs, list_prepositions, soft_max, list_logits, list_same_index_logits_softmax, condition_letter_list
