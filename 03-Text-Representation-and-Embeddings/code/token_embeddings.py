
# Import required libraries
import torch
from transformers import AutoTokenizer, AutoModel

# Load pretrained BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load pretrained BERT model
model = AutoModel.from_pretrained("bert-base-uncased")

# Input sentence
text = "The cat is drinking milk."

# Convert text into token IDs
inputs = tokenizer(text, return_tensors="pt")

# Generate embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Extract token embeddings
token_embeddings = outputs.last_hidden_state

# Display tokens
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

print("Tokens:")
print(tokens)

# Display embedding shape
print("\nToken Embeddings Shape:")
print(token_embeddings.shape)

# Display embedding of each token
for i in range(len(tokens)):
    print("\nToken:", tokens[i])
    print("Embedding:", token_embeddings[0][i])
