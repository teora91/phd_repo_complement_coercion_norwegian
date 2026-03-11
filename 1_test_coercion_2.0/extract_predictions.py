import pandas as pd
from ast import literal_eval
import json
import gspread
from datetime import date
# from read_gsheet import read_gsheet
today = date.today().strftime('%d-%m-%y')
import os

def extraction_new_events(path_new_results): 
    df = pd.read_csv(path_new_results)
    df["predicted_events"] = df["predicted_events"].apply(literal_eval)

    list_predictions = list()
    list_entities = list()

    for idx, item in df.iterrows():
        preds = item["predicted_events"]
        entity = item["entities"]

        for p in preds:
            list_predictions.append(p)
            list_entities.append(entity)


    df_ = pd.DataFrame([
        list_entities,
        list_predictions,
    ]).T
    
    
    df_ = df_.drop_duplicates() #list created with unique values of classification
    return df_
    
    
def filter_events(path_new_results, folder_path, with_context): #get only events not already present in the gsheet table 
    df_semantic = pd.read_csv("data_for_task/list_semantic_classification_definitive - official.csv")
    new_df_events = extraction_new_events(path_new_results)
    
    list_never_seen_predictions = []
    list_entities_associated_with_never_seen_predictions = []

    for idx, item in new_df_events.iterrows():
        preds = item[1]
        entity = item[0]
        for p in preds.split():
            x = df_semantic[df_semantic["entity"]==entity]
            pr = x[x["retrieved"]==p]
            if pr.empty:
                # print(p, entity)
                list_never_seen_predictions.append(p)
                list_entities_associated_with_never_seen_predictions.append(entity)
                

    path_for_saving = folder_path  + f"temporary_list_semantic_classification_to_merge_updated_{today}_with_context_{with_context}.csv"

    new_df = pd.DataFrame([list_entities_associated_with_never_seen_predictions, list_never_seen_predictions]).T.drop_duplicates().sort_values(by=[0, 1])
    
    if with_context == True:
        new_df["context?"] =  "WITH CONTEXT" 
    elif with_context == False:
        new_df["context?"] =  "NO CONTEXT" 

    new_df.to_csv(path_for_saving)
    print("Done")
    
    return new_df
    
    
    
    
def main(folder_path, with_context):
    path_new_results = 'results_coercion_{}/merged_results_coercion_updated_{}_with_context_{}.csv'.format(today, today, with_context)
    
    new_df = filter_events(path_new_results, folder_path, with_context)
    return new_df
    
if __name__ == '__main__':
    folder_path = f'results_coercion_{today}/'
    
    print('Extracting and filter unique events to be classified...')
    df_no_context = main(folder_path, with_context=False)
    df_with_context = main(folder_path, with_context=True)
    
    merged_df = pd.concat([df_no_context, df_with_context])
    merged_df.drop_duplicates(subset= [0,1])
    
    merged_df.to_csv(folder_path + "definitive_list_semantic_classification_to_merge_updated_{today}_with_context_both_context.csv", index=False)
    
    
    print("COMPLETED! \n")
    
    

    
    
    
