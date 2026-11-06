# 🏗️ Transformer Architecture

## 1. What is Transformer Architecture?

Transformer Architecture is a deep learning architecture designed to process sequential data, especially text.

It uses Self-Attention, Feed-Forward Networks, Positional Information, and other components to process input sequences and learn relationships between tokens.

The original Transformer architecture was introduced in the 2017 research paper **"Attention Is All You Need"**.

It consists of two major components:

- **Encoder:** Processes the input sequence and generates contextual representations.
- **Decoder:** Uses encoder information and previously generated tokens to produce an output sequence.

**Basic Architecture:**

```text
             INPUT TEXT
                  |
                  ↓
             Tokenization
                  |
                  ↓
            Token Embeddings
                  |
                  ↓
          Positional Encoding
                  |
                  ↓
          ┌───────────────┐
          │    ENCODER    │
          │               │
          │ Self-Attention│
          │       ↓       │
          │ Feed-Forward  │
          └───────┬───────┘
                  |
                  ↓
          ┌───────────────┐
          │    DECODER    │
          │               │
          │ Masked Self-  │
          │ Attention     │
          │       ↓       │
          │ Encoder-      │
          │ Decoder       │
          │ Attention     │
          │       ↓       │
          │ Feed-Forward  │
          └───────┬───────┘
                  |
                  ↓
             Linear Layer
                  |
                  ↓
              Softmax
                  |
                  ↓
             OUTPUT TEXT
```

This represents the original encoder-decoder Transformer used for sequence-to-sequence tasks.

---

## 2. Input Embeddings

The first major step is converting input tokens into numerical vectors.

Neural networks cannot directly process ordinary text. Therefore, text must first be tokenized and converted into token IDs.

These token IDs are then passed through an embedding layer.

**Example:**

```text
Input:
The cat is sleeping.

       ↓

Tokens:
[The, cat, is, sleeping]

       ↓

Token IDs:
[101, 1996, 4937, 2003, 7777, 102]

       ↓

Input Embeddings:
Numerical vectors for each token
```

The token IDs shown are illustrative.

Each token is represented by a dense numerical vector.

These vectors provide the initial numerical representation of the input sequence.

---

## 3. Positional Encoding

Transformers process tokens in parallel and do not inherently understand their sequence order.

Positional Encoding provides information about the position of each token.

**Example:**

```text
Sentence 1:
The dog chased the cat.

Sentence 2:
The cat chased the dog.
```

The words are similar, but their positions change the meaning of the sentences.

Positional information helps the model distinguish between these arrangements.

In the original Transformer, sinusoidal positional encodings are added to token embeddings.

The resulting vectors are passed to the encoder or decoder.

---

## 4. Encoder Architecture

The Encoder processes the input sequence and generates contextual representations.

The original Transformer encoder consists of multiple identical layers.

Each encoder layer contains two main sublayers:

### A. Multi-Head Self-Attention

- Examines relationships between tokens.
- Allows each token to attend to other tokens in the input sequence.
- Uses multiple attention heads to learn different relationships.

### B. Feed-Forward Network

- Processes the output of the attention sublayer.
- Applies learned transformations to each token representation.
- Helps the model learn more complex features.

Each sublayer also uses residual connections and layer normalization.

**Encoder Layer Structure:**

```text
       Input Embeddings
              |
              ↓
     Multi-Head Attention
              |
              ↓
    Add & Layer Normalization
              |
              ↓
      Feed-Forward Network
              |
              ↓
    Add & Layer Normalization
              |
              ↓
       Encoder Output
```

The encoder can contain multiple stacked layers.

Each layer further processes the token representations.

---

## 5. Decoder Architecture

The Decoder generates an output sequence using previously generated tokens and information from the encoder.

The original Transformer decoder contains three main sublayers:

### A. Masked Multi-Head Self-Attention

- Processes previously generated tokens.
- Prevents a position from accessing future target tokens.
- Supports autoregressive generation.

