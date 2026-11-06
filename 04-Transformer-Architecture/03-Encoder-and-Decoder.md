# 🔄 Encoder and Decoder

## 1. What are Encoder and Decoder?

Encoder and Decoder are two major components of the original Transformer architecture.

They perform different roles when processing sequences.

- **Encoder:** Reads and processes the input sequence to generate contextual representations.
- **Decoder:** Uses the encoder's information and previously generated tokens to produce an output sequence.

Together, they allow Transformer models to perform sequence-to-sequence tasks such as machine translation and text summarization.

**Basic Architecture:**

```text
          INPUT SEQUENCE
                |
                ↓
             ENCODER
                |
                ↓
      Contextual Representations
                |
                ↓
             DECODER
                |
                ↓
          OUTPUT SEQUENCE
```

---

## 2. What is an Encoder?

An Encoder is the component responsible for understanding and processing the input sequence.

It converts input tokens into contextual representations that capture information about the relationships between tokens.

### How Does an Encoder Work?

1. Receives input token IDs.
2. Converts token IDs into embeddings.
3. Adds positional information.
4. Processes tokens through Self-Attention.
5. Applies Feed-Forward Networks.
6. Produces contextual representations.

**Encoder Workflow:**

```text
       Input Text
           |
           ↓
       Tokenization
           |
           ↓
        Token IDs
           |
           ↓
     Input Embeddings
           |
           ↓
    Positional Information
           |
           ↓
     Self-Attention
           |
           ↓
    Feed-Forward Network
           |
           ↓
    Contextual Representations
```

### Important Features of Encoder

- Processes the complete input sequence.
- Uses bidirectional Self-Attention in the original Transformer encoder.
- Captures relationships between tokens.
- Generates contextual representations.
- Does not generate output text autoregressively.

### Examples of Encoder-Based Models

- BERT
- RoBERTa
- DistilBERT
- ALBERT

### Applications

- Sentiment Analysis
- Text Classification
- Named Entity Recognition
- Semantic Understanding
- Text Representation

---

## 3. What is a Decoder?

A Decoder is the component responsible for generating an output sequence.

In the original Transformer, it uses previously generated tokens and information from the encoder to generate the next output token.

### How Does a Decoder Work?

1. Receives previously generated output tokens.
2. Converts tokens into embeddings.
3. Adds positional information.
4. Applies Masked Self-Attention.
5. Uses Encoder-Decoder Attention to access encoder representations.
6. Processes information through a Feed-Forward Network.
7. Generates vocabulary scores.
8. Predicts the next output token.

**Decoder Workflow:**

```text
     Previous Output Tokens
                |
                ↓
         Token Embeddings
                |
                ↓
      Positional Information
                |
                ↓
      Masked Self-Attention
                |
                ↓
     Encoder-Decoder Attention
                ↑
                |
       Encoder Representations
                |
                ↓
      Feed-Forward Network
                |
                ↓
           Linear Layer
                |
                ↓
             Softmax
                |
                ↓
        Next Token Prediction
```

### Important Features of Decoder

- Generates output sequences.
- Uses Masked Self-Attention in the original Transformer decoder.
- Can access encoder information through Encoder-Decoder Attention.
- Predicts output tokens one at a time.
- Uses previous output tokens to generate subsequent tokens.

### Examples of Decoder-Based Models

- GPT
- LLaMA
- Qwen

These are decoder-only models. They do not use a separate encoder.

### Applications

- Text Generation
- Chatbots
- Conversational AI
- Code Generation
- Language Modeling

---

## 4. Encoder vs Decoder

| Feature | Encoder | Decoder |
|---|---|---|
| Main Purpose | Understand input | Generate output |
| Input | Source sequence | Previous output tokens |
| Attention | Self-Attention | Masked Self-Attention |
| Encoder-Decoder Attention | No | Yes, in original architecture |
| Output | Contextual representations | Output token predictions |
| Common Models | BERT, RoBERTa | GPT, LLaMA, Qwen |
| Common Tasks | Classification, NER | Text Generation, Chatbots |

**Important:** GPT is decoder-only, while BERT is encoder-only. The original Transformer uses both components.

---

## 5. How Encoder and Decoder Work Together

Let's understand their interaction using Machine Translation.

**Example:**

Translate English into French.

```text
Input:
I love programming.

             |
             ↓
          ENCODER
             |
             ↓
    Contextual Representations
             |
             ↓
          DECODER
             |
             ↓
     Generated Tokens
             |
             ↓
Output:
J'aime programmer.
```

### Step-by-Step Process

**Step 1: Input Processing**

The encoder receives the English sentence and converts it into contextual representations.

**Step 2: Information Transfer**

The encoder sends its output representations to the decoder.

**Step 3: First Token Generation**

The decoder starts with a special start token and predicts the first output token.

**Step 4: Next Token Generation**

The decoder uses previously generated tokens and encoder information to predict the next token.

**Step 5: Sequence Completion**

The process continues until the decoder generates an end-of-sequence token or reaches its generation limit.

---

## 6. Types of Transformer Architectures

Based on how Encoder and Decoder components are used, Transformer models are divided into three main categories.

### A. Encoder-Only Architecture

Uses only the Encoder component.

**Examples:**
- BERT
- RoBERTa
- DistilBERT

**Main Purpose:** Understanding input text.

**Applications:**
- Sentiment Analysis
- Text Classification
- Named Entity Recognition

### B. Decoder-Only Architecture

Uses only the Decoder component.

**Examples:**
- GPT
- LLaMA
- Qwen

**Main Purpose:** Predicting the next token and generating text.

**Applications:**
- Text Generation
- Chatbots
- Conversational AI

Decoder-only models use causal (masked) Self-Attention and do not require a separate encoder.

### C. Encoder-Decoder Architecture

Uses both Encoder and Decoder components.

**Examples:**
- T5
- BART
- FLAN-T5

**Main Purpose:** Transforming an input sequence into an output sequence.

**Applications:**
- Machine Translation
- Text Summarization
- Text Transformation

---

## 7. Real-World Applications

| Architecture | Example Applications |
|---|---|
| Encoder-Only | Sentiment Analysis, NER, Classification |
| Decoder-Only | Chatbots, Text Generation, Code Generation |
| Encoder-Decoder | Translation, Summarization, Text Transformation |

---

## 8. Key Takeaways

- Encoder processes input sequences and generates contextual representations.
- Decoder generates output sequences using previous tokens.
- The original Transformer architecture contains both Encoder and Decoder.
- BERT is an example of an Encoder-only model.
- GPT is an example of a Decoder-only model.
- T5 and BART are examples of Encoder-Decoder models.
- Encoder-only models are commonly used for text understanding.
- Decoder-only models are commonly used for autoregressive text generation.
- Encoder-Decoder models are commonly used for sequence-to-sequence tasks.
