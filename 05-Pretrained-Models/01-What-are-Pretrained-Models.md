# 🤖 What Are Pretrained Models?

## 📖 Introduction

A **Pretrained Model** is a machine learning model that has already been trained on a large dataset before being used for a specific task.

In Natural Language Processing (NLP), pretrained models learn language patterns, word relationships, grammar, and contextual information by processing large amounts of text.

Instead of training a model from scratch, we can use an existing pretrained model and apply it to different NLP tasks.

For example, models such as **BERT, GPT, RoBERTa, and DistilBERT** are pretrained language models.

They can be used for tasks such as:

- 😊 Sentiment Analysis
- 🏷️ Text Classification
- 🏢 Named Entity Recognition
- ❓ Question Answering
- 📄 Text Summarization
- 🌐 Machine Translation

---

## 🎯 Why Pretrained Models?

Training a language model from scratch requires large datasets, significant computational resources, and considerable training time.

Pretrained models reduce this effort by providing a model that has already learned useful language representations.

Their main advantages are:

- ⏱️ **Save Training Time:** We do not need to train the entire model from scratch.
- 📚 **Learn from Large Datasets:** Models are pretrained on large collections of text.
- 🧠 **Capture Language Patterns:** They learn grammar, vocabulary, and contextual relationships.
- 💻 **Reduce Computational Requirements:** We can reuse existing model weights instead of performing complete pretraining.
- 🎯 **Support Multiple NLP Tasks:** A pretrained model can be adapted to different downstream tasks.
- ⚙️ **Enable Fine-Tuning:** We can further train a pretrained model on task-specific data.

---

## ⚙️ How Pretrained Models Work

The pretrained model workflow generally involves the following stages:

### 1. 📚 Pretraining Dataset

First, a large text dataset is collected.

It may contain:

- 📖 Books
- 🌐 Web pages
- 📰 Articles
- 📄 Documents
- 💬 Other text sources

The quality, size, and composition of the training data influence what the model learns.

### 2. 🧠 Pretraining

The model is trained on the collected dataset using a learning objective.

Different models use different objectives.

For example:

- **BERT:** Learns through masked language modeling and, in its original version, next sentence prediction.
- **GPT:** Learns to predict the next token in a sequence.

During pretraining, the model learns useful language patterns and representations.

### 3. 💾 Save the Trained Model

After pretraining, the model's learned parameters are saved.

These saved parameters are called **Model Weights**.

A pretrained model checkpoint generally includes the model weights and configuration required to load the architecture.

The tokenizer files may also be included.

### 4. 🛠️ Use the Pretrained Model

The pretrained model can now be loaded and used for NLP tasks.

For example, we can use a pretrained BERT model to generate contextual representations of input text.

### 5. ⚙️ Fine-Tuning (Optional)

If we want to use the model for a specific task, we can fine-tune it using a task-specific dataset.

For example:

A pretrained BERT model can be fine-tuned using labeled movie reviews to perform sentiment classification.

Fine-tuning is not always required. Some pretrained models can be used directly for supported tasks.

---

## 🔄 Pretraining vs Fine-Tuning

Pretraining and fine-tuning are two different stages of model training.

| Pretraining | Fine-Tuning |
|---|---|
| Trains a model on a large general dataset. | Further trains an existing pretrained model. |
| Learns general language patterns. | Adapts the model to a specific task or domain. |
| Usually requires substantial computational resources. | Often requires fewer resources than pretraining. |
| Produces a pretrained model. | Produces a task-adapted model. |
| Uses general training objectives. | Uses objectives suitable for the target task. |

### Example

```text
             Large Text Dataset
                     |
                     ▼
                Pretraining
                     |
                     ▼
              Pretrained BERT
                     |
                     ▼
              Labeled Reviews
                     |
                     ▼
                Fine-Tuning
                     |
                     ▼
          Sentiment Classification Model
```

---

## 🧩 Types of Pretrained Language Models

Pretrained language models can be grouped according to their Transformer architecture.

### 1. 🧠 Encoder-Only Models

Encoder-only models use the Transformer encoder architecture.

They are mainly designed to understand input text and generate contextual representations.

Examples:

- **BERT:** Bidirectional Encoder Representations from Transformers.
- **RoBERTa:** A robustly optimized version of BERT.
- **DistilBERT:** A smaller and faster model derived from BERT using knowledge distillation.

Common applications:

- Text Classification
- Sentiment Analysis
- Named Entity Recognition
- Extractive Question Answering

### 2. ✍️ Decoder-Only Models

Decoder-only models use the Transformer decoder architecture with causal attention.

They generate text by predicting the next token based on previously available tokens.

Examples:

- **GPT:** Generative Pre-trained Transformer.
- **GPT-2:** An autoregressive language model developed by OpenAI.
- **LLaMA:** A family of autoregressive language models developed by Meta.

Common applications:

- Text Generation
- Conversational AI
- Code Generation
- Language Modeling

### 3. 🔄 Encoder-Decoder Models

Encoder-decoder models use both Transformer components.

The encoder processes the input sequence, while the decoder generates an output sequence using the encoder's representations.

Examples:

- **T5:** Text-to-Text Transfer Transformer.
- **BART:** Bidirectional and Auto-Regressive Transformers.
- **Original Transformer:** The encoder-decoder architecture introduced in the paper *Attention Is All You Need*.

Common applications:

- Machine Translation
- Text Summarization
- Text-to-Text Generation

---

## 🏗️ Popular Pretrained Models

Some widely used pretrained NLP models include:

| Model | Architecture | Main Purpose |
|---|---|---|
| BERT | Encoder-Only | Language Understanding |
| RoBERTa | Encoder-Only | Language Understanding |
| DistilBERT | Encoder-Only | Efficient Language Understanding |
| GPT | Decoder-Only | Text Generation |
| GPT-2 | Decoder-Only | Autoregressive Text Generation |
| T5 | Encoder-Decoder | Text-to-Text Tasks |
| BART | Encoder-Decoder | Text Generation and Summarization |

---

## 🤗 Pretrained Models in Hugging Face

Hugging Face provides access to thousands of pretrained models through its **Model Hub**.

The Model Hub allows us to:

- 🔍 Search for pretrained models.
- 📥 Download model checkpoints.
- ⚙️ Load models using Transformers.
- 📝 Access model documentation and configurations.
- 🚀 Use models for different NLP tasks.
- 🏋️ Fine-tune existing models.

Official resources:

- 🤗 [Hugging Face Model Hub](https://huggingface.co/models)
- 📚 [Transformers Documentation](https://huggingface.co/docs/transformers/index)

---

## 💡 Key Takeaways

- 🤖 A pretrained model is a model that has already learned from a dataset before being used for a specific task.
- 📚 Pretraining helps models learn general language patterns and representations.
- 💾 Model weights store the parameters learned during training.
- ⚙️ Fine-tuning adapts a pretrained model to a specific task or domain.
- 🧠 BERT and RoBERTa are encoder-only models.
- ✍️ GPT is a decoder-only model.
- 🔄 T5 and BART are encoder-decoder models.
- 🤗 Hugging Face provides a large collection of pretrained models through its Model Hub.
