# 🤖 Introduction to Transformers

## 1. What are Transformers?

Transformers are a type of deep learning architecture used to process and understand sequential data, especially text.

They were introduced in the research paper **"Attention Is All You Need" (2017)** by researchers at Google.

Transformers use a mechanism called **Self-Attention** to understand relationships between different words or tokens in a sequence.

Unlike traditional sequence models such as RNNs and LSTMs, Transformers can process multiple tokens in parallel during training.

Today, Transformers are widely used in modern NLP applications.

---

## 2. Why Do We Need Transformers?

Before Transformers, NLP systems commonly used architectures such as:

- RNN (Recurrent Neural Network)
- LSTM (Long Short-Term Memory)
- GRU (Gated Recurrent Unit)

These models process sequential information step by step.

However, they have some limitations:

- **Sequential Processing:** RNN-based models process tokens one after another, which can make training slower.
- **Long-Term Dependencies:** They can struggle to retain information across long sequences.
- **Parallelization:** Their sequential nature limits parallel processing during training.
- **Context Understanding:** Capturing relationships between distant words can be difficult.

Transformers address many of these limitations through Self-Attention and parallel processing.

---

## 3. How Do Transformers Work?

Transformers process text through multiple stages.

**Basic Workflow:**

1. **Input Text:** Provide a sentence or sequence.
2. **Tokenization:** Convert text into tokens.
3. **Token IDs:** Convert tokens into numerical IDs.
4. **Embeddings:** Convert token IDs into numerical vectors.
5. **Positional Information:** Add information about token positions.
6. **Self-Attention:** Learn relationships between tokens.
7. **Feed-Forward Network:** Further process the token representations.
8. **Output:** Generate contextual representations or predictions depending on the model.

**Example:**

```text
Input:
The cat is drinking milk.

        ↓

Tokenization

        ↓

Token IDs

        ↓

Token Embeddings

        ↓

Positional Information

        ↓

Self-Attention

        ↓

Feed-Forward Network

        ↓

Output Representations
```

---

## 4. What is Self-Attention?

Self-Attention is one of the most important components of the Transformer architecture.

It allows the model to understand how different tokens in a sequence relate to one another.

For example:

```text
The animal did not cross the road because it was tired.
```

To understand the word `"it"`, the model can use information from other words in the sentence, especially `"animal"`.

Self-Attention helps the model learn which tokens are important when processing a particular token.

It uses three main components:

- **Query (Q):** Represents what a token is looking for.
- **Key (K):** Represents information that a token provides for matching.
- **Value (V):** Contains the information used to build the updated representation.

These components are used to calculate attention scores and combine information from relevant tokens.

---

## 5. Main Components of a Transformer

A Transformer contains several important components:

### A. Input Embeddings

Input token IDs are converted into numerical vectors.

These vectors provide the initial representation of each token.

### B. Positional Encoding

Transformers do not process tokens sequentially in the same way as RNNs.

Therefore, they need positional information to understand the order of tokens.

Positional information helps distinguish between sentences such as:

```text
The dog chased the cat.

The cat chased the dog.
```

### C. Self-Attention

Self-Attention allows each token to use information from other relevant tokens.

It helps the model capture relationships within a sequence.

### D. Feed-Forward Network

A Feed-Forward Network processes the representations produced by the attention layer.

It applies learned transformations to each token representation.

### E. Residual Connections and Layer Normalization

These components help stabilize the training of deep Transformer networks.

- Residual Connections provide shortcut paths for information.
- Layer Normalization helps normalize intermediate representations.

---

## 6. Encoder and Decoder

The original Transformer architecture consists of two main parts:

**1. Encoder**

- Processes the input sequence.
- Uses Self-Attention and Feed-Forward Networks.
- Produces contextual representations of input tokens.

**2. Decoder**

- Generates an output sequence.
- Uses masked Self-Attention.
- Uses encoder-decoder attention to access encoder representations in the original architecture.

The original Transformer uses both encoder and decoder components for sequence-to-sequence tasks such as machine translation.

Modern Transformer models may use only an encoder, only a decoder, or an encoder-decoder architecture.

---

## 7. Types of Transformer Architectures

Transformer-based models are commonly grouped into three categories.

### A. Encoder-Only Models

These models focus on understanding input text.

Examples:

- BERT
- RoBERTa
- DistilBERT
- ALBERT

Common applications:

- Sentiment Analysis
- Text Classification
- Named Entity Recognition
- Semantic Understanding

### B. Decoder-Only Models

These models generate text by predicting the next token based on previous tokens.

Examples:

- GPT
- LLaMA
- Qwen

Common applications:

- Text Generation
- Chatbots
- Conversational AI
- Code Generation

### C. Encoder-Decoder Models

These models use an encoder to process input and a decoder to generate output.

Examples:

- T5
- BART
- FLAN-T5

Common applications:

- Text Summarization
- Machine Translation
- Text Transformation
- Sequence-to-Sequence Tasks

---

## 8. Transformers vs RNN and LSTM

| Feature | RNN | LSTM | Transformer |
|---|---|---|---|
| Processing | Sequential | Sequential | Parallelizable during training |
| Long-Range Relationships | Difficult | Better than basic RNN | Self-Attention |
| Training Speed | Often slower | Often slower | Can be faster with suitable hardware |
| Parallel Processing | Limited | Limited | High |
| Main Mechanism | Recurrent Connections | Gates and Memory | Self-Attention |

Transformers are particularly effective for large-scale language modeling and modern NLP applications.

However, they can require substantial computational resources, especially when models become large.

---

## 9. Applications of Transformers

Transformers are used in many NLP applications:

- Text Classification
- Sentiment Analysis
- Named Entity Recognition
- Question Answering
- Text Summarization
- Machine Translation
- Semantic Search
- Text Generation
- Chatbots
- Information Extraction

They are also used beyond NLP in areas such as computer vision, speech processing, and multimodal AI.

---

## 10. Transformers in Modern NLP

Transformers form the foundation of many modern pretrained language models.

Some popular Transformer-based models include:

| Model | Architecture Type | Main Use |
|---|---|---|
| BERT | Encoder-Only | Text Understanding |
| GPT | Decoder-Only | Text Generation |
| T5 | Encoder-Decoder | Text-to-Text Tasks |
| BART | Encoder-Decoder | Text Generation and Summarization |
| RoBERTa | Encoder-Only | Language Understanding |
| DistilBERT | Encoder-Only | Lightweight NLP Applications |

These models are available through the Hugging Face Transformers ecosystem.

---

## 11. Key Takeaways

- Transformers are deep learning architectures widely used in modern NLP.
- They were introduced in the paper "Attention Is All You Need" in 2017.
- Self-Attention helps models understand relationships between tokens.
- Positional Information provides information about token order.
- Feed-Forward Networks further process token representations.
- The original Transformer contains both Encoder and Decoder components.
- Modern Transformer models can be Encoder-Only, Decoder-Only, or Encoder-Decoder.
- BERT, GPT, and T5 are popular Transformer-based models.
