# ==========================================
# Working with Pretrained BERT Model
# ==========================================

import torch
from transformers import AutoTokenizer, AutoModel

# Load BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load pretrained BERT model
model = AutoModel.from_pretrained("bert-base-uncased")

# Input text
text = "I love learning Natural Language Processing."

# Tokenize input text
inputs = tokenizer(text, return_tensors="pt")

# Set model to evaluation mode
model.eval()

# Generate contextual representations
with torch.no_grad():
    outputs = model(**inputs)

# Display tokens
print("Tokens:")
print(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0]))

# Display input IDs
print("\nInput IDs:")
print(inputs["input_ids"])

# Display output shape
print("\nLast Hidden State Shape:")
print(outputs.last_hidden_state.shape)

# Display contextual representation of first token
print("\nFirst Token Representation:")
print(outputs.last_hidden_state[0][0])
