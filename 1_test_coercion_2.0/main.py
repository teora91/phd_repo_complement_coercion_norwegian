from utils import *
import MLM_model, CAUSAL_LM_model
from classification import start_classification


def model_name_converter(model_name):
    model_hub = re.sub("^", "models--", model_name)
    model_hub = re.sub("/", "--", model_hub)
    model_hub = re.sub("^", "C:/Users/mattera/.cache/huggingface/hub/", model_hub)

    return model_hub


def flatten_list(list_):
    new_list = []
    for i in list_:
        for x in i:
            new_list.append(x)
    return new_list
    
    
def main():
    output_text_df = []
    union_list_model_used = []
    list_entities_df = []
    list_prediction_df = []
    df_list_prepositions, df_list_subjects, df_list_verbs = [], [], []
    df_soft_max = []
    df_logits = []
    df_list_mask_tokens_found = []
    df_same_index_logits_softmax = []
    df_condition_letter_list = []
    
    #This part ensures the selection of the desired model and dataset (with or without context) from bash command line (ArgumentParser). See file test_coercion_launcher.sh
    def str2bool(value):   #Convert string to boolean.
        if isinstance(value, bool):
            return value
        if value.lower() in ('true', 't', 'yes', '1'):
            return True
        elif value.lower() in ('false', 'f', 'no', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError("Boolean value expected.")

    parser = argparse.ArgumentParser(description=None)

    #adding arguments 
    parser.add_argument(
        "-idx", "--index_group",
        type=int,
        required=True
    )

    parser.add_argument(
        "-c", "--context",
        type=str2bool,  # Use the custom str2bool function
        required=True,
        help="Specify True or False for the context"
    )

    args = parser.parse_args()    
    
    if args.index_group:
        selected_model_index = args.index_group
        print(f"Group of model chosen -> {args.index_group}")
        
        #Load list of LLMs
        with open('data_for_task/llm_list_nor.json', 'r') as file:
            model_list = json.load(file)[str(selected_model_index)]

        
        with_context = args.context
        print(f"Group of model chosen -> {with_context}")

        
    folder_path = f"results_coercion_{today}"
        
    path_data = folder_path + f"/results_test_coercion_no_context_OFFICIAL_updated_{today}_part_{args.index_group}_with_context_{with_context}.csv"
    
    #create a folder if not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"New folder for results created: {folder_path}")
        
    #loop single model
    for model in model_list:
        print("Running Model: ", model[0])
        print("")
    
        if model[1] == 0: #FILL MASK FOR BERT MODELS
            print(model[1])
            model_hub = model_name_converter(model[0]) 
            model_mlm = MLM_model.MLMHeadModel(model[0]) #Get model

            #if ltg models they need to modify the string where the mask token is found
            model_ltg = model[2]
            


            list_model_used, output_text, list_entities_, list_predictions, list_subjects, list_verbs, list_prepositions, soft_max, list_logits, list_same_index_logits_softmax, condition_letter_list = \
            start_classification(model_mlm, model[1], model_mlm.tokenizer, with_context, model_ltg)

        if model[1] == 1:             # GPT MODELS
            print(model[1])
            model_hub = model_name_converter(model[0])
            model_gpt = CAUSAL_LM_model.LMHeadModel(model[0]) #Get model
            model_ltg = 0

            list_model_used, output_text, list_entities_, list_predictions, list_subjects, list_verbs, list_prepositions, soft_max, list_logits, list_same_index_logits_softmax, condition_letter_list = \
            start_classification(model_gpt, model[1], model_gpt.tokenizer, with_context, model_ltg)
            
        union_list_model_used.append(list_model_used)
        output_text_df.append(output_text)
        list_entities_df.append(list_entities_)
        list_prediction_df.append(list_predictions)
        df_list_prepositions.append(list_prepositions)
        df_list_subjects.append(list_subjects)
        df_list_verbs.append(list_verbs)
        df_soft_max.append(soft_max)
        df_logits.append(list_logits)
        df_same_index_logits_softmax.append(list_same_index_logits_softmax)
        df_condition_letter_list.append(condition_letter_list)

            
            
            
    output_text_df = flatten_list(output_text_df)
    list_entities_df_ = flatten_list(list_entities_df)
    list_prediction_df_ = flatten_list(list_prediction_df)
    df_list_prepositions = flatten_list(df_list_prepositions)
    df_list_subjects = flatten_list(df_list_subjects)
    df_list_verbs = flatten_list(df_list_verbs)
    df_soft_max = flatten_list(df_soft_max)
    df_logits = flatten_list(df_logits)
    df_same_index_logits_softmax = flatten_list(df_same_index_logits_softmax)
    df_condition_letter_list = flatten_list(df_condition_letter_list)
    model_list_df = []
    
    
    for x in union_list_model_used:
        c = []
        c.append(x[0]) 
        for i in c * int(len(list_entities_df_)/len(model_list)):
            model_list_df.append(i)

    print("Creation Dataframe ...")
    print("Length Dataframe", len(model_list_df))
    columns_df_final = ["model_name", "condition letter", "entities", "subject", "verb" ,"preposition", "predicted_events","soft_max", "logits", "output_text_predicted", "same_index_logits_sftmax"]
    results_df = pd.DataFrame([model_list_df, df_condition_letter_list, list_entities_df_, df_list_subjects, df_list_verbs, df_list_prepositions, list_prediction_df_, df_soft_max, df_logits, output_text_df, df_same_index_logits_softmax ], index=columns_df_final).T

    print("Saving DataFrame ...")
    
    results_df.to_csv(path_data, index=False)
    


if __name__ == '__main__':
    main()
    print("Done")
