# Import required libraries
import torch
from transformers import AutoTokenizer, AutoModel

# Load pretrained tokenizer and model
model_name = "bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Input text
text = "Transformers are powerful models for NLP."

# Convert text into tokens and token IDs
inputs = tokenizer(text, return_tensors="pt")

# Display input tokens
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

print("Tokens:")
print(tokens)

# Pass input through the Transformer model
with torch.no_grad():
    outputs = model(**inputs)

# Get final hidden states
hidden_states = outputs.last_hidden_state

# Display input shape
print("\nInput Shape:")
print(inputs["input_ids"].shape)

# Display Transformer output shape
print("\nTransformer Output Shape:")
print(hidden_states.shape)

# Display representation of the first token
print("\nFirst Token Representation:")
print(hidden_states[0][0])
