# 🔢 Token IDs in NLP

## 1. Introduction

**Token IDs** are numerical representations assigned to tokens by a tokenizer.

NLP models cannot directly process text words as input. They require numerical values.

Therefore, after tokenization, each token is mapped to a unique numerical ID using the tokenizer's vocabulary.

**Example:**

Input Text:

`I love NLP`

Tokens:

`["I", "love", "NLP"]`

Token IDs:

`[101, 2293, 17953]`

*Note: These IDs are illustrative. Actual IDs depend on the tokenizer and its vocabulary.*

## 2. Why Do We Need Token IDs?

Token IDs convert text into numerical values that can be processed by neural network models.

Their importance includes:

- Converting tokens into numerical representations.
- Providing input to Transformer models.
- Mapping tokens to their corresponding vocabulary entries.
- Helping models retrieve token embeddings.
- Making text suitable for mathematical computation.

Without numerical representation, Transformer models cannot process text in their expected input format.

## 3. How Do Token IDs Work?

A tokenizer maintains a vocabulary containing tokens and their corresponding numerical IDs.

Each token is assigned an ID.

For example, consider this illustrative vocabulary:

| Token | Token ID |
|---|---:|
| I | 101 |
| love | 2293 |
| NLP | 17953 |
| learning | 4083 |
| computer | 6251 |

When a tokenizer receives text, it performs the following steps:

1. Receives the input text.
2. Divides the text into tokens.
3. Searches for each token in its vocabulary.
4. Assigns the corresponding numerical ID.
5. Returns a sequence of token IDs.

**Example:**

Input:

`I love NLP`

Tokens:

`["I", "love", "NLP"]`

Token IDs:

`[101, 2293, 17953]`

## 4. Token IDs and Vocabulary

A vocabulary is a collection of tokens supported by a tokenizer.

Each token has its own numerical ID.

For example:

```text
Vocabulary:

"I"        → 101
"love"     → 2293
"NLP"      → 17953
"learning" → 4083
```

The tokenizer uses this vocabulary to convert text into numerical IDs.

Different pretrained models can have different vocabularies and token IDs.

Therefore, the same word may have different token IDs depending on the tokenizer.

## 5. Token IDs in Transformer Models

Transformer models receive token IDs as numerical input.

These IDs are passed through an embedding layer, which converts them into dense numerical vectors called embeddings.

A simplified representation is:

**Text → Tokens → Token IDs → Embeddings → Transformer Model**

For example:

```text
Input Text:
"I love NLP"

Tokens:
["I", "love", "NLP"]

Token IDs:
[101, 2293, 17953]

Embeddings:
Numerical vectors representing each token
```

The model processes these embeddings to perform tasks such as classification, translation, and text generation.

**Important:** Token IDs themselves are not embeddings. They are vocabulary indices used to retrieve the corresponding embedding vectors.

## 6. Token IDs Using Hugging Face Transformers

Hugging Face Transformers provides `AutoTokenizer` to load a pretrained tokenizer.

Example:

```python
from transformers import AutoTokenizer

# Load a pretrained tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Input text
text = "I love learning NLP."

# Convert text into token IDs
token_ids = tokenizer.encode(text)

# Display token IDs
print(token_ids)
```

The tokenizer converts the input text into numerical IDs.

These IDs can be used as input for the corresponding pretrained model.

## 7. Converting Token IDs Back into Text

Token IDs can also be converted back into their corresponding tokens and readable text.

Hugging Face provides the `decode()` method for this purpose.

Example:

```python
# Convert token IDs back into text
decoded_text = tokenizer.decode(token_ids)

print(decoded_text)
```

Output:

```text
i love learning nlp.
```

The decoded text may differ slightly in capitalization or formatting from the original input because of tokenizer-specific normalization.

## 8. Important Methods

| Method | Purpose |
|---|---|
| `tokenizer.tokenize()` | Converts text into tokens. |
| `tokenizer.convert_tokens_to_ids()` | Converts tokens into numerical IDs. |
| `tokenizer.encode()` | Converts text into token IDs, usually including special tokens by default. |
| `tokenizer.decode()` | Converts token IDs back into readable text. |
| `tokenizer.convert_ids_to_tokens()` | Converts token IDs back into tokens. |

## 9. Key Takeaways

- Token IDs are numerical representations of tokens.
- Each token is mapped to an ID using the tokenizer's vocabulary.
- Token IDs allow NLP models to process text numerically.
- Different tokenizers may assign different IDs to the same word.
- Token IDs are not embeddings.
- Embedding layers convert token IDs into dense numerical vectors.
- Hugging Face `AutoTokenizer` provides methods to encode and decode text.
