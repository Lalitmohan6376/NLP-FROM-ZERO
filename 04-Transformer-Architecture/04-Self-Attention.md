# 🎯 Self-Attention Mechanism

## 1. What is Self-Attention?

Self-Attention is a mechanism used in Transformer models to understand relationships between different tokens in an input sequence.

It allows each token to look at other tokens and determine which ones are important for understanding its meaning.

Instead of processing every word independently, the model considers information from the surrounding words.

**Example:**

```text
The animal did not cross the road because it was tired.
```

To understand the word `"it"`, the model needs information about the other words in the sentence.

Self-Attention helps the model learn relationships between `"it"` and relevant tokens such as `"animal"`.

---

## 2. Why Do We Need Self-Attention?

Traditional sequence models such as RNNs and LSTMs process tokens sequentially.

They can face difficulties when learning relationships between words that are far apart in a sentence.

Self-Attention helps address this problem.

**Example:**

```text
The student who studied all night passed the examination.
```

To understand the relationship between `"student"` and `"passed"`, the model needs to capture information from different positions in the sentence.

Self-Attention allows tokens to directly exchange information with other relevant tokens.

### Benefits

- Captures relationships between distant tokens.
- Helps understand context.
- Allows parallel processing during training.
- Supports better contextual representations.
- Forms the foundation of Transformer attention layers.

---

## 3. How Does Self-Attention Work?

Self-Attention uses three important components:

1. Query (Q)
2. Key (K)
3. Value (V)

These three components are generated from the input token representations using learned weight matrices.

**Basic Workflow:**

```text
          Input Embeddings
                 |
                 ↓
          Linear Transformations
                 |
          ┌──────┼──────┐
          ↓      ↓      ↓
        Query   Key    Value
          |      |      |
          └──────┼──────┘
                 |
                 ↓
        Attention Scores
                 |
                 ↓
          Softmax
                 |
                 ↓
       Attention Weights
                 |
                 ↓
       Weighted Sum of Values
                 |
                 ↓
        Output Representations
```

---

## 4. Query, Key, and Value

### A. Query (Q)

Query represents what a token is looking for from other tokens.

In simple terms, it helps determine which information is relevant to the current token.

### B. Key (K)

Key represents the information used to match against a Query.

The model compares Queries and Keys to calculate attention scores.

### C. Value (V)

Value contains the information that will be combined using the calculated attention weights.

**Simple Example:**

```text
Sentence:
The cat is drinking milk.

Query:
What information should this token look for?

Key:
How relevant is this token to another token?

Value:
What information should be passed forward?
```

Queries, Keys, and Values are numerical vectors, not ordinary text.

---

## 5. Step-by-Step Self-Attention Calculation

Let's understand how Self-Attention calculates relationships between tokens.

Consider the sentence:

```text
The cat is drinking milk.
```

### Step 1: Input Embeddings

Each token is converted into a numerical vector.

```text
The      → [Numerical Vector]
cat      → [Numerical Vector]
is       → [Numerical Vector]
drinking → [Numerical Vector]
milk     → [Numerical Vector]
```

### Step 2: Generate Query, Key, and Value

The input embeddings are multiplied by three learned weight matrices.

```text
Q = X × WQ

K = X × WK

V = X × WV
```

Where:

- `X` represents input embeddings.
- `WQ` represents Query weight matrix.
- `WK` represents Key weight matrix.
- `WV` represents Value weight matrix.

### Step 3: Calculate Attention Scores

The model compares Query and Key vectors using the dot product.

Higher scores indicate stronger compatibility between a Query and a Key.

### Step 4: Scale Attention Scores

The scores are divided by the square root of the Key dimension.

This helps prevent excessively large values from making the Softmax distribution too concentrated.

### Step 5: Apply Softmax

Softmax converts the scaled scores into attention weights.

These weights determine how much information should be taken from each token.

### Step 6: Calculate Weighted Sum

The attention weights are multiplied by the Value vectors.

The resulting weighted sum produces updated token representations.

---

## 6. Scaled Dot-Product Attention

Scaled Dot-Product Attention is the mathematical operation used in Transformer attention.

Its formula is:

\[
\text{Attention}(Q,K,V)
=
\text{softmax}\left(
\frac{QK^T}{\sqrt{d_k}}
\right)V
\]

Where:

- `Q` = Query matrix
- `K` = Key matrix
- `V` = Value matrix
- `Kᵀ` = Transpose of Key matrix
- `dₖ` = Dimension of Key vectors
- `√dₖ` = Scaling factor
- `Softmax` = Converts scores into attention weights

**Understanding the Formula:**

1. `QKᵀ` calculates similarity scores between Queries and Keys.
2. Division by `√dₖ` scales the scores.
3. Softmax converts scores into attention weights.
4. Multiplication by `V` generates the final weighted representations.

---

## 7. Attention Weights

Attention Weights indicate how much attention one token gives to other tokens.

Consider an illustrative attention distribution for the token `"drinking"`:

| Token | Attention Weight |
|---|---:|
| The | 0.05 |
| cat | 0.35 |
| is | 0.10 |
| drinking | 0.15 |
| milk | 0.35 |

These values are illustrative, not actual model outputs.

The weights add up to 1.

A higher attention weight means that the corresponding Value contributes more to the updated representation.

---

## 8. Self-Attention vs Traditional Sequence Processing

| Feature | RNN / LSTM | Self-Attention |
|---|---|---|
| Processing | Sequential | Parallelizable |
| Token Relationships | Through recurrent processing | Direct attention between tokens |
| Long-Range Dependencies | Can be difficult | Easier to model |
| Context Understanding | Through hidden states | Through attention weights |
| Computation | Recurrent operations | Attention matrix operations |

Self-Attention is powerful, but it also has a limitation: standard full Self-Attention has quadratic computational and memory complexity with respect to sequence length.

---

## 9. Applications of Self-Attention

Self-Attention is used in many Transformer-based NLP applications:

- Text Classification
- Sentiment Analysis
- Machine Translation
- Text Summarization
- Question Answering
- Text Generation
- Chatbots
- Semantic Understanding

---

## 10. Key Takeaways

- Self-Attention helps Transformer models understand relationships between tokens.
- It uses Query, Key, and Value vectors.
- Queries and Keys are compared to calculate attention scores.
- Softmax converts attention scores into attention weights.
- Attention weights determine how Values are combined.
- Scaled Dot-Product Attention is the core mathematical operation.
- Self-Attention allows parallelizable processing and captures long-range relationships.
- It is a fundamental component of Transformer architecture.
