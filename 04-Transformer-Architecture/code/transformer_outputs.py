# Import required libraries
import torch
from transformers import AutoTokenizer, AutoModel

# Load pretrained tokenizer and model
model_name = "bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Input text
text = "Transformers process text using attention."

# Tokenize input text
inputs = tokenizer(text, return_tensors="pt")

# Pass input through the model
with torch.no_grad():
    outputs = model(**inputs)

# Access different Transformer outputs
last_hidden_state = outputs.last_hidden_state
pooler_output = outputs.pooler_output

# Display input tokens
print("Input Tokens:")
print(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0]))

# Display output shapes
print("\nLast Hidden State Shape:")
print(last_hidden_state.shape)

print("\nPooler Output Shape:")
print(pooler_output.shape)

# Display first token representation
print("\nFirst Token Representation:")
print(last_hidden_state[0][0])

# Display pooled representation
print("\nPooled Output:")
print(pooler_output[0])