### B. Encoder-Decoder Attention

- Connects the decoder with the encoder output.
- Allows the decoder to use information from the input sequence.
- Helps generate output relevant to the original input.

### C. Feed-Forward Network

- Further processes the decoder representations.
- Applies learned transformations to each position.

Like the encoder, each decoder layer also uses residual connections and layer normalization.

**Decoder Layer Structure:**

```text
       Previous Output Tokens
                 |
                 ↓
        Masked Self-Attention
                 |
                 ↓
       Add & Layer Normalization
                 |
                 ↓
      Encoder-Decoder Attention
                 |
                 ↓
       Add & Layer Normalization
                 |
                 ↓
         Feed-Forward Network
                 |
                 ↓
       Add & Layer Normalization
                 |
                 ↓
          Decoder Output
```

The decoder can also contain multiple stacked layers.

---

## 6. Add and Layer Normalization

Residual Connections and Layer Normalization are important components of the original Transformer architecture.

### A. Residual Connections

A residual connection adds the input of a sublayer to its output.

It creates a shortcut path that helps information and gradients flow through deep networks.

**Basic Representation:**

```text
Input
  |
  ├───────────────┐
  ↓               |
Sublayer          |
  |               |
  ↓               |
Output            |
  |               |
  └───────+───────┘
          |
          ↓
    Final Output
```

### B. Layer Normalization

Layer Normalization normalizes the features within a token representation.

It helps stabilize training and makes optimization easier.

In the original Transformer, residual addition and layer normalization are applied around each sublayer.

---

## 7. Linear Layer and Softmax

After the final decoder layer, the output is passed through a Linear Layer and Softmax.

### A. Linear Layer

The Linear Layer transforms the decoder output into scores for every token in the vocabulary.

These scores are called logits.

### B. Softmax

Softmax converts logits into probability values.

These probabilities represent the model's predicted distribution over the vocabulary.

**Example:**

```text
Input Context:
The cat is

        ↓

Linear Layer

        ↓

Softmax

        ↓

Predicted Probabilities:

sleeping  → 0.65
playing   → 0.20
eating    → 0.10
running   → 0.05
```

The values are illustrative.

The model can select a token based on its generation strategy and continue generating the sequence.

---

## 8. Complete Transformer Workflow

Let's understand how the original Transformer processes an input and generates an output.

**Example: Machine Translation**

```text
Input:
I love programming.

        ↓

Tokenization

        ↓

Token IDs

        ↓

Input Embeddings

        ↓

Positional Encoding

        ↓

Encoder

        ↓

Contextual Representations

        ↓

Decoder
        ↑
Previous Output Tokens

        ↓

Linear Layer

        ↓

Softmax

        ↓

Generated Output:
J'aime programmer.
```

The encoder processes the source sentence, while the decoder generates the translated sentence token by token.

---

## 9. Important Transformer Components

| Component | Purpose |
|---|---|
| Input Embeddings | Convert token IDs into vectors |
| Positional Encoding | Provide token position information |
| Self-Attention | Learn relationships between tokens |
| Multi-Head Attention | Learn different attention relationships |
| Feed-Forward Network | Further process token representations |
| Residual Connections | Provide shortcut information paths |
| Layer Normalization | Normalize intermediate representations |
| Linear Layer | Convert decoder representations into vocabulary scores |
| Softmax | Convert scores into probabilities |

---

## 10. Key Takeaways

- The original Transformer architecture contains an Encoder and a Decoder.
- Input Embeddings convert token IDs into numerical vectors.
- Positional Encoding provides information about token order.
- The Encoder processes input sequences using Self-Attention and Feed-Forward Networks.
- The Decoder generates output sequences using masked Self-Attention and Encoder-Decoder Attention.
- Residual Connections and Layer Normalization support stable training.
- Linear and Softmax layers produce vocabulary probability distributions.
- Modern Transformer models may use encoder-only, decoder-only, or encoder-decoder architectures.
