from utils import *

def fill_mask_mlm(tokenizer, model, sentence, entity, top_k=10):
    masked_token_found = []
    
    output_text_list = []
    list_prob_events = [] #list of plausible events
    list_probabilities = [] #list of softmax prob of the extracted event
    list_probabilities_logits = [] #list of logits of the extracted event
    
    same_index_logits_softmax = []

    mask_id = tokenizer.convert_tokens_to_ids("[MASK]")
    input_text = tokenizer(sentence, return_tensors="pt").to("cuda")
    
    if (input_text.input_ids  == mask_id).any().item():
        masked_token_found.append([1] * top_k) 
    else:
        masked_token_found.append([0] * top_k) 

    
    # Get the logits from the model
    with torch.no_grad():
        outputs = model.model(**input_text)
        
    # Find the index of the mask token
    mask_token_index = (input_text.input_ids == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]
    
    
    # Obtain logits for the masked position
    logits_for_mask = outputs.logits[0, mask_token_index, :]
        
    # Apply softmax to get probabilities
    probs_for_mask = F.softmax(logits_for_mask, dim=-1)
    
    # Sort the probabilities to get the indices of the most probable tokens
    sorted_probs, sorted_indices = torch.sort(probs_for_mask, descending=True)
    
    sorted_probs_logits, sorted_indices_logits = torch.sort(logits_for_mask, descending = True)
    
    #checking the sorted indices of logits and ssoftmax we can find some differences in indices maybe due to the conversion of softmax function due to the values too low
    # probably this will always happen from a certain index.

    
    for i in range(top_k):

        highest_logit_index = sorted_indices_logits[0, i]
        
        highest_index_softmax = sorted_indices[0, i]
        
        same_index_logits_softmax.append(highest_logit_index == highest_index_softmax)
        
        #here we use the softmax probabilities
        probability = sorted_probs[0, i]
        
        indexed_logits_values  = sorted_probs_logits[0, i]
        
        # Replace the mask token with the indexed token ID
        input_text.input_ids[0, mask_token_index] = highest_index_softmax
        # Decode the input_ids to get the final text
        output_text = tokenizer.decode(input_text.input_ids[0], skip_special_tokens=True)
        output_text_list.append(output_text)
        
        list_prob_events.append(tokenizer.decode(highest_index_softmax).strip())
        list_probabilities.append(probability.item())  # Convert to Python float for readability
        list_probabilities_logits.append(indexed_logits_values)
                
    return output_text_list, list_prob_events, list_probabilities, list_probabilities_logits, same_index_logits_softmax
