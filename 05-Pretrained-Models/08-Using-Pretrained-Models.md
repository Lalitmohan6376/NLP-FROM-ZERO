# 🤗 Using Pretrained Models

## 📌 Introduction

Pretrained models are neural networks that have already been trained on large amounts of data.

Instead of training a model from scratch, we can load an existing pretrained model and use it for different NLP tasks.

The **Hugging Face Transformers** library makes it easy to download, load, and use pretrained models.

For example, we can use pretrained models such as:

- 🧠 BERT for text understanding.
- ✍️ GPT for text generation.
- 🔄 T5 for text-to-text tasks.
- ⚡ DistilBERT for lightweight NLP applications.
- 🚀 RoBERTa for language understanding.

---

## 1️⃣ Understanding the Pretrained Model Workflow

Using a pretrained model generally involves the following steps:

```text
       Input Text
           |
           v
        Tokenizer
           |
           v
        Token IDs
           |
           v
     Pretrained Model
           |
           v
     Model Processing
           |
           v
       Model Output
           |
           v
    Output Interpretation
```

### ⚙️ Main Steps

1. **Load Tokenizer:** Load the tokenizer associated with the pretrained checkpoint.
2. **Load Model:** Load the pretrained model and its weights.
3. **Prepare Input:** Convert text into token IDs and other required inputs.
4. **Run Inference:** Pass the tokenized inputs to the model.
5. **Process Output:** Interpret the model's output according to the NLP task.

---

## 2️⃣ Loading a Pretrained Tokenizer

A tokenizer converts human-readable text into tokens and numerical IDs that a model can process.

Hugging Face provides `AutoTokenizer` to load the correct tokenizer automatically.

### 💻 Code

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "I love learning Natural Language Processing."

tokens = tokenizer.tokenize(text)

print(tokens)
```

### 🔍 Explanation

- `AutoTokenizer` automatically selects the appropriate tokenizer architecture.
- `from_pretrained()` loads the tokenizer associated with the checkpoint.
- `tokenize()` converts the input sentence into tokens.

The output contains tokens that can be converted into numerical IDs.

---

## 3️⃣ Converting Text into Model Inputs

After tokenization, we need to convert the text into numerical representations.

We can use the tokenizer directly to generate model inputs.

### 💻 Code

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "I love learning NLP."

inputs = tokenizer(text)

print(inputs)
```

### 🔍 Understanding the Output

The tokenizer generally returns a dictionary containing fields such as:

- `input_ids`: Numerical IDs representing tokens.
- `token_type_ids`: Segment IDs used by models that support them.
- `attention_mask`: Identifies actual tokens and padding tokens.

The exact fields depend on the model architecture and tokenizer.

### 🔹 Getting PyTorch Tensors

We can use `return_tensors="pt"` to receive PyTorch tensors.

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "I love learning NLP."

inputs = tokenizer(text, return_tensors="pt")

print(inputs)
```

The resulting tensors can be passed directly to a compatible PyTorch model.

---

## 4️⃣ Loading a Pretrained Model

After loading the tokenizer, we can load the corresponding pretrained model.

Hugging Face provides `AutoModel` for loading a base Transformer model without a task-specific prediction head.

### 💻 Code

```python
from transformers import AutoModel

model = AutoModel.from_pretrained("bert-base-uncased")

print(model)
```

### 🔍 Explanation

- `AutoModel` automatically selects the appropriate model architecture.
- `from_pretrained()` downloads the model configuration and pretrained weights.
- The loaded model can generate contextual representations of input tokens.

**Important:** `AutoModel` does not automatically perform tasks such as sentiment classification or text generation. It provides the base model outputs.

---

## 5️⃣ Performing Inference with a Pretrained Model

Inference means using an already trained model to process new input data and generate predictions or representations.

Let's load BERT and generate contextual representations for a sentence.

### 💻 Code

```python
import torch
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

model = AutoModel.from_pretrained("bert-base-uncased")

text = "I love learning NLP."

inputs = tokenizer(text, return_tensors="pt")

model.eval()

with torch.no_grad():
    outputs = model(**inputs)

print(outputs.last_hidden_state.shape)
```

### 🔍 Explanation

**1. Load Tokenizer**

```python
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
```

Loads the tokenizer associated with BERT.

**2. Load Model**

```python
model = AutoModel.from_pretrained("bert-base-uncased")
```

Loads the pretrained BERT model.

**3. Tokenize Input**

```python
inputs = tokenizer(text, return_tensors="pt")
```

Converts the sentence into PyTorch tensors.

**4. Set Evaluation Mode**

```python
model.eval()
```

Disables training-specific behavior such as dropout.

**5. Run Inference**

```python
with torch.no_grad():
    outputs = model(**inputs)
```

Runs the model without calculating gradients.

**6. Get Model Output**

```python
outputs.last_hidden_state
```

Returns contextual representations for every input token.

### 📊 Understanding the Output Shape

The output shape follows this structure:

```text
(batch_size, sequence_length, hidden_size)
```

For BERT Base:

- `batch_size`: Number of input sequences.
- `sequence_length`: Number of tokens, including special tokens.
- `hidden_size`: 768.

For one sentence, the batch size is 1.

---

## 6️⃣ Using AutoModelForSequenceClassification

For classification tasks, we need a model with a classification head.

Hugging Face provides `AutoModelForSequenceClassification` for this purpose.

It adds a task-specific classification layer to the pretrained Transformer model.

### 💻 Code

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=2
)

text = "I really enjoyed this movie."

inputs = tokenizer(text, return_tensors="pt")

model.eval()

with torch.no_grad():
    outputs = model(**inputs)

print(outputs.logits)
```

