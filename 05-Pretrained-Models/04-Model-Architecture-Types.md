# 🏗️ Model Architecture Types

## 📌 Introduction

Pretrained language models are built using different neural network architectures. Each architecture processes text differently and is designed for particular NLP tasks.

The three major Transformer architecture types are:

1. **Encoder-Only Models**
2. **Decoder-Only Models**
3. **Encoder-Decoder Models**

Understanding these architectures helps us choose the right pretrained model for an NLP application.

---

## 1️⃣ Encoder-Only Models

Encoder-only models use only the **Encoder** part of the Transformer architecture.

They process the input text and generate contextual representations of its tokens.

### ⚙️ How They Work

- The model receives input text.
- The tokenizer converts text into token IDs.
- The encoder processes all input tokens using bidirectional self-attention.
- Each token can attend to other tokens on both its left and right sides.
- The model generates contextual representations.

**Example:**

```text
Input:  The movie was really good.

Encoder:
[The] [movie] [was] [really] [good]

Output:
Contextual representations of all tokens
```

Because encoder-only models can use information from both directions, they are useful for understanding the meaning of text.

### 🎯 Common Applications

- Text Classification
- Sentiment Analysis
- Named Entity Recognition (NER)
- Part-of-Speech Tagging
- Semantic Understanding
- Extractive Question Answering

### 🤖 Examples

| Model | Description |
|---|---|
| BERT | Bidirectional Encoder Representations from Transformers |
| RoBERTa | An optimized training approach based on BERT |
| DistilBERT | A smaller and faster version of BERT |

---

## 2️⃣ Decoder-Only Models

Decoder-only models use only the **Decoder** part of the Transformer architecture.

They are primarily designed for autoregressive text generation, where the model predicts the next token based on previously generated tokens.

### ⚙️ How They Work

- The model receives an initial text prompt.
- The tokenizer converts the prompt into token IDs.
- The decoder processes the tokens using causal self-attention.
- Each token can attend only to previous tokens and itself.
- The model predicts the next token.
- The predicted token is added to the sequence.
- This process continues until the generation stops.

**Example:**

```text
Input: I love

Step 1: I love NLP
Step 2: I love NLP because
Step 3: I love NLP because it
Step 4: I love NLP because it is interesting.
```

The model generates text one token at a time.

### 🎯 Common Applications

- Text Generation
- Conversational AI
- Chatbots
- Code Generation
- Text Completion
- Creative Writing
- Instruction Following

### 🤖 Examples

| Model | Description |
|---|---|
| GPT | Generative Pre-trained Transformer |
| LLaMA | Large Language Model Meta AI |
| Qwen | A family of language models developed by Alibaba |

---

## 3️⃣ Encoder-Decoder Models

Encoder-decoder models use both the **Encoder** and **Decoder** parts of the Transformer architecture.

The encoder understands the input text and creates contextual representations. The decoder uses these representations to generate an output sequence.

### ⚙️ How They Work

- The model receives an input sequence.
- The tokenizer converts the input into token IDs.
- The encoder processes the input using bidirectional self-attention.
- The encoder generates contextual representations.
- The decoder uses causal self-attention to process previously generated output tokens.
- Cross-attention allows the decoder to use information from the encoder's output.
- The decoder generates the output sequence token by token.

**Example: Machine Translation**

```text
Input (English):
I love learning NLP.

        |
        v

     Encoder
        |
        v

Contextual Representations
        |
        v

     Decoder
        |
        v

Output (French):
J'aime apprendre le TAL.
```

The encoder understands the source sentence, while the decoder generates the translated sentence.

### 🎯 Common Applications

- Machine Translation
- Text Summarization
- Text-to-Text Generation
- Paraphrase Generation
- Sequence-to-Sequence Tasks

### 🤖 Examples

| Model | Description |
|---|---|
| T5 | Text-to-Text Transfer Transformer |
| BART | Bidirectional and Auto-Regressive Transformers |
| Original Transformer | The encoder-decoder architecture introduced in the original Transformer paper |

---

## 4️⃣ Comparison of Transformer Architectures

The three architectures differ in how they process input text and produce outputs.

| Feature | Encoder-Only | Decoder-Only | Encoder-Decoder |
|---|---|---|---|
| Architecture | Encoder | Decoder | Both |
| Attention | Bidirectional | Causal | Encoder and decoder attention |
| Main Purpose | Text Understanding | Text Generation | Input-to-Output Generation |
| Input Processing | Entire input context | Previous tokens | Encoder processes input |
| Output | Contextual representations | Next-token predictions | Generated output sequence |
| Common Tasks | Classification, NER | Chatbots, Text Generation | Translation, Summarization |
| Examples | BERT, RoBERTa | GPT, LLaMA | T5, BART |

---

## 5️⃣ Understanding the Attention Differences

Attention is one of the main differences between these architectures.

### 🧠 Encoder-Only: Bidirectional Attention

Each token can attend to tokens on both its left and right sides.

```text
Input: The movie was good

The    <----> Movie
Movie  <----> Was
Was    <----> Good
```

This helps the model understand words using their surrounding context.

### 🔒 Decoder-Only: Causal Attention

Each token can attend only to previous tokens and itself.

```text
Token 1: The

Token 2: The, movie

Token 3: The, movie, was

Token 4: The, movie, was, good
```

This prevents the model from using future tokens while predicting the next token.

### 🔄 Encoder-Decoder: Multiple Attention Mechanisms

Encoder-decoder models combine different attention mechanisms:

- **Encoder Self-Attention:** Understands the input using bidirectional context.
- **Decoder Causal Self-Attention:** Processes previously generated output tokens.
- **Cross-Attention:** Allows the decoder to attend to the encoder's output representations.

These mechanisms help the decoder generate output based on the original input.

---

## 6️⃣ When to Use Which Architecture?

Choosing an architecture depends on the task.

| Requirement | Suitable Architecture |
|---|---|
| Sentiment Analysis | Encoder-Only |
| Text Classification | Encoder-Only |
| Named Entity Recognition | Encoder-Only |
| Text Generation | Decoder-Only |
| Chatbot Development | Decoder-Only |
| Code Generation | Decoder-Only |
| Machine Translation | Encoder-Decoder |
| Text Summarization | Encoder-Decoder |

These are common choices, not strict limitations. Some tasks can be solved using more than one architecture.

---

## 🎯 Key Takeaways

- 🧠 **Encoder-Only:** Mainly used to understand and represent input text.
- ✍️ **Decoder-Only:** Mainly used to generate text through next-token prediction.
- 🔄 **Encoder-Decoder:** Uses an encoder to understand input and a decoder to generate output.
- 🔍 Encoder-only models use bidirectional self-attention.
- 🔒 Decoder-only models use causal self-attention.
- 🔗 Encoder-decoder models use encoder self-attention, decoder causal self-attention, and cross-attention.
- 🚀 The best architecture depends on the NLP task and the model's training and capabilities.
