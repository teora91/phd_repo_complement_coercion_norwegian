#!/bin/bash
#Getting the length of the json dictionary

len_=$(jq 'length' data_for_task/llm_list_nor.json)
echo Total grouped models: $len_

echo Classification Started...
for n in $(seq 1 $len_);
# for n in 1 2;

do
    python main.py -idx $n -c false
    python main.py -idx $n -c true

    
done

echo Merging Results...
python merging_results.py

echo Extracting Predictions...
python extract_predictions.py


echo SCRIPT ENDED
