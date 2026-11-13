# 🧠 BERT Model

## 📌 Introduction

**BERT (Bidirectional Encoder Representations from Transformers)** is a pretrained language model developed by Google and introduced in 2018.

BERT is based on the **Encoder-only Transformer architecture**. It is designed to understand the meaning and context of words in a sentence.

Unlike traditional language models that process text in only one direction, BERT uses bidirectional context. This means it considers both the left and right sides of a token to understand its meaning.

### 🔍 Example

Consider the word `bank` in two sentences:

```text
Sentence 1: I deposited money in the bank.

Sentence 2: We sat beside the river bank.
```

The word `bank` has different meanings in these sentences.

BERT uses the surrounding words from both directions to understand the correct meaning.

---

## 1️⃣ BERT Architecture

BERT is built using the **Transformer Encoder** architecture.

It contains multiple encoder layers stacked together. Each encoder layer consists of:

1. Multi-Head Self-Attention
2. Feed-Forward Neural Network
3. Residual Connections
4. Layer Normalization

### ⚙️ Basic Architecture Flow

```text
             Input Text
                 |
                 v
              Tokenizer
                 |
                 v
             Token IDs
                 |
                 v
        Input Embeddings
                 |
                 v
        Transformer Encoder
                 |
                 v
       Contextual Representations
                 |
                 v
          Output Layer
                 |
                 v
          NLP Prediction
```

BERT does not contain a Transformer decoder. Its encoder layers generate contextual representations that can be used for different NLP tasks.

### 🏗️ BERT Model Variants

Two original BERT configurations are:

| Model | Transformer Layers | Hidden Size | Attention Heads | Parameters |
|---|---:|---:|---:|---:|
| BERT Base | 12 | 768 | 12 | 110M |
| BERT Large | 24 | 1024 | 16 | 340M |

BERT Large has more layers, a larger hidden representation, and more parameters than BERT Base.

---

## 2️⃣ Bidirectional Context Understanding

The main feature of BERT is its ability to understand tokens using both left and right context.

Consider:

```text
The animal did not cross the road because it was tired.
```

To understand the word `it`, BERT can use information from the surrounding words.

### 🔍 Directional Understanding

**Left Context:**

```text
The animal did not cross the road because
```

**Right Context:**

```text
was tired.
```

BERT uses both directions together to build contextual representations.

This makes it useful for tasks that require understanding the meaning of words and sentences.

---

## 3️⃣ Input Representation in BERT

BERT uses three types of embeddings to represent its input:

1. Token Embeddings
2. Segment Embeddings
3. Position Embeddings

These embeddings are combined to create the final input representation.

### 🔹 Token Embeddings

Token embeddings represent the tokens in the input sequence.

BERT uses WordPiece tokenization to split text into tokens.

Example:

```text
Input:
I love NLP.

Tokens:
[CLS] I love NL ##P . [SEP]
```

The exact tokenization depends on the tokenizer vocabulary.

Each token is converted into an embedding vector.

### 🔹 Segment Embeddings

Segment embeddings identify which sentence a token belongs to.

They are useful when BERT processes two sentences together.

Example:

```text
Sentence A: I love NLP.
Sentence B: Transformers are interesting.

Combined Input:
[CLS] I love NLP . [SEP]
Transformers are interesting . [SEP]
```

- Tokens belonging to Sentence A receive segment ID 0.
- Tokens belonging to Sentence B receive segment ID 1.

For a single-sentence input, the segment ID is generally 0.

### 🔹 Position Embeddings

Position embeddings provide information about the position of each token in the sequence.

For example:

```text
Tokens:
I       love       NLP

Position:
0        1          2
```

This allows BERT to distinguish token positions because self-attention alone does not represent the original order of tokens.

### 🧩 Final Input Representation

BERT combines all three embeddings:

```text
Final Input Embedding =
Token Embedding
+ Segment Embedding
+ Position Embedding
```

The combined embeddings are passed through the Transformer encoder layers.

---

## 4️⃣ Special Tokens in BERT

BERT uses special tokens to structure its input.

| Token | Purpose |
|---|---|
| `[CLS]` | Added at the beginning of the input sequence |
| `[SEP]` | Separates sentences and marks sequence boundaries |
| `[MASK]` | Used to hide tokens during masked language modeling |
| `[PAD]` | Used to make sequences equal in length |
| `[UNK]` | Represents an unknown token |

### 🔍 Example

```text
Input:
I love learning NLP.

BERT Input:
[CLS] I love learning NLP . [SEP]
```

The `[CLS]` token is commonly used as a sequence-level representation for classification tasks.

The `[SEP]` token marks the end of the input sequence or separates two input sentences.

---

## 5️⃣ BERT Pretraining

BERT was originally pretrained using two objectives:

1. Masked Language Modeling (MLM)
2. Next Sentence Prediction (NSP)

These objectives help BERT learn language patterns and relationships between text.

### 🔹 Masked Language Modeling (MLM)

In Masked Language Modeling, some input tokens are selected and hidden during training.

BERT learns to predict the original tokens using the surrounding context.

**Example:**

```text
Original:
The movie was really good.

Masked Input:
The movie was [MASK] good.

BERT Prediction:
really
```

BERT uses both left and right context to predict the masked token.

