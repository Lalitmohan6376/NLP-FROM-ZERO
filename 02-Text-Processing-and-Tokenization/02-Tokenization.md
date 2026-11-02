# 🔤 Tokenization in NLP

## 1. Introduction

**Tokenization** is the process of breaking text into smaller units called **tokens**.

A token can be a word, subword, or character, depending on the tokenization method.

NLP models do not directly understand sentences like humans. Tokenization helps convert text into smaller units that can be processed by a model.

**Example:**

Input Text:

`I love Natural Language Processing.`

Tokens:

`["I", "love", "Natural", "Language", "Processing", "."]`

Here, the sentence is divided into individual tokens.

## 2. Why is Tokenization Important?

Tokenization is one of the fundamental steps in NLP because it helps models process text in a structured way.

Its importance includes:

- Dividing text into manageable units.
- Preparing text for numerical representation.
- Identifying individual words or subwords.
- Handling unknown and uncommon words.
- Providing input to NLP models.

Without tokenization, converting text into the format expected by most NLP models would be difficult.

## 3. Types of Tokenization

There are three commonly discussed tokenization approaches.

### 3.1 Word-Level Tokenization

Word-level tokenization divides a sentence into individual words.

**Example:**

Input:

`I love learning NLP.`

Tokens:

`["I", "love", "learning", "NLP."]`

Each word is treated as a separate token.

**Limitation:**

- Vocabulary can become very large.
- New or unknown words may be difficult to handle.
- Different word forms may need separate vocabulary entries.

### 3.2 Character-Level Tokenization

Character-level tokenization divides text into individual characters.

**Example:**

Input:

`Hello`

Tokens:

`["H", "e", "l", "l", "o"]`

Each character becomes an individual token.

**Advantages:**

- Very small vocabulary.
- Can represent almost any word using individual characters.
- Does not require a separate vocabulary entry for every word.

**Limitations:**

- Produces many tokens.
- Loses direct word-level information.
- Models may need to process longer sequences.

### 3.3 Subword-Level Tokenization

Subword tokenization divides words into smaller meaningful or frequently occurring pieces.

**Example:**

A tokenizer might divide:

`unhappiness`

Into:

`["un", "happiness"]`

The exact output depends on the tokenizer and its vocabulary.

**Advantages:**

- Handles uncommon words better than word-level tokenization.
- Maintains a manageable vocabulary.
- Can represent many words using smaller units.

Modern Transformer models commonly use subword-based tokenization.

## 4. Comparison of Tokenization Types

| Word-Level | Character-Level | Subword-Level |
|---|---|---|
| Divides text into words. | Divides text into characters. | Divides text into smaller word pieces. |
| Larger vocabulary. | Smaller vocabulary. | Balanced vocabulary size. |
| Unknown words can be a problem. | Can represent new words using characters. | Can represent many uncommon words. |
| Usually fewer tokens per sentence. | Usually more tokens per sentence. | Usually between word and character level. |

## 5. Common Subword Tokenization Algorithms

Modern NLP models use different algorithms to divide text into subwords.

### 5.1 Byte Pair Encoding (BPE)

**Byte Pair Encoding (BPE)** is a subword tokenization algorithm that builds a vocabulary by repeatedly merging frequently occurring character sequences or token pairs.

Basic idea:

1. Start with smaller units.
2. Identify frequently occurring adjacent pairs.
3. Merge frequent pairs.
4. Repeat until the desired vocabulary is created.

BPE is used in several language models and tokenizers.

### 5.2 WordPiece

**WordPiece** is a subword tokenization algorithm that builds a vocabulary of useful word pieces.

It divides words into smaller units when a complete word is not available in the vocabulary.

For example, a word may be divided into:

`["play", "##ing"]`

Here, `##` indicates that the subword continues from the previous piece.

WordPiece is associated with BERT tokenization.

### 5.3 SentencePiece

**SentencePiece** is a tokenizer framework that can train subword tokenization models directly from raw text.

It supports algorithms such as:

- BPE
- Unigram Language Model

SentencePiece is used in models such as T5 and several multilingual models.

## 6. Tokenization in Transformer Models

Modern Transformer models use model-specific tokenizers.

Different models can produce different tokens for the same input sentence because they may use different vocabularies and tokenization algorithms.

For example:

- BERT commonly uses WordPiece.
- GPT-2 uses Byte Pair Encoding (BPE).
- T5 uses SentencePiece.

Hugging Face Transformers provides the `AutoTokenizer` class to load the tokenizer associated with a pretrained model.

Example:

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "I love learning NLP."

tokens = tokenizer.tokenize(text)

print(tokens)
```

Output:

```text
['i', 'love', 'learning', 'nl', '##p', '.']
```

*Note: The exact output depends on the selected pretrained tokenizer.*

## 7. Important Tokenization Terms

| Term | Meaning |
|---|---|
| Token | A smaller unit of text. |
| Vocabulary | Collection of tokens known to a tokenizer. |
| Subword | A smaller piece of a word. |
| Unknown Token | A special token used when text cannot be represented by the tokenizer's vocabulary or rules. |
| Tokenizer | A component that converts text into tokens and model inputs. |

## 8. Key Takeaways

- Tokenization divides text into smaller units called tokens.
- Word-level tokenization separates text into words.
- Character-level tokenization separates text into characters.
- Subword-level tokenization divides words into smaller pieces.
- BPE, WordPiece, and SentencePiece are common subword approaches.
- Modern Transformer models use their own tokenizers.
- Hugging Face Transformers provides `AutoTokenizer` to load pretrained tokenizers.
- The tokenizer should match the pretrained model being used.
