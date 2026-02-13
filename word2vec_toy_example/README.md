# Toy Word2Vec Trainer & Visualization

A minimal educational repository showing how **word embeddings emerge from raw text** using a Skip-gram Word2Vec model and how they can be inspected visually in 2D.

The project trains a small embedding space from a plain text corpus and demonstrates semantic structure (e.g., *coffee* closer to *espresso* than to *dog*) using PCA projection.

---

## What this project demonstrates

This repository is intentionally simple and designed for teaching / understanding.

It illustrates:

* Building a corpus pipeline (reading + tokenization)
* Learning semantic similarity from co-occurrence statistics
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
.
├── corpus.txt
├── word2vec_trainer_visualization.py
├── requirements.txt
└── plot_toy_embeddings.png   (generated after running)
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/toy-word2vec-demo.git
cd toy-word2vec-demo
```

---

### 2. Create a virtual environment (recommended)

#### Using venv

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
.venv\\Scripts\\activate
```

#### Using conda (optional)

```bash
conda create -n word2vec-demo python=3.10
conda activate word2vec-demo
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Prepare the corpus

Create a file named:

```
corpus.txt
```

Each line must be one sentence.

Example:

```
I drank an espresso at the cafe
The barista served hot coffee
My dog chased the cat
The pet drank milk
The cafe serves good coffee
```

The model learns purely from these co-occurrence patterns.

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
5. Generate a 2D embedding plot

---

## Output

After execution:

```
plot_toy_embeddings.png
```

This figure shows clusters of semantically related words in the learned vector space.

---

## How it works (conceptual overview)

The model follows the **distributional hypothesis**:

> Words that appear in similar contexts tend to have similar meanings.

Skip-gram objective:

Given a target word, predict its surrounding context words.

Because words like:

```
espresso, coffee, cafe, barista
```

share contexts, they become close in the vector space.

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

## Educational purpose

Useful for:

* NLP teaching
* explaining distributional semantics
* lecture demonstrations
* quick embedding intuition experiments

---

## License

MIT License — free for research and teaching.
