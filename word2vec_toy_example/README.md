# Toy example: Word2Vec Trainer & Visualization

A toy example of training **dense word embeddings** using a Skip-gram Word2Vec model. 

The project trains a small embedding space from a small set of text corpus and further visualized using PCA projection. 

*word2vec_toy_example* was used as illustrative example of distributional semantic models introduced in Section 3.2. 

---

## Demo

The script includes

* Building a corpus/data preprocessing pipeline (loading + tokenization). The corpus includes a small set of sentences designed to encode clear, visually separable distributional information (e.g., coffee/cafe, animals/pets, and books/reading).
* Training Word2Vec model, including learning semantic similarity from co-occurrence statistics of single token
* Using cosine similarity to measure meaning relatedness
* Projecting embeddings into 2D space for visualization

Example output:

```
Cosine similarities (higher = closer in embedding space):
  espresso ~ coffee  : 0.82
  espresso ~ barista : 0.71
  espresso ~ dog     : 0.05
  dog ~ cat          : 0.76
  dog ~ cafe         : 0.09
```

---

## Repository structure

```
word2vec_toy_example
├── corpus.txt
├── word2vec_trainer_visualization.py
├── word2vec_trainer_visualization.ipynb (in notebook version)
├── requirements.txt
└── plot_toy_embeddings.png   (generated after running)
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/teora91/phd_repo_complement_coercion_norwegian.git
cd word2vec_toy_example
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the project

```bash
python word2vec_trainer_visualization.py
```

The script will:

1. Load the corpus
2. Tokenize and normalize text
3. Train a Skip-gram Word2Vec model
4. Print similarity scores
5. Generate/Save a 2D embedding plot

---

## Output

After execution:

```
plot_toy_embeddings.png
```

This figure shows clusters of semantically related words in the learned vector space.

---

## Customization

Modify parameters inside `train_model()`:

| Parameter     | Description                   |
| ------------- | ----------------------------- |
| `vector_size` | embedding dimensionality      |
| `window`      | context window size           |
| `sg`          | 1 = Skip-gram, 0 = CBOW       |
| `negative`    | negative sampling             |
| `epochs`      | number of training iterations |

---
## License

MIT License — free for research and teaching.
