# 🔢 Text Representation in NLP

## 1. Introduction

**Text Representation** is the process of converting human-readable text into numerical form so that computers and machine learning models can process it.

Humans understand words, sentences, and their meanings. However, machine learning models work with numerical data.

For example:

`I love Natural Language Processing.`

A computer cannot directly perform mathematical operations on this sentence.

Therefore, NLP techniques convert text into numerical representations that models can use for learning, analysis, and prediction.

**In simple words:** Text Representation converts text into numbers that computers can process.

## 2. Why Do We Need Text Representation?

Text representation is an important part of NLP because machine learning and deep learning models require numerical input.

Its importance includes:

- Converting text into numerical data.
- Making text suitable for mathematical operations.
- Helping models identify patterns in language.
- Representing relationships between words.
- Providing numerical input to NLP models.

Without numerical representation, most NLP models cannot directly process human-readable text.

## 3. Different Methods of Text Representation

There are several techniques used to convert text into numerical representations.

Some common approaches are:

1. One-Hot Encoding
2. Bag of Words (BoW)
3. TF-IDF
4. Word Embeddings
5. Contextual Embeddings

### 3.1 One-Hot Encoding

**One-Hot Encoding** represents each word using a binary vector.

Each word receives a vector in which one position contains `1` and all other positions contain `0`.

**Example:**

Consider this vocabulary:

`["I", "love", "NLP"]`

One-Hot Representation:

| Word | I | love | NLP |
|---|---:|---:|---:|
| I | 1 | 0 | 0 |
| love | 0 | 1 | 0 |
| NLP | 0 | 0 | 1 |

Each word has a unique binary representation.

**Advantages:**
- Simple to understand.
- Easy to implement.
- Provides a unique representation for each vocabulary word.

**Limitations:**
- Creates large vectors for large vocabularies.
- Does not capture semantic relationships.
- Similar words do not have similar representations.

### 3.2 Bag of Words (BoW)

**Bag of Words (BoW)** represents text based on the frequency of words appearing in a document.

It creates a vocabulary from the available text and counts how many times each word appears.

Word order and grammar are generally ignored.

**Example:**

Document 1:

`I love NLP`

Document 2:

`I love AI`

Vocabulary:

`["I", "love", "NLP", "AI"]`

Bag of Words Representation:

| Document | I | love | NLP | AI |
|---|---:|---:|---:|---:|
| Document 1 | 1 | 1 | 1 | 0 |
| Document 2 | 1 | 1 | 0 | 1 |

Each document is represented as a numerical vector.

**Advantages:**
- Simple and easy to understand.
- Represents word frequency.
- Useful for basic text classification.

**Limitations:**
- Ignores word order.
- Does not understand context.
- Can create large and sparse vectors.

### 3.3 TF-IDF

**TF-IDF** stands for Term Frequency–Inverse Document Frequency.

It is a numerical representation technique that measures how important a word is in a document compared with a collection of documents.

It combines two values:

**Term Frequency (TF):**

Measures how frequently a word appears in a particular document.

**Inverse Document Frequency (IDF):**

Measures how rare or common a word is across the entire collection of documents.

The basic formula is:

\[
TF\text{-}IDF = TF \times IDF
\]

A word that appears frequently in one document but rarely across other documents can receive a higher TF-IDF score.

**Example:**

Consider two documents:

- Document 1: `I love machine learning`
- Document 2: `I love deep learning`

The words `I` and `love` appear in both documents, while `machine` and `deep` appear in only one document each.

TF-IDF can assign more importance to words that help distinguish one document from another.

**Advantages:**
- Considers word importance.
- Reduces the influence of very common words.
- Useful for search and text classification.

**Limitations:**
- Does not understand word meaning.
- Does not capture contextual relationships.
- Produces sparse numerical representations.

### 3.4 Word Embeddings

**Word Embeddings** represent words as dense numerical vectors.

Unlike One-Hot Encoding and Bag of Words, embeddings can capture semantic and syntactic relationships between words.

Words with similar meanings can have similar vector representations.

**Example:**

Words such as:

- King
- Queen
- Man
- Woman

Can have numerical representations that capture relationships between them.

A simplified example:

```text
King  → [0.21, 0.45, 0.78]
Queen → [0.23, 0.43, 0.75]
Apple → [0.82, 0.14, 0.31]
```

These values are illustrative, not actual pretrained embeddings.

**Advantages:**
- Dense numerical representations.
- Can capture semantic relationships.
- More compact than large one-hot vectors.

**Limitation:**

Traditional word embeddings generally assign the same vector to a word regardless of its context.

### 3.5 Contextual Embeddings

**Contextual Embeddings** represent words based on their surrounding context.

Unlike traditional word embeddings, the same word can have different representations depending on how it is used in a sentence.

**Example:**

Sentence 1:

`I deposited money in the bank.`

Sentence 2:

`She sat near the river bank.`

The word `bank` has different meanings in these sentences.

Contextual embeddings help models understand these differences by considering surrounding words.

Modern Transformer models such as BERT generate contextual representations.

**Advantages:**
- Understands contextual relationships.
- Handles words with multiple meanings.
- Captures information from surrounding words.
- Useful for advanced NLP tasks.

## 4. Comparison of Text Representation Techniques

| Technique | Representation | Understands Meaning? | Uses Context? |
|---|---|---|---|
| One-Hot Encoding | Binary vectors | No | No |
| Bag of Words | Word counts | No | No |
| TF-IDF | Weighted word counts | No | No |
| Word Embeddings | Dense vectors | Partially | Generally no |
| Contextual Embeddings | Context-dependent vectors | Yes, through learned representations | Yes |

## 5. Sparse vs Dense Representations

Text representations can also be categorized as sparse or dense.

### Sparse Representation

A sparse representation contains many zero values.

Examples:
- One-Hot Encoding.
- Bag of Words.
- TF-IDF.

Example:

```text
[1, 0, 0, 0, 0, 1, 0, 0]
```

### Dense Representation

A dense representation contains meaningful numerical values across most vector positions.

Examples:
- Word Embeddings.
- Contextual Embeddings.

Example:

```text
[0.21, 0.45, 0.78, 0.32]
```

## 6. Text Representation in Modern NLP

Modern NLP models commonly use embedding layers to convert token IDs into dense numerical vectors.

Transformer models then process these representations to learn relationships between tokens and their surrounding context.

A simplified process is:

**Text → Tokenization → Token IDs → Embeddings → Transformer Model**

Hugging Face Transformers provides pretrained models that can generate these numerical representations.

For example, BERT can generate contextual representations for input tokens.

## 7. Key Takeaways

- Text Representation converts human language into numerical data.
- One-Hot Encoding assigns a binary vector to each word.
- Bag of Words represents documents using word frequencies.
- TF-IDF measures the importance of words across documents.
- Word Embeddings represent words as dense numerical vectors.
- Contextual Embeddings generate representations based on surrounding words.
- Sparse representations contain many zero values.
- Dense representations contain meaningful numerical values across vector dimensions.
- Modern Transformer models use embeddings to process text.