In the original BERT training setup, 15% of tokens were selected for prediction.

The selected tokens were not all replaced with `[MASK]`:

- 80% were replaced with `[MASK]`.
- 10% were replaced with a random token.
- 10% were kept unchanged.

This helped BERT learn useful contextual representations.

### 🔹 Next Sentence Prediction (NSP)

Next Sentence Prediction trains BERT to understand the relationship between two sentences.

The model receives two sentences and predicts whether the second sentence actually follows the first sentence in the original text.

**Example 1: IsNext**

```text
Sentence A:
I went to the library.

Sentence B:
I borrowed a book.

Label:
IsNext
```

**Example 2: NotNext**

```text
Sentence A:
I went to the library.

Sentence B:
The weather is very cold today.

Label:
NotNext
```

The original BERT training process used both related and randomly sampled sentence pairs.

**Note:** Later models such as RoBERTa removed NSP and used a different pretraining strategy. NSP is part of the original BERT approach, not a compulsory objective for every BERT-based model.

---

## 6️⃣ BERT Fine-Tuning

After pretraining, BERT can be fine-tuned for specific NLP tasks.

Fine-tuning means taking a pretrained BERT model and training it further on a task-specific dataset.

### ⚙️ Fine-Tuning Process

```text
        Pretrained BERT
               |
               v
       Task-Specific Layer
               |
               v
       Task-Specific Dataset
               |
               v
           Training
               |
               v
        Fine-Tuned BERT
               |
               v
        Task Predictions
```

For example, in sentiment analysis:

```text
Input:
This movie is amazing.

        |
        v

    BERT Model
        |
        v

 Classification Layer
        |
        v

Prediction:
Positive
```

The pretrained BERT model provides contextual representations, while the additional classification layer produces the final prediction.

During traditional full fine-tuning, the model's parameters and task-specific layer are updated using the task-specific dataset.

---

## 7️⃣ Applications of BERT

BERT is widely used for NLP tasks that require language understanding.

### 🎯 Common Applications

| Application | Description |
|---|---|
| Sentiment Analysis | Identifies positive, negative, or neutral sentiment |
| Text Classification | Assigns categories to input text |
| Named Entity Recognition | Identifies names, locations, organizations, and other entities |
| Question Answering | Finds answers to questions from a given context |
| Semantic Similarity | Compares the meaning of sentences |
| Part-of-Speech Tagging | Identifies grammatical categories of words |

---

## 8️⃣ Using BERT with Hugging Face Transformers

The Hugging Face Transformers library makes it easy to load and use pretrained BERT models.

### 🔹 Loading a BERT Tokenizer

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "I love learning NLP."

tokens = tokenizer.tokenize(text)

print(tokens)
```

**Explanation:**

- `AutoTokenizer` loads the tokenizer associated with the checkpoint.
- `from_pretrained()` loads the tokenizer vocabulary and configuration.
- `tokenize()` converts input text into tokens.

### 🔹 Loading a Pretrained BERT Model

```python
from transformers import AutoModel

model = AutoModel.from_pretrained("bert-base-uncased")

print(model)
```

`AutoModel` loads the base BERT architecture and pretrained weights without adding a task-specific classification head.

### 🔹 Generating Contextual Representations

```python
import torch
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

model = AutoModel.from_pretrained("bert-base-uncased")

text = "I love learning NLP."

inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

print(outputs.last_hidden_state.shape)
```

**Explanation:**

- `return_tensors="pt"` returns PyTorch tensors.
- `model(**inputs)` passes the tokenized input to BERT.
- `torch.no_grad()` disables gradient calculation during inference.
- `last_hidden_state` contains contextual representations for every input token.

For a batch containing one sequence, the output shape is:

```text
(batch_size, sequence_length, hidden_size)
```

For BERT Base, the hidden size is 768.

---

## 9️⃣ Advantages and Limitations of BERT

### ✅ Advantages

- 🧠 Understands text using bidirectional context.
- 📚 Learns useful language representations through pretraining.
- 🎯 Performs well on many text-understanding tasks.
- 🔄 Can be fine-tuned for different NLP applications.
- 🤗 Supported by the Hugging Face Transformers library.

### ⚠️ Limitations

- 🚫 The original BERT architecture is not designed for autoregressive text generation.
- 💻 Large BERT variants require significant computational resources.
- 📏 Original BERT supports a maximum sequence length of 512 tokens.
- 🔧 Fine-tuning requires task-specific data and suitable training configuration.
- 🧩 Its original pretraining objectives do not directly make it a conversational generative model.

---

## 🔟 Key Takeaways

- 🧠 BERT stands for Bidirectional Encoder Representations from Transformers.
- 🏗️ BERT uses the Encoder-only Transformer architecture.
- ↔️ It uses bidirectional self-attention to understand context from both directions.
- 🔤 It uses Token, Segment, and Position Embeddings.
- 🎭 Its original pretraining objectives are Masked Language Modeling and Next Sentence Prediction.
- 🔧 Pretrained BERT can be fine-tuned for specific NLP tasks.
- 🎯 It is mainly suitable for language understanding tasks such as classification, sentiment analysis, and named entity recognition.
- 🤗 Hugging Face Transformers provides `AutoTokenizer` and `AutoModel` for loading pretrained BERT checkpoints.
