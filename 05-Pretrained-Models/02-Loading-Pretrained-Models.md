# 📥 Loading Pretrained Models

## 📖 Introduction

Loading a Pretrained Model means importing an already trained model into our Python environment so that we can use it for NLP tasks.

Instead of training a model from scratch, we can download an existing model checkpoint from the Hugging Face Model Hub and load it using the **Transformers** library.

Hugging Face provides two important classes for loading pretrained models:

- 🔤 **AutoTokenizer:** Loads the tokenizer associated with a pretrained model.
- 🧠 **AutoModel:** Loads the pretrained model architecture and its weights.

These classes make it easier to work with different pretrained models without manually specifying their architecture.

---

## 🎯 Why Load Pretrained Models?

Loading pretrained models allows us to reuse models that have already learned useful language representations.

Its main advantages are:

- ⏱️ **Save Training Time:** Avoid training a model from scratch.
- 🧠 **Reuse Learned Knowledge:** Use language representations learned during pretraining.
- 🔄 **Support Different Models:** Load BERT, RoBERTa, DistilBERT, and other compatible models.
- 🛠️ **Perform NLP Tasks:** Use pretrained models for text understanding and other applications.
- ⚙️ **Enable Fine-Tuning:** Further train an existing model on task-specific data.

---

## 📦 Required Library

We use the Hugging Face Transformers library to load pretrained models.

Install it using:

```bash
pip install transformers torch
```

- 🤗 `transformers` provides pretrained model and tokenizer classes.
- 🔥 `torch` provides the PyTorch backend for model execution.

---

## 🔤 1. Loading a Pretrained Tokenizer

A tokenizer converts input text into tokens and numerical token IDs that a model can process.

We use `AutoTokenizer` to load the tokenizer associated with a pretrained model.

### Example

```python
from transformers import AutoTokenizer

# Load pretrained tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Input text
text = "Transformers are powerful models."

# Tokenize text
tokens = tokenizer.tokenize(text)

# Convert tokens into IDs
token_ids = tokenizer.convert_tokens_to_ids(tokens)

# Display results
print("Tokens:")
print(tokens)

print("\nToken IDs:")
print(token_ids)
```

### 🔍 Explanation

- `AutoTokenizer.from_pretrained()` loads the tokenizer files.
- `tokenizer.tokenize()` splits the text into tokens.
- `convert_tokens_to_ids()` converts tokens into numerical IDs.

---

## 🧠 2. Loading a Pretrained Model

We use `AutoModel` to load the pretrained model architecture and its learned weights.

`AutoModel` loads a base model without adding a task-specific classification or generation head.

### Example

```python
from transformers import AutoModel

# Load pretrained model
model = AutoModel.from_pretrained("bert-base-uncased")

# Display model architecture
print(model)
```

### 🔍 Explanation

- `AutoModel.from_pretrained()` downloads or loads the model checkpoint.
- The model architecture is created according to its configuration.
- The pretrained weights are loaded into the model.
- `print(model)` displays the model architecture.

---

## 🔄 3. Loading Tokenizer and Model Together

In practical NLP applications, we generally need both the tokenizer and the model.

The tokenizer converts text into model inputs, while the model processes those inputs and produces representations.

### Example

```python
import torch
from transformers import AutoTokenizer, AutoModel

# Model checkpoint
model_name = "bert-base-uncased"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Input text
text = "Natural Language Processing is interesting."

# Convert text into model inputs
inputs = tokenizer(text, return_tensors="pt")

# Pass inputs through the model
with torch.no_grad():
    outputs = model(**inputs)

# Display results
print("Input IDs:")
print(inputs["input_ids"])

print("\nAttention Mask:")
print(inputs["attention_mask"])

print("\nModel Output Shape:")
print(outputs.last_hidden_state.shape)
```

### 🔍 Explanation

