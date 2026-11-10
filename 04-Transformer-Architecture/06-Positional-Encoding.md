# 📍 Positional Encoding

## 📖 Introduction

Positional Encoding is an important component of the original Transformer architecture. It provides information about the position of each token in an input sequence.

Unlike traditional sequence models such as RNNs and LSTMs, the Transformer processes tokens in parallel rather than sequentially.

Because of this, the model does not automatically know the order of tokens.

Positional Encoding solves this problem by adding position information to token embeddings.

For example, consider these two sentences:

- **Sentence 1:** The dog chased the cat.
- **Sentence 2:** The cat chased the dog.

Both sentences contain the same words, but their meanings are different because the word order changes.

Positional Encoding helps the Transformer understand these differences.

---

## 🎯 Why Positional Encoding?

The Transformer uses self-attention to understand relationships between tokens.

However, self-attention alone does not provide information about the original positions of tokens.

Without positional information, the model cannot directly distinguish between different token orders.

Positional Encoding helps by:

- 🔢 **Preserving Word Order:** Provides information about the position of each token.
- 🧠 **Understanding Sequence Structure:** Helps the model understand how tokens are arranged.
- 🔗 **Capturing Position Relationships:** Provides information about the relative positions of tokens.
- ⚙️ **Supporting Self-Attention:** Adds positional information to token representations before attention operations.

---

## ⚙️ How Positional Encoding Works

Positional Encoding creates a positional vector for each position in the input sequence.

This vector is combined with the corresponding token embedding.

The process involves the following steps:

### 1. 🔤 Token Embeddings

First, the input text is tokenized and converted into token IDs.

Each token ID is then converted into a numerical embedding vector.

For example:

```text
Input:  "I love NLP"

Tokens: ["I", "love", "NLP"]

Token Embeddings:
I     → [0.2, 0.5, 0.1]
love  → [0.4, 0.3, 0.8]
NLP   → [0.6, 0.7, 0.2]
```

These embeddings represent the tokens.

However, they do not independently indicate the original position of each token.

### 2. 📍 Generate Positional Encodings

The Transformer generates a positional encoding for every position in the sequence.

Each position receives a different positional vector.

For example:

```text
Position 0 → [0.1, 0.2, 0.3]
Position 1 → [0.4, 0.5, 0.6]
Position 2 → [0.7, 0.8, 0.9]
```

These vectors contain information about token positions.

### 3. ➕ Add Positional Encoding to Token Embeddings

The positional encoding is added to the corresponding token embedding.

The operation is:

\[
Input\ Representation = Token\ Embedding + Positional\ Encoding
\]

For example:

```text
Token Embedding:       [0.2, 0.5, 0.1]
Positional Encoding:   [0.1, 0.2, 0.3]

Final Representation:  [0.3, 0.7, 0.4]
```

This operation is performed for every token in the sequence.

### 4. 📤 Pass to Transformer Layers

The resulting representations are passed to the Transformer layers.

Now, the model has both:

- 🧠 Information about the token itself.
- 📍 Information about its position in the sequence.

This helps the Transformer process the input while considering token order.

---

## 📐 Sinusoidal Positional Encoding

The original Transformer paper introduced sinusoidal positional encoding.

It uses sine and cosine functions to generate positional vectors.

The mathematical formulas are:

For even dimensions:

\[
PE(pos, 2i) =
\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right)
\]

For odd dimensions:

\[
PE(pos, 2i+1) =
\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)
\]

Where:

- \(pos\) = Position of the token in the sequence.
- \(i\) = Dimension index.
- \(d_{model}\) = Embedding dimension.
- \(PE\) = Positional Encoding.

### 🔍 Why Sine and Cosine?

Sine and cosine functions generate different values for different positions.

They create positional patterns that allow the model to learn information about token positions and relationships between positions.

Using different frequencies helps represent both short-range and long-range positional patterns.

---

## 🧩 Types of Positional Encoding

There are different approaches to providing positional information in Transformer models.

### 1. 📍 Absolute Positional Encoding

Absolute Positional Encoding represents the specific position of each token in a sequence.

For example:

```text
Token:       I      love     NLP
Position:    0       1        2
```

Each position receives its own positional representation.

The original Transformer uses sinusoidal absolute positional encoding.

### 2. 🔗 Relative Positional Encoding

Relative Positional Encoding represents the relative distance or position between tokens instead of relying only on their absolute positions.

For example:

```text
The cat is sleeping

The → cat = 1 position apart
The → is  = 2 positions apart
The → sleeping = 3 positions apart
```

It helps models understand how tokens are positioned relative to one another.

---

## ⚖️ Absolute vs Relative Positional Encoding

| Absolute Positional Encoding | Relative Positional Encoding |
|---|---|
| Represents the position of each token. | Represents relationships between token positions. |
| Provides absolute position information. | Provides relative position information. |
| Used in the original Transformer. | Used in architectures such as Transformer-XL and other modern Transformer variants. |
| Position information is associated with individual tokens. | Position information is incorporated into relationships between tokens. |

---

## 🏗️ Positional Encoding in Different Transformer Models

Different Transformer architectures handle positional information differently.

- 🧠 **Original Transformer:** Uses sinusoidal positional encoding.
- 🤖 **BERT:** Uses learned absolute positional embeddings.
- ✍️ **GPT-2:** Uses learned absolute positional embeddings.
- 🔗 **Transformer-XL:** Uses relative positional encoding.
- 🚀 **Modern LLMs:** Some models use techniques such as Rotary Position Embeddings (RoPE).

### 🌀 Rotary Position Embeddings (RoPE)

RoPE is a positional encoding technique used in several modern language models.

Instead of simply adding positional vectors to token embeddings, RoPE applies position-dependent rotations to Query and Key representations in the attention mechanism.

This allows attention scores to incorporate relative positional information.

---

## 🔄 Positional Encoding Workflow

The complete process can be summarized as:

1. 📥 Receive input tokens.
2. 🔢 Convert tokens into token IDs.
3. 🧠 Generate token embeddings.
4. 📍 Generate positional encodings.
5. ➕ Add positional encodings to token embeddings.
6. ⚙️ Pass the combined representations into Transformer layers.
7. 📤 Process tokens using self-attention and other Transformer components.

---

## 🌍 Practical Importance

Positional Encoding is important in many NLP applications:

- 📝 **Text Understanding:** Helps models understand word order.
- 🌐 **Machine Translation:** Preserves the order of words in sentences.
- 📄 **Text Summarization:** Helps models understand the structure of longer text.
- ❓ **Question Answering:** Helps identify the positions of relevant information.
- ✍️ **Text Generation:** Helps models process token positions while generating text.

---

## 💡 Key Takeaways

- 📍 Positional Encoding provides position information to Transformer models.
- 🧠 Self-attention alone does not represent the original sequence order.
- ➕ In the original Transformer, positional encodings are added to token embeddings.
- 📐 Sinusoidal encoding uses sine and cosine functions.
- 🔗 Positional encoding can be absolute or relative.
- 🤖 Different Transformer models use different positional information techniques.
- 🚀 RoPE is used by several modern language models.