### 🔍 Explanation

- `AutoModelForSequenceClassification` loads a Transformer with a sequence classification head.
- `num_labels=2` creates a classification head with two output classes.
- `outputs.logits` contains the raw classification scores.

**Important:** The classification head created from a base checkpoint is generally newly initialized. The model must be fine-tuned on a labeled classification dataset before its predictions can be considered meaningful.

---

## 7️⃣ Using AutoModelForCausalLM

For autoregressive text generation, we can use `AutoModelForCausalLM`.

It loads a decoder-style language model with a causal language modeling head.

### 💻 Code

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")

model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")

text = "Artificial intelligence is"

inputs = tokenizer(text, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_new_tokens=30
)

generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)
```

### 🔍 Explanation

- `AutoModelForCausalLM` loads a causal language model.
- `generate()` produces new tokens based on the input prompt.
- `max_new_tokens=30` limits the number of newly generated tokens.
- `decode()` converts generated token IDs back into readable text.
- `skip_special_tokens=True` removes special tokens from the decoded output.

The generated text depends on the pretrained checkpoint and generation settings.

---

## 8️⃣ Using Pretrained Models Through Pipelines

Hugging Face provides the `pipeline()` function to simplify common NLP tasks.

A pipeline combines tokenization, model execution, and output processing into a single interface.

### 🔹 Sentiment Analysis

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("I really enjoyed this movie.")

print(result)
```

The pipeline loads a default sentiment analysis model and returns a label with a confidence score.

### 🔹 Named Entity Recognition

```python
from transformers import pipeline

ner = pipeline("ner", aggregation_strategy="simple")

text = "Google was founded in California."

result = ner(text)

print(result)
```

The pipeline identifies entities such as organizations, locations, and people.

### 🔹 Text Generation

```python
from transformers import pipeline

generator = pipeline("text-generation", model="openai-community/gpt2")

result = generator(
    "Artificial intelligence is",
    max_new_tokens=30
)

print(result)
```

The text generation pipeline uses a causal language model to continue the input prompt.

**Note:** Pipelines use task-specific pretrained checkpoints. The model's training and capabilities determine how well it performs the selected task.

---

## 9️⃣ Saving and Loading a Pretrained Model

Hugging Face provides `save_pretrained()` to save model weights and configuration locally.

We can later load the saved model without downloading the original checkpoint again.

### 💾 Saving the Model and Tokenizer

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

model = AutoModel.from_pretrained("bert-base-uncased")

tokenizer.save_pretrained("./saved_bert")

model.save_pretrained("./saved_bert")
```

This creates a local directory containing the model and tokenizer files.

### 📂 Loading the Saved Model

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("./saved_bert")

model = AutoModel.from_pretrained("./saved_bert")

print(model)
```

The model and tokenizer are loaded from the local directory.

---

## 🔟 Choosing the Right Auto Class

Hugging Face provides different Auto classes for different requirements.

| Auto Class | Purpose |
|---|---|
| `AutoTokenizer` | Loads the appropriate tokenizer |
| `AutoConfig` | Loads model configuration |
| `AutoModel` | Loads the base Transformer model |
| `AutoModelForSequenceClassification` | Loads a model for sequence classification |
| `AutoModelForTokenClassification` | Loads a model for token-level classification |
| `AutoModelForQuestionAnswering` | Loads a model for extractive question answering |
| `AutoModelForMaskedLM` | Loads a model for masked language modeling |
| `AutoModelForCausalLM` | Loads a model for autoregressive language modeling |
| `AutoModelForSeq2SeqLM` | Loads a model for sequence-to-sequence generation |

The selected Auto class must match the architecture and task supported by the checkpoint.

---

## ⚠️ Important Considerations

Before using a pretrained model, keep these points in mind:

- 📌 **Checkpoint Compatibility:** Use the tokenizer and model from compatible checkpoints.
- 🎯 **Task Compatibility:** Select a model architecture that supports your intended task.
- 🔧 **Fine-Tuning:** A pretrained base model may need additional training for a specific task.
- 💻 **Hardware Requirements:** Larger models require more memory and computational resources.
- 🔤 **Tokenization:** Different models may use different tokenization methods.
- 📏 **Sequence Length:** Follow the model's supported input length.
- ⚡ **Inference Mode:** Use `model.eval()` and `torch.no_grad()` for ordinary inference.

---

## 🎯 Key Takeaways

- 🤗 Hugging Face Transformers provides pretrained models through Auto classes.
- 🔤 `AutoTokenizer` converts text into model inputs.
- 🧠 `AutoModel` loads a base Transformer model.
- 🎯 Task-specific Auto classes provide additional prediction heads.
- ⚡ Inference means using a trained model without updating its parameters.
- ✍️ `AutoModelForCausalLM` supports autoregressive text generation.
- 🔄 `pipeline()` simplifies common NLP tasks.
- 💾 `save_pretrained()` saves models and tokenizers locally.
- 🚀 Pretrained models can be used directly for supported tasks or fine-tuned for specific applications.
