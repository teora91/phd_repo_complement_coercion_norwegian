# Norwegian Aspectual Verbs Sentence Extractor 1.0

## Description
This project provides scripts and tools for extracting sentences containing aspectual verbs in Norwegian from the Norwegian Colossal Corpus (NCC).

> **Note:** Extracted sentences may include non-verbs, as the extractor matches strings with similar patterns to aspectual verbs. This method is employed to handle the vast size of the corpus, drastically reducing the sample size while preserving meaningful matches.

## Features
- **Efficient Pattern Matching:** Extracts sentences matching strings related to aspectual verbs. The list of aspectual verbs is found in __list_aspectual_verbs_nor.csv__
- **User-Friendly Outputs:** Extracted results saved in single CSV files for each sentence, preventing the generation of huge unmanageable files.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/teora91/phd-coercion.corpus.study.git
   cd APPENDIX_aspectual_verb_extractor_NCC_1.0
   ```
2. Install the required dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Ensure you have Python 3.10 or above installed.

## Usage
1. Run the extraction script:
   ```bash
   python NCC_extractor.py
   ```
4. Find the results in the sentence_list_NCC/ directory.


## Folder Structure
```
├── NCC_extractor.py
├── requirements.txt
├── list_aspectual_verbs_nor.csv
├── utils.py
├── sentence_list_NCC/
```

## Acknowledgements
- Special thanks to: 
	- NTNU for permitting the accomplishment of this project. 
	- Prof. Giosuè Baggio (NTNU) for his collaboration and suggestions.

## Contact Information
For questions or support, contact: 
- Email: matteo.radaelli91@gmail.com

## Badges
![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
