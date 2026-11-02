# 🏷️ Special Tokens in NLP

## 1. Introduction

**Special Tokens** are predefined tokens used by NLP models to perform specific functions during text processing.

Unlike normal tokens, special tokens provide additional information about the structure, boundaries, and meaning of model inputs.

They help Transformer models identify where a sequence starts, where it ends, and how different parts of the input are organized.

**Example:**

```text
[CLS] I love NLP [SEP]
```

Here:
- `[CLS]` represents a classification token.
- `[SEP]` represents a separator token.

These tokens are commonly used by BERT-based models.

## 2. Why Do We Need Special Tokens?

Special tokens help models understand how input text is structured.

Their importance includes:

- Identifying the beginning of a sequence.
- Identifying the end of a sequence.
- Separating multiple text sequences.
- Representing missing or unknown tokens.
- Handling padding in batches.
- Supporting specific model tasks.

Without appropriate special tokens, models may not receive the input structure they were designed to process.

## 3. Common Special Tokens

Different Transformer models use different special tokens.

Some commonly used tokens are:

### 3.1 [CLS] — Classification Token

`[CLS]` is commonly used in BERT-based models.

It is generally added at the beginning of an input sequence.

Example:

```text
[CLS] I love Natural Language Processing [SEP]
```

In classification tasks, the model can use the final hidden representation of this token to make a prediction.

### 3.2 [SEP] — Separator Token

`[SEP]` is used by BERT to mark the end of a sequence or separate two input sequences.

Example:

```text
[CLS] I love NLP [SEP]
```

For a pair of sentences:

```text
[CLS] First sentence [SEP] Second sentence [SEP]
```

### 3.3 [PAD] — Padding Token

`[PAD]` is used to make sequences equal in length.

This is useful when multiple text sequences are processed together in a batch.

Example:

```text
Sentence 1: [101, 2023, 2003, 102]

Sentence 2: [101, 2023, 102, 0]
```

Here, `0` is an illustrative padding ID.

The actual padding token ID depends on the tokenizer.

### 3.4 [UNK] — Unknown Token

`[UNK]` represents an unknown token when the tokenizer cannot represent a piece of text using its vocabulary or tokenization rules.

Example:

```text
[CLS] I love [UNK] [SEP]
```

Subword tokenizers can often represent uncommon words without using an unknown token.

### 3.5 [MASK] — Mask Token

`[MASK]` is used in masked language modeling.

A word or token is hidden, and the model tries to predict the missing token.

Example:

```text
Input:
I love [MASK].

Prediction:
NLP
```

BERT uses this approach during its masked language modeling pretraining.

### 3.6 BOS — Beginning of Sequence

`BOS` represents the beginning of a sequence.

It helps certain models identify where an input sequence starts.

Some tokenizers use names such as `<bos>` for this token.

### 3.7 EOS — End of Sequence

`EOS` represents the end of a sequence.

It helps models identify when a sequence or generated response should stop.

Some tokenizers use names such as `<eos>` for this token.

## 4. Special Tokens in Different Models

Not every Transformer model uses the same special tokens.

For example:

| Special Token | Common Purpose | Example Model |
|---|---|---|
| `[CLS]` | Classification representation | BERT |
| `[SEP]` | Sequence separation | BERT |
| `[PAD]` | Padding | BERT, GPT-2 |
| `[UNK]` | Unknown token | BERT |
| `[MASK]` | Masked language modeling | BERT |
| `<bos>` | Beginning of sequence | Some generative models |
| `<eos>` | End of sequence | GPT and other generative models |

The exact tokens and their behavior depend on the selected model and tokenizer.

## 5. Special Tokens Using Hugging Face Transformers

Hugging Face provides `AutoTokenizer` to load a pretrained tokenizer and inspect its special tokens.

Example:

```python
from transformers import AutoTokenizer

# Load a pretrained BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Display special tokens
print("Special Tokens:", tokenizer.special_tokens_map)

# Display special token IDs
print("Special Token IDs:", tokenizer.all_special_ids)

# Display the classification token
print("CLS Token:", tokenizer.cls_token)

# Display the separator token
print("SEP Token:", tokenizer.sep_token)

# Display the padding token
print("PAD Token:", tokenizer.pad_token)

# Display the unknown token
print("UNK Token:", tokenizer.unk_token)

# Display the mask token
print("MASK Token:", tokenizer.mask_token)
```

## 6. Adding Special Tokens to Input Text

When we tokenize text using a pretrained tokenizer, special tokens can be added automatically.

Example:

```python
from transformers import AutoTokenizer

# Load BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Input text
text = "I love NLP."

# Convert text into tokens
tokens = tokenizer.tokenize(text)

# Add special tokens
input_ids = tokenizer.encode(text, add_special_tokens=True)

# Display results
print("Tokens:", tokens)
print("Input IDs:", input_ids)

# Convert IDs back into tokens
print("Tokens with Special Tokens:",
      tokenizer.convert_ids_to_tokens(input_ids))
```

For BERT, the resulting token sequence generally includes `[CLS]` at the beginning and `[SEP]` at the end.

## 7. Important Difference: Normal Tokens vs Special Tokens

| Normal Tokens | Special Tokens |
|---|---|
| Represent ordinary text. | Perform predefined structural or task-related functions. |
| Example: `hello`, `world`. | Example: `[CLS]`, `[SEP]`, `[MASK]`. |
| Represent parts of the input text. | Provide additional information to the model. |

## 8. Key Takeaways

- Special tokens are predefined tokens with specific functions.
- `[CLS]` is commonly used for classification in BERT.
- `[SEP]` separates input sequences.
- `[PAD]` makes sequences equal in length.
- `[UNK]` represents unknown tokens.
- `[MASK]` is used in masked language modeling.
- `BOS` and `EOS` indicate sequence boundaries.
- Different pretrained models can use different special tokens.
- Hugging Face `AutoTokenizer` can automatically handle model-specific special tokens.
