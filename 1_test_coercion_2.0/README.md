# Complement Coercion in Norwegian – Language Model Evaluation

Repository containing code and datasets used to evaluate **complement coercion in Norwegian language models with and without contextual information**.

The experiments investigate whether language models can retrieve **covert events** in coercion constructions. The repository contains the experimental pipeline used to test **17 Norwegian language models**, including masked language models and causal language models.

This repository supports the experiments presented in:

- Radaelli et al., **CoNLL 2025**
- Radaelli et al., **IWCS 2025**

---

# Complement Coercion

Complement coercion occurs when a verb that normally selects an **event** combines with an **entity-denoting noun**, forcing the interpretation of an implicit event.

Example:


Kim begynte på boken.
(Kim began the book.)


The sentence implies an event such as:

- read
- write

To test whether language models can infer these implicit events, the experiment prompts models to complete an interpretation sentence:


Det som Kim begynte å gjøre, var å [MASK].
(What Kim began to do was to [MASK].)


The language model must predict a **plausible eventive verb**.

---

# Experiment Design

Each experimental item consists of two sentences:

### 1. Coercion sentence


{SUBJ} {VERB-FIN} {PREP|Ø} {ENTITY-DEF}


Example:


Kim begynte på essayet.


### 2. Prompt sentence for event retrieval


Det som {SUBJ} begynte å gjøre, var å [MASK]


---

# Context Conditions

The dataset includes **four contextual conditions**.

### (a) Context-neutral


Kim begynte på essayet.


### (b) Subject-enriched context


Tolken begynte på essayet.
(The interpreter began the essay.)


### (c) Post-verbal context


Kim begynte på essayet ved hjelp av ordboken.
(Kim began the essay with the help of the dictionary.)


### (d) Discourse-level context


Kim ønsket å publisere sitt nye verk på et annet språk.
Kim begynte på essayet.


---

# Dataset

The dataset contains **4320 sentence pairs**.

Each item varies along several dimensions:

| Component | Description |
|---|---|
| Entities | 90 nouns across 6 semantic categories |
| Aspectual verbs | begynne, starte, fortsette, avslutte |
| Complement constructions | på + NP, med + NP, NP |
| Context conditions | 4 |

Entity categories include:

- food
- text
- clothing
- everyday objects
- construction/housing
- entertainment

---

# Tested Language Models

The experiments evaluate **17 pretrained Norwegian language models** available on HuggingFace.  
These models include both **masked language models (autoencoders)** and **causal language models (autoregressive)**.

### Masked Language Models

- `MBERT-CASED`
- `MBERT-UNCASED`
- `NB-BERT-BASE`
- `NB-BERT`
- `NORBERT`
- `NORBERT2`
- `NORBERT3-BASE`
- `NORBERT3-LARGE`
- `NORBERT3-SMALL`
- `NORBERT3-XS`

### Causal Language Models

- `NORGPT-369M`
- `NORGPT-3B`
- `NORGPT-3B-CONTINUE`
- `NORLLAMA-3B`
- `NORMISTRAL-7B-SCRATCH`
- `NORMISTRAL-7B-WARM`
- `NORBLOOM-7B-SCRATCH`  

Models differ in:

- architecture
- parameter size
- training data

Both **masked language models (MLMs)** and **causal language models (CLMs)** are evaluated.

## Repository Structure

```
.
├── data_for_task/
│   ├── llm_list_nor.json
│   ├── entity_verb_association.xlsx
│   ├── list_lemma_coercion_inflected.xlsx
│   └── experiment_coercion_dataset.xlsx
│
├── main.py
├── classification.py
├── MLM_model.py
├── CAUSAL_LM_model.py
├── fill_mask_mlm.py
├── import_data.py
├── merging_results.py
├── extract_predictions.py
├── utils.py
└── test_coercion_launcher.sh
```

# Script Overview

| Script | Description |
|---|---|
| `main.py` | Starts the experiment pipeline for a single language model |
| `test_coercion_launcher.sh` | Launches experiments for multiple models |
| `MLM_model.py` | Interface for masked language models |
| `CAUSAL_LM_model.py` | Interface for causal language models |
| `fill_mask_mlm.py` | Performs fill-mask predictions for MLMs |
| `classification.py` | Runs the classification stage of predictions |
| `import_data.py` | Loads datasets and lexical resources |
| `merging_results.py` | Merges results from all models |
| `extract_predictions.py` | Extracts predicted events and identifies new entity–event pairs |
| `utils.py` | Shared imports and utilities |

---

# Running the Experiments

Run the full pipeline with:

```bash
bash test_coercion_launcher.sh

The script iterates over the list of language models and runs the evaluation pipeline.

Internally it calls:

python main.py -idx N -c false
python main.py -idx N -c true

Parameters:

Argument	Description
-idx	Model index from the model list
-c false	Context-neutral condition
-c true	Context-enriched condition
Output

Results are generated dynamically when the experiments run.

A results folder is created automatically:

results_coercion_DATE/

Example outputs:

model_results_with_context_True.csv
model_results_with_context_False.csv
merged_results_coercion_updated_DATE_with_context_True.csv
merged_results_coercion_updated_DATE_with_context_False.csv

The script extract_predictions.py identifies new entity–event pairs not yet present in the semantic classification table and exports them for manual annotation.

Citation

If you use this repository or dataset, please cite:

@inproceedings{radaelli2025compositionality,
  title = {Compositionality and Event Retrieval in Complement Coercion: A Study of Language Models in a Low-resource Setting},
  author = {Radaelli, Matteo and Chersoni, Emmanuele and Lenci, Alessandro and Baggio, Giosu{\`e}},
  booktitle = {Proceedings of the 29th Conference on Computational Natural Language Learning (CoNLL)},
  pages = {469--480},
  address = {Vienna, Austria},
  publisher = {Association for Computational Linguistics},
  year = {2025},
  doi = {10.18653/v1/2025.conll-1.31},
  url = {https://aclanthology.org/2025.conll-1.31/}
}

@inproceedings{radaelli2025context,
  title = {Context Effects on the Interpretation of Complement Coercion: A Comparative Study with Language Models in Norwegian},
  author = {Radaelli, Matteo and Chersoni, Emmanuele and Lenci, Alessandro and Baggio, Giosu{\`e}},
  booktitle = {Proceedings of the 16th International Conference on Computational Semantics (IWCS)},
  pages = {78--88},
  address = {D{\"u}sseldorf, Germany},
  publisher = {Association for Computational Linguistics},
  year = {2025},
  url = {https://aclanthology.org/2025.iwcs-main.7/}
}
