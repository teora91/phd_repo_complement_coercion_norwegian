from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LMHeadModel:

    def __init__(self, model_name):
        # Initialize the model and the tokenizer.
        self.model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=True).to("cuda")
        self.model.eval()  # Set the model to evaluation mode
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model_name = model_name
    
    def get_predictions(self, sentence):
        # Encode the sentence using the tokenizer and return the model predictions.
        inputs = self.tokenizer.encode(sentence, return_tensors="pt").to("cuda")
        with torch.no_grad():
            outputs = self.model(inputs)
            predictions_logits = outputs.logits
        return predictions_logits
    
    def get_next_word_probabilities(self, sentence, top_k=10):
        list_same_index_logits_softmax = []

        

        # Get the model predictions for the sentence.
        predictions_logits = self.get_predictions(sentence)
        
        # Get the next token candidates.
        next_token_candidates_tensor = predictions_logits[0, -1, :]
        
        # Get the top k next token (INDEXES) candidates.
        topk_candidates_indexes_logits = torch.topk(
            next_token_candidates_tensor, top_k).indices.tolist()
        
        # Get the token probabilities (LOGITS) for top-k candidates.
        topk_candidates_logits = \
            next_token_candidates_tensor[topk_candidates_indexes_logits].tolist()
        
        
        # Get the token probabilities (SOFTMAX) for all candidates.
        all_candidates_probabilities = torch.nn.functional.softmax(
            next_token_candidates_tensor, dim=-1)
        
        topk_candidates_indexes_softmax = torch.topk(
            all_candidates_probabilities, top_k).indices.tolist()
        
        
        
        # Filter the token probabilities (SOFTMAX) for the top k candidates.
        topk_candidates_probabilities = \
            all_candidates_probabilities[topk_candidates_indexes_softmax].tolist()
        
        
        for log, softmx in zip(topk_candidates_indexes_logits, topk_candidates_indexes_softmax):
            list_same_index_logits_softmax.append(log == softmx)


        # Decode the top k candidates back to words.
        topk_candidates_tokens = \
            [self.tokenizer.decode([idx]).strip() for idx in topk_candidates_indexes_softmax]
        
        # Return the top k candidates and their probabilities.
        
        return list(zip(topk_candidates_tokens, topk_candidates_probabilities, topk_candidates_logits, list_same_index_logits_softmax))
    
    
    def fill_mask_gpt(self, sentence, entity):
        sequence_prediction = []
        sequence_prediction_softmax = []
        sequence_prediction_logits = []
        output_text_list = []
        list_same_index_logits_softmax_list = []

        list_probabilities = self.get_next_word_probabilities(sentence, top_k=10)
        for prob in list_probabilities:
            output_text_list.append(sentence + " " + prob[0] + ".")
            sequence_prediction.append(prob[0].strip())
            sequence_prediction_softmax.append(prob[1])
            sequence_prediction_logits.append(prob[2])
            list_same_index_logits_softmax_list.append(prob[3])
            
        return sequence_prediction, sequence_prediction_softmax, sequence_prediction_logits, output_text_list, list_same_index_logits_softmax_list
