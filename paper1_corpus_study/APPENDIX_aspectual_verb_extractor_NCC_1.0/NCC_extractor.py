from utils import *

def main():
    discarded = 0
    accepted = 0
    total = 0
    
    today = date.today()
    nlp = stanza.Pipeline(lang='no', processors='tokenize') #calling stanza pipeline
    
    start = time.time() #start initial time
    
    list_asp_verbs = utils.list_asp_verbs("list_aspectual_verbs_nor.csv") # extraction of list of verbs. Function from utils.py
    pattern = utils.stemming(list_asp_verbs)# stemming verbs. Function from utils.py
    
    #Initialization of NCC corpus https://huggingface.co/datasets/NbAiLab/NCC
    data = load_dataset("NbAiLab/NCC", split="train", streaming=True) #here only training set, check also dev and test set
    
    for article in data: #here every article may contain multiple sents.
        # print(f"RAM used: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} MB", end ="\r")
        mid_term = time.time() #freeze time 
        total += 1
        idx = article["id"]
        idx = re.sub("/","_", article["id"]) #getting the id as string
        try:
            art_ = article["text"]
            doc = nlp(art_)
            for line_, sent in enumerate(doc.sentences): #looping through every single sentence in each article
                if re.findall(pattern, sent.text): #matching apsectual verbs.
                    sent_classification = langid.classify(sent.text.strip()) #classification bm vs nn
                    classified_lang = re.sub("no", "nb", sent_classification[0]) #consider no as nb 
                    if re.match(r"nb|no|nn",sent_classification[0]):# attention: multiple languages identified. Some cases langid cannot distinguish btw nb and nn - identified with no
                        pd.DataFrame([sent.text], columns=["Sentence"]).to_csv("sentence_list_NCC/"+str(classified_lang)+"_id_"+ str(idx) + "_line_"+str(line_) +".csv", index = False) #every sentence is saved singularly to avoid file size problems.
                        accepted += 1
                    else:
                        discarded += 1
                else:
                    discarded += 1
    
    
    
            print("Total: ", total, "Accpeted: ", accepted, "Discarded: ", discarded, "Time:", round(mid_term- start, 2), end = "\r")
    
        except:
            with open("article_not_parsed.txt", "a") as fout: #it creates a file including the index of the corrputed sentence.
                print(idx, file = fout)
            
    end = time.time()
    
    elapsed_time = end - start
    print("Elapsed time: {}".format(elapsed_time))


if __name__ == "__main__":
    main()

