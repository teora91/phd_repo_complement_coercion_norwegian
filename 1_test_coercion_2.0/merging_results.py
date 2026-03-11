from utils import *

today = date.today().strftime('%d-%m-%y')

folder_path = f"results_coercion_{today}/"

def merging_results(path, with_context):

    df_ = pd.DataFrame()
    
    if with_context == True:
        for filename in os.listdir(path):
            if filename.endswith('_with_context_True.csv'):
                _path = os.path.join(path + filename)
                df_temp = pd.read_csv(_path)
                df_ = pd.concat([df_, df_temp], ignore_index=True)  # Concatenating properly
        print("Saving merged dataframe")
        
        df_.to_csv(folder_path + f'merged_results_coercion_updated_{today}_with_context_{with_context}.csv', index=False)




    elif with_context == False:
        for filename in os.listdir(path):
            if filename.endswith('_with_context_False.csv'):
                _path = os.path.join(path + filename)
                df_temp = pd.read_csv(_path)
                df_ = pd.concat([df_, df_temp], ignore_index=True)  # Concatenating properly
        print("Saving merged dataframe")

        df_.to_csv(folder_path + f'merged_results_coercion_updated_{today}_with_context_{with_context}.csv', index=False)
        
    print("Merging Done")


if __name__ == "__main__":
    merging_results(folder_path, with_context=False)
    merging_results(folder_path, with_context=True)