- `return_tensors="pt"` returns PyTorch tensors.
- `input_ids` contains numerical token IDs.
- `attention_mask` identifies actual tokens and padding positions.
- `model(**inputs)` passes the tokenizer outputs into the model.
- `torch.no_grad()` disables gradient calculation during inference.
- `last_hidden_state` contains contextual representations for every input token.

---

## 🏷️ 4. Understanding Model Checkpoints

A model checkpoint identifies a particular pretrained model available locally or on the Hugging Face Model Hub.

For example:

```python
model_name = "bert-base-uncased"
```

Some other popular model checkpoints are:

| Model Checkpoint | Description |
|---|---|
| `bert-base-uncased` | BERT Base with lowercase text processing |
| `bert-base-cased` | BERT Base that preserves letter casing |
| `roberta-base` | Base RoBERTa model |
| `distilbert-base-uncased` | Smaller DistilBERT model |
| `gpt2` | GPT-2 language model |

We can replace the checkpoint name in `from_pretrained()` to load another compatible model.

---

## ⚙️ 5. Using a Different Model Architecture

The Auto classes automatically identify the appropriate model architecture from the checkpoint configuration.

For example:

```python
from transformers import AutoTokenizer, AutoModel

# Select model checkpoint
model_name = "distilbert-base-uncased"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Input text
text = "I am learning NLP."

# Tokenize input
inputs = tokenizer(text, return_tensors="pt")

# Generate model output
outputs = model(**inputs)

# Display output shape
print(outputs.last_hidden_state.shape)
```

The same loading approach works with other compatible encoder models.

---

## 📂 6. Loading a Model from a Local Directory

A pretrained model can also be saved locally and loaded later.

### Save Model and Tokenizer

```python
from transformers import AutoTokenizer, AutoModel

# Load pretrained model
model_name = "bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Save model and tokenizer
tokenizer.save_pretrained("my_bert_model")
model.save_pretrained("my_bert_model")
```

### Load from Local Directory

```python
from transformers import AutoTokenizer, AutoModel

# Load model and tokenizer from local directory
tokenizer = AutoTokenizer.from_pretrained("my_bert_model")
model = AutoModel.from_pretrained("my_bert_model")

print("Model and tokenizer loaded successfully!")
```

This allows us to reuse saved model checkpoints without downloading them again.

---

## 🔍 Important Methods

| Method | Purpose |
|---|---|
| `AutoTokenizer.from_pretrained()` | Loads a pretrained tokenizer. |
| `AutoModel.from_pretrained()` | Loads a pretrained base model. |
| `tokenizer.tokenize()` | Converts text into tokens. |
| `tokenizer.convert_tokens_to_ids()` | Converts tokens into token IDs. |
| `tokenizer.save_pretrained()` | Saves tokenizer files locally. |
| `model.save_pretrained()` | Saves model weights and configuration. |
| `model(**inputs)` | Passes input tensors through the model. |

---

## ⚠️ Important Points

- 🌐 The first time a model is loaded, its files are generally downloaded from the Hugging Face Model Hub.
- 💾 Downloaded files are cached locally for reuse.
- 🔤 Always use the tokenizer compatible with the selected model checkpoint.
- 🧠 `AutoModel` loads a base model, not a task-specific classification head.
- 🎯 For specific tasks, classes such as `AutoModelForSequenceClassification` or `AutoModelForTokenClassification` may be required.
- 🔒 Use `torch.no_grad()` during inference when gradients are not needed.
- 📦 Some models may require additional dependencies or configuration.

---

## 💡 Key Takeaways

- 📥 Pretrained models can be loaded directly using Hugging Face Transformers.
- 🔤 `AutoTokenizer` converts text into model-compatible inputs.
- 🧠 `AutoModel` loads the pretrained model architecture and weights.
- 🔄 Both tokenizer and model are generally required to process text.
- 🏷️ Model checkpoints identify specific pretrained models.
- 📂 Models and tokenizers can be saved and loaded from local directories.
- ⚙️ Auto classes make it easier to work with different model architectures.
