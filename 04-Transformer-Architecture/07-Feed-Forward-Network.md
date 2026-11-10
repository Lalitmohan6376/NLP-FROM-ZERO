# ⚙️ Feed-Forward Network (FFN)

## 📖 Introduction

A Feed-Forward Network (FFN) is an important component of the Transformer architecture.

It is responsible for processing and transforming the representations produced by the attention layer.

In a Transformer, the attention mechanism helps tokens gather information from other tokens. The Feed-Forward Network then applies additional transformations to each token representation independently.

A typical Transformer Feed-Forward Network consists of two linear layers with a non-linear activation function between them.

It helps the model learn complex patterns and meaningful features from the input representations.

---

## 🎯 Why Feed-Forward Network?

Self-attention allows tokens to exchange information with other tokens, but attention alone is not the complete transformation process.

The Feed-Forward Network adds a separate processing stage after attention.

Its main purposes are:

- 🧠 **Feature Transformation:** Transforms token representations into more useful features.
- 🔍 **Pattern Learning:** Helps the model learn complex patterns in the input.
- ⚡ **Non-Linearity:** Uses activation functions to learn non-linear relationships.
- 🔄 **Representation Refinement:** Further processes the information produced by attention.
- 🎯 **Independent Processing:** Applies the same network separately to each token position.

---

## ⚙️ How Feed-Forward Network Works

A standard Transformer Feed-Forward Network contains two linear transformations and an activation function.

The process involves the following steps:

### 1. 📥 Receive Attention Output

The Feed-Forward Network receives the output of the Multi-Head Attention sublayer.

This output contains contextual token representations.

For example:

```text
Token 1 → [0.2, 0.5, 0.1, 0.8]
Token 2 → [0.4, 0.3, 0.7, 0.2]
Token 3 → [0.6, 0.1, 0.9, 0.5]
```

Each row represents one token.

### 2. 📈 First Linear Transformation

The input representation passes through the first linear layer.

This layer usually increases the dimensionality of the representation.

For example:

```text
Input Dimension:  768
Hidden Dimension: 3072
```

The transformation is:

\[
H = XW_1 + b_1
\]

Where:

- \(X\) = Input representation
- \(W_1\) = First weight matrix
- \(b_1\) = First bias
- \(H\) = Intermediate representation

### 3. ⚡ Apply Activation Function

The intermediate representation passes through a non-linear activation function.

The original Transformer uses ReLU.

\[
ReLU(x) = max(0,x)
\]

ReLU replaces negative values with zero while keeping positive values unchanged.

Modern Transformer architectures may use other activation functions, such as GELU or SwiGLU.

### 4. 🔄 Second Linear Transformation

After the activation function, the representation passes through the second linear layer.

This layer usually reduces the dimensionality back to the original model dimension.

For example:

```text
Hidden Dimension: 3072
Output Dimension: 768
```

The transformation is:

\[
Output = HW_2 + b_2
\]

Where:

- \(H\) = Activated intermediate representation
- \(W_2\) = Second weight matrix
- \(b_2\) = Second bias

### 5. 📤 Produce Final Output

The Feed-Forward Network produces transformed token representations.

These outputs are passed to the next part of the Transformer layer.

---

## 📐 Feed-Forward Network Formula

The complete Feed-Forward Network operation is:

\[
FFN(X) = max(0, XW_1+b_1)W_2+b_2
\]

This formula represents the original Transformer Feed-Forward Network using ReLU activation.

Where:

- \(X\) = Input representation
- \(W_1\) = First linear layer weights
- \(b_1\) = First linear layer bias
- \(W_2\) = Second linear layer weights
- \(b_2\) = Second linear layer bias
- \(max(0,x)\) = ReLU activation function

---

## 🔍 Important Characteristics

### 1. 🧩 Same Network for Every Token

The same Feed-Forward Network is applied independently to every token position.

For example, if an input contains 10 tokens, the same FFN processes all 10 token representations.

The network does not directly mix information between different token positions.

### 2. 🧠 Position-Wise Processing

The Feed-Forward Network is also called a **Position-Wise Feed-Forward Network** because it processes each position separately using the same weights.

### 3. ⚙️ Non-Linear Transformation

The activation function introduces non-linearity into the network.

Without a non-linear activation function, two consecutive linear transformations would be equivalent to a single linear transformation.

### 4. 📈 Hidden Dimension

The intermediate hidden dimension is often larger than the model's hidden dimension.

For example, the original Transformer uses:

- Model Dimension = 512
- FFN Hidden Dimension = 2048

BERT Base uses:

- Hidden Dimension = 768
- Intermediate Dimension = 3072

---

## ⚖️ Attention vs Feed-Forward Network

| Attention Mechanism | Feed-Forward Network |
|---|---|
| Allows tokens to exchange information. | Processes each token representation independently. |
| Captures relationships between tokens. | Transforms token features. |
| Uses Query, Key, and Value. | Uses linear layers and activation functions. |
| Combines information across sequence positions. | Applies the same transformation at each position. |

Both components perform different but complementary roles in a Transformer layer.

---

## 🏗️ Feed-Forward Network in a Transformer Layer

In the original Transformer encoder layer, the Feed-Forward Network comes after the Multi-Head Attention sublayer.

The simplified flow is:

```text
Input Representations
        |
        ▼
Multi-Head Self-Attention
        |
        ▼
Add & Layer Normalization
        |
        ▼
Feed-Forward Network
        |
        ▼
Add & Layer Normalization
        |
        ▼
Output Representations
```

The residual connections and Layer Normalization help stabilize the training process.

---

## 🌍 Practical Applications

Feed-Forward Networks contribute to the learning process in Transformer-based NLP models.

- 📝 **Text Classification:** Helps transform contextual representations for classification.
- 😊 **Sentiment Analysis:** Helps learn features useful for identifying sentiment.
- 🌐 **Machine Translation:** Processes representations used to generate translated text.
- 📄 **Text Summarization:** Helps refine representations used for generating summaries.
- ❓ **Question Answering:** Helps process contextual features used to predict answers.

---

## 💡 Key Takeaways

- ⚙️ Feed-Forward Network is an important component of Transformer architecture.
- 🧠 It transforms token representations produced by the attention sublayer.
- 🔄 It usually contains two linear layers and an activation function.
- ⚡ The original Transformer uses ReLU activation.
- 🎯 The same FFN is applied independently to every token position.
- 📈 The intermediate hidden dimension is generally larger than the model dimension.
- 🔗 Attention mixes information across tokens, while FFN transforms each token's features independently.
