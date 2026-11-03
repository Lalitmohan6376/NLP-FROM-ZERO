# 🧠 Word Embeddings

## 1. What are Word Embeddings?

Word Embeddings are a technique used in NLP to convert words into numerical vectors (arrays of numbers).

Machine learning models cannot directly understand words like `"king"`, `"queen"`, or `"computer"`. They need numerical representations to process text.

Word Embeddings represent each word as a dense vector, where the values capture useful information about the word's meaning and relationships with other words.

**Example:**

```text
king    → [0.25, 0.81, 0.42, 0.17]
queen   → [0.29, 0.78, 0.45, 0.21]
apple   → [0.91, 0.12, 0.63, 0.37]
```

These are illustrative vectors, not actual model outputs.

Words with similar meanings or usage patterns may have similar vector representations.

---

## 2. Why Do We Need Word Embeddings?

Earlier text representation techniques, such as One-Hot Encoding and Bag of Words, have some limitations:

- They create sparse vectors containing mostly zeros.
- They do not directly capture semantic relationships between words.
- They treat words as separate features without representing their similarity.

Word Embeddings help address these limitations.

**Example:**

Consider these words:

```text
car
vehicle
banana
```

The words `"car"` and `"vehicle"` are related in meaning, while `"banana"` is different.

A good embedding model can represent `"car"` and `"vehicle"` with vectors that are closer to each other than to `"banana"`.

---

## 3. How Do Word Embeddings Work?

Word Embedding models learn numerical representations from large amounts of text.

During training, the model learns patterns based on how words appear in different contexts.

For example:

```text
The cat is drinking milk.
The dog is drinking water.
```

The model observes how words are used in sentences and learns relationships between them.

After training, each word can be represented by a dense numerical vector.

**Basic Process:**

1. Collect a large text dataset.
2. Process and tokenize the text.
3. Train an embedding model on the text.
4. The model learns numerical representations for words.
5. Use the learned vectors in NLP tasks.

---

## 4. Types of Word Embedding Techniques

### A. Word2Vec

Word2Vec is a popular word embedding technique developed by Google.

It learns word representations by predicting relationships between words in a sentence.

It has two main architectures:

**1. CBOW (Continuous Bag of Words)**

- Predicts a target word using its surrounding context words.
- Uses nearby words to understand which word is missing.

Example:

```text
The cat is ___ milk.

Context Words:
The, cat, is, milk

Target Word:
drinking
```

**2. Skip-Gram**

- Predicts surrounding context words using a target word.
- Uses one word to identify the words that commonly appear around it.

Example:

```text
Target Word:
drinking

Context Words:
cat, is, milk
```

### B. GloVe (Global Vectors)

GloVe is a word embedding technique developed at Stanford University.

It learns word representations by using global word co-occurrence statistics from a text corpus.

In simple terms:

- It examines how frequently words appear together.
- It builds relationships using word co-occurrence information.
- It converts words into dense numerical vectors.

### C. FastText

FastText is a word embedding technique developed by Facebook AI Research.

Unlike traditional Word2Vec, FastText represents words using character-level subwords (character n-grams).

Example:

```text
playing

Possible Subwords:
pla
lay
ayi
yin
ing
```

It combines information from these subwords to create a word representation.

This can help with rare words and words that were not directly seen during training.

---

## 5. Word Embeddings vs One-Hot Encoding

| Feature | One-Hot Encoding | Word Embeddings |
|---|---|---|
| Representation | Binary vector | Dense vector |
| Values | 0 and 1 | Real numbers |
| Vector Size | Vocabulary size | Usually fixed dimensions |
| Semantic Meaning | Not directly captured | Can capture semantic relationships |
| Similarity | Words are equally distinct | Similar words can have similar vectors |
| Storage | Often sparse | Usually dense |

**Example:**

One-Hot Encoding:

```text
cat     → [1, 0, 0, 0]
dog     → [0, 1, 0, 0]
apple   → [0, 0, 1, 0]
car     → [0, 0, 0, 1]
```

Word Embeddings:

```text
cat     → [0.21, 0.54, 0.81]
dog     → [0.24, 0.57, 0.79]
apple   → [0.91, 0.13, 0.32]
car     → [0.62, 0.74, 0.18]
```

The embedding values above are only illustrative.

---

## 6. Advantages of Word Embeddings

- **Dense Representation:** Uses compact numerical vectors instead of mostly-zero vectors.
- **Semantic Relationships:** Can capture similarities and relationships between words.
- **Lower Dimensionality:** Usually represents words using fewer dimensions than vocabulary-sized One-Hot vectors.
- **Better NLP Features:** Provides useful numerical representations for many NLP tasks.
- **Reusable:** Pretrained embeddings can be used in different machine learning applications.

## 7. Limitations of Word Embeddings

- **One Representation Per Word:** Traditional Word2Vec, GloVe, and FastText generally provide one learned vector per word.
- **Limited Context Understanding:** They do not automatically change a word's representation based on its sentence.
- **Ambiguous Words:** Different meanings of the same word can be difficult to represent with a single vector.

Example:

```text
I deposited money in the bank.

I sat near the river bank.
```

The word `"bank"` has different meanings in these sentences, but traditional static word embeddings generally assign it the same learned representation.

Contextual Embeddings help address this limitation.

---

## 8. Applications of Word Embeddings

Word Embeddings are useful in several NLP applications:

- Sentiment Analysis
- Text Classification
- Text Similarity
- Named Entity Recognition (NER)
- Machine Translation
- Search and Information Retrieval
- Recommendation Systems

---

## 9. Word Embeddings in Modern NLP

Word2Vec, GloVe, and FastText are examples of **static word embedding techniques**.

Modern Transformer-based models, such as BERT, also use embedding layers. However, they combine token embeddings with other information and produce contextual representations through Transformer layers.

This means the representation of a word can change depending on the sentence in which it appears.

For example:

```text
He deposited money in the bank.

He sat near the river bank.
```

A contextual model can generate different representations for `"bank"` in these two sentences.

---

## 10. Key Takeaways

- Word Embeddings convert words into dense numerical vectors.
- They help represent semantic relationships between words.
- Word2Vec, GloVe, and FastText are popular embedding techniques.
- CBOW predicts a target word from its context.
- Skip-Gram predicts context words from a target word.
- Traditional word embeddings generally assign one representation to each word.
- Contextual Embeddings generate representations based on surrounding text.
