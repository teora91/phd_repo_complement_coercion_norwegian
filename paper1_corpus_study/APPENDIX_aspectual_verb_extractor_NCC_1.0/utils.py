import re
import os
import time
import numpy as np
import langid
import pandas as pd
import json
import time
import psutil
import stanza
import sys
import utils
from datasets import load_dataset



from datetime import date  #getting current date


def list_asp_verbs(file_path):
    df =  pd.read_csv(file_path, header = None)[0].tolist()
    return df
    
def stemming(list_verbs): #requires a list o verbs. Returns a regex pattern
    pattern = r""
    for verb in list_verbs:
        if len(verb.split()) == 1:
            if verb != "ende":
                chars = verb[:-1] # deletion of final vowel if ending with es

                if chars[-1] == chars[-2]: # if geminate 
                    if re.findall("n|l",chars[-1]): # begynne - begynte
                        chars = chars[:-1] 
            else:
                chars = verb
#             new_verb = "".join(chars)
            pattern += chars + " "
    pattern = re.sub(r"\s", "|", pattern)
    pattern = re.sub(r"(\|)$", "", pattern)
    pattern = r"\b("+ pattern + ")"
   
    
    return pattern

def sent_ext(sent):
    doc = nlp(sent) # sentence segmentation / select only sentence with verb
    for i, sentence in enumerate(doc.sentences):
        for token in sentence.tokens:
            if re.match(pattern,token.text):
                return sentence.text
            
            
def save(set_, path):
    with open(path, "w")as fout:
        json.dump(set_, fout)