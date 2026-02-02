# Complement Coercion in Norwegian: A Computational Linguistics Research

This repository contains the code, data, and evaluation scripts for the PhD research project *Complement Coercion in Norwegian: A Computational Linguistics Research*.

## Thesis Abstract

This dissertation investigates the representation of **complement coercion** in Norwegian. Complement coercion refers to the phenomenon in which an aspectual verb (e.g., *begin*), which typically selects for an event-denoting argument (e.g., *John began the concert*), is instead combined with an entity-denoting one (e.g., *John began the book*). The resulting semantic type mismatch is resolved by inferring an implicit event from information provided by the sentence’s constituents, including lexical semantics, world knowledge, and discourse context.

Despite the rich body of literature on complement coercion, the phenomenon remains underexplored in languages that are considered under-resourced, such as Norwegian. This gap limits our understanding of how complement coercion is syntactically and semantically realized across languages and how it is used in naturally occurring data. Moreover, with the advent of modern transformer-based language models, a systematic investigation of complement coercion has become increasingly relevant, as it constitutes a complex inference-based task that requires the extraction of underlying compositional information from linguistic input.

This thesis addresses these gaps by dividing the research into two main parts. The first part presents a corpus-based analysis of complement coercion in Norwegian, aimed at identifying the syntactic and semantic configurations that trigger coercion and assessing their distribution in naturally occurring data. The analysis reveals heterogeneous coercion configurations that vary according to the aspectual verb involved, as well as a restricted set of entity-denoting arguments that systematically trigger coercion. In addition, the results show that complement coercion is relatively infrequent in natural language use, suggesting that Norwegian speakers often prefer alternative, less ambiguous constructions conveying equivalent meanings.

The second part of the thesis evaluates whether pretrained language models interpret complement coercion constructions consistently. Two experiments are conducted to address distinct research questions. The first examines whether models can exploit compositional information in coercion sentences and whether syntactic variation provides informative cues for event interpretation. The second investigates the role of context, focusing on how different types of contextual enrichment influence model performance. These experiments are conducted on seventeen language models that vary in architecture and size.

The results indicate that complement coercion poses a substantial challenge for language models, which struggle to consistently recover the intended event interpretations. Qualitative analyses suggest that model predictions rely predominantly on distributional regularities and frequency-driven biases learned during pretraining, rather than on the exploitation of compositional semantic information. Consequently, models tend to favor frequent and strongly associated event interpretations, while less frequent but contextually appropriate events are often overlooked. Although contextual enrichment leads to systematic performance improvements, these gains are likely attributable to the presence of additional lexical-semantic cues reinforcing existing distributional biases, rather than to genuine compositional inference.

## Research Scope

The aim of this project is to investigate how modern multilingual language models represent and process complement coercion phenomena in Norwegian, with a particular focus on:

* **Verb-specific coercion constructions** (e.g., *begynne på* vs. *avslutte*)
* **Cross-model comparison** across encoder-based (e.g., BERT) and decoder-based (e.g., GPT) architectures
* **Surprisal analysis** to quantify model expectations in coercive contexts
* **Lexical semantic and compositional evaluation** using top-*k* predictions and plausibility criteria

The project includes:

* Corpus preparation and annotation for coercion phenomena
* Standardized evaluation pipelines for typological analysis
* Scripts for surprisal computation on masked and autoregressive architectures
* Benchmarks and visualization tools for model behavior analysis

## Authorship and Supervision

This repository is developed and maintained by **Matteo Radaelli** as part of his PhD research in Computational Linguistics at the Norwegian University of Science and Technology (NTNU). The work is carried out in collaboration with, and under the supervision of:

* [**Giosuè Baggio**](https://www.ntnu.edu/employees/giosue.baggio) — Professor of Cognitive Science, NTNU. Email: [giosue.baggio@ntnu.no](mailto:giosue.baggio@ntnu.no)
* [**Emanuele Chersoni**](https://research.polyu.edu.hk/en/persons/emmanuele-chersoni/) — Assistant Professor, The Hong Kong Polytechnic University. Email: [emmanuele.chersoni@polyu.edu.hk](mailto:emmanuele.chersoni@polyu.edu.hk)
* [**Alessandro Lenci**](https://people.unipi.it/alessandro_lenci/) — Professor, University of Pisa. Email: [alessandro.lenci@unipi.it](mailto:alessandro.lenci@unipi.it)

## Contact

For questions, feedback, or collaboration inquiries related to this project, please contact:

[**Matteo Radaelli**](https://www.ntnu.no/ansatte/mattera) <br>
PhD Candidate in Computational Linguistics<br> 
Trondheim, Norway<br>
Email: [matteo.radaelli@ntnu.no](mailto:matteo.radaelli@ntnu.no)

## 📂 Repository Structure

```text
phd_repo_complement_coercion_norwegian/
├── data/
│   ├── raw/                  # Native texts and corpus sources
│   ├── processed/            # Tokenized & annotated coercion items
│   └── annotations/          # Linguistic annotations & metadata
├── src/
│   ├── preprocessing/        # Tokenization, normalization routines
│   ├── evaluation/           # Model evaluation scripts
│   ├── surprisal/            # Surprisal computation & analysis code
│   └── utils/                # Auxiliary functions
├── experiments/              # Notebooks and experiment logs
├── results/                  # Evaluation outputs & visualizations
├── environment.yml           # Reproducible environment spec
├── setup.py                  # Installation script
└── README.md                # This file
```
