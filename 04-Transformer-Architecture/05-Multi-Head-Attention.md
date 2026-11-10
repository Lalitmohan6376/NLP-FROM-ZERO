# 🧠 Multi-Head Attention

## 📖 Introduction

Multi-Head Attention is an important component of the Transformer architecture. It allows a model to focus on different parts of an input sequence simultaneously.

Instead of calculating attention only once, Multi-Head Attention performs multiple attention operations called **Attention Heads**.

Each attention head can learn different relationships between tokens and capture different aspects of the input.

For example, consider the sentence:

> "The animal didn't cross the road because it was tired."

To understand the word "it", the model needs to identify its relationship with "animal".

Different attention heads can learn different relationships between words, helping the model build richer contextual representations.

---

## 🎯 Why Multi-Head Attention?

A single attention operation can capture relationships between tokens, but it may not capture all types of relationships effectively.

Multi-Head Attention solves this by using multiple attention heads.

Its main advantages are:

- 🔍 **Multiple Perspectives:** Focuses on different relationships between tokens.
- 🧩 **Better Context Understanding:** Captures different aspects of the input sequence.
- 🔗 **Relationship Learning:** Helps identify connections between words in a sentence.
- 🚀 **Parallel Processing:** Multiple attention heads can be computed simultaneously.
- 🧠 **Richer Representations:** Combines information from multiple attention heads.

---

## ⚙️ How Multi-Head Attention Works

Multi-Head Attention uses multiple Query, Key, and Value projections.

Each attention head independently calculates attention using its own learned projection matrices.

The process involves the following steps:

### 1. 🔤 Input Representation

The Transformer receives input token representations.

Each token is represented as a numerical vector.

These representations are passed to the Multi-Head Attention layer.

### 2. 🔀 Linear Projections

The input representations are transformed into three different matrices:

- 🔎 **Query (Q):** Represents what a token is looking for.
- 🔑 **Key (K):** Represents what information a token provides.
- 📦 **Value (V):** Contains the information that will be combined.

Each attention head has its own learned projection matrices for generating Query, Key, and Value.

### 3. 🎯 Calculate Attention for Each Head

Each attention head independently calculates attention scores.

The scaled dot-product attention formula is:

\[
Attention(Q,K,V) =
softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

Here:

- \(Q\) = Query matrix
- \(K\) = Key matrix
- \(V\) = Value matrix
- \(d_k\) = Dimension of each Key vector

Each head learns to focus on different relationships between tokens.

### 4. 🧩 Concatenate Attention Heads

After calculating attention, the outputs from all heads are combined.

This operation is called **Concatenation**.

For example, if there are four attention heads, their outputs are joined together into a single representation.

### 5. ⚙️ Final Linear Projection

The concatenated output is passed through a final linear transformation.

This combines information learned by different attention heads into the final output representation.

---

## 📐 Multi-Head Attention Formula

The complete Multi-Head Attention operation is represented as:

\[
MultiHead(Q,K,V) =
Concat(head_1, head_2, \ldots, head_h)W^O
\]

Each attention head is calculated as:

\[
head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)
\]

Where:

- \(h\) = Number of attention heads
- \(W_i^Q\) = Query projection matrix for head \(i\)
- \(W_i^K\) = Key projection matrix for head \(i\)
- \(W_i^V\) = Value projection matrix for head \(i\)
- \(W^O\) = Final output projection matrix
- \(Concat\) = Concatenation of all attention head outputs

---

## 🔍 Single-Head vs Multi-Head Attention

| Single-Head Attention | Multi-Head Attention |
|---|---|
| Uses one attention head. | Uses multiple attention heads. |
| Learns relationships through one attention operation. | Learns different relationships through multiple attention operations. |
| Produces one attention output. | Combines outputs from multiple heads. |
| Has a single attention perspective. | Provides multiple attention perspectives. |

---

## 🏗️ Example: Multi-Head Attention in BERT

BERT Base uses 12 attention heads in each Transformer encoder layer.

Its hidden size is 768.

Therefore, each attention head operates on a dimension of:

\[
\frac{768}{12} = 64
\]

This means:

- 🧠 Hidden Size = 768
- 🔢 Number of Attention Heads = 12
- 📏 Dimension per Head = 64

Each head processes a different learned projection of the input representations.

The outputs of all 12 heads are concatenated and passed through the output projection.

---

## 🔄 Multi-Head Attention Workflow

The overall workflow can be summarized as:

1. 📥 Receive input token representations.
2. 🔀 Generate Query, Key, and Value projections for each head.
3. 🎯 Calculate scaled dot-product attention independently for each head.
4. 🧩 Concatenate all attention head outputs.
5. ⚙️ Apply the final linear projection.
6. 📤 Produce the final attention output.

---

## 🌍 Practical Applications

Multi-Head Attention is used in Transformer-based models for several NLP applications:

- 📝 **Text Understanding:** Captures relationships between words in a sentence.
- 🌐 **Machine Translation:** Helps models understand relationships between source and target tokens.
- ❓ **Question Answering:** Helps identify relevant information in a context.
- 📄 **Text Summarization:** Helps capture important relationships across a document.
- ✍️ **Text Generation:** Helps models use contextual information while predicting the next token.

---

## 💡 Key Takeaways

- 🧠 Multi-Head Attention is a core component of the Transformer architecture.
- 🔍 It uses multiple attention heads to learn different token relationships.
- 🔀 Each head has its own Query, Key, and Value projections.
- 🧩 Outputs from all heads are concatenated.
- ⚙️ A final linear projection combines the information from all heads.
- 🤖 BERT Base uses 12 attention heads in each Transformer encoder layer.
