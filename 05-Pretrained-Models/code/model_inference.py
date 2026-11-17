# ==========================================
# Pretrained Model Inference using BERT
# ==========================================

import torch
from transformers import AutoTokenizer, AutoModel

# Load pretrained tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load pretrained model
model = AutoModel.from_pretrained("bert-base-uncased")

# Input text
text = "I love learning Natural Language Processing."

# Convert text into tensors
inputs = tokenizer(text, return_tensors="pt")

# Set model to evaluation mode
model.eval()

# Perform inference
with torch.no_grad():
    outputs = model(**inputs)

# Extract contextual representations
embeddings = outputs.last_hidden_state

# Display input tokens
print("Input Tokens:")
print(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0]))

# Display input shape
print("\nInput Shape:")
print(inputs["input_ids"].shape)

# Display model output shape
print("\nOutput Shape:")
print(embeddings.shape)

# Display contextual representation
print("\nFirst Token Representation:")
print(embeddings[0][0])
