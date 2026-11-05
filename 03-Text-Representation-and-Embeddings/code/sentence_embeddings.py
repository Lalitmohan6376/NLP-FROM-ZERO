
# Import required libraries
import torch
from transformers import AutoTokenizer, AutoModel

# Load pretrained BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load pretrained BERT model
model = AutoModel.from_pretrained("bert-base-uncased")

# Input sentence
text = "The cat is drinking milk."

# Tokenize the sentence
inputs = tokenizer(
    text,
    return_tensors="pt",
    padding=True
)

# Generate token embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Extract token embeddings
token_embeddings = outputs.last_hidden_state

# Extract attention mask
attention_mask = inputs["attention_mask"]

# Expand attention mask to match embedding dimensions
mask = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()

# Remove padding tokens from the calculation
masked_embeddings = token_embeddings * mask

# Calculate mean of token embeddings
sum_embeddings = masked_embeddings.sum(dim=1)

# Count actual tokens
sum_mask = mask.sum(dim=1)

# Generate sentence embedding
sentence_embedding = sum_embeddings / sum_mask

# Display sentence embedding
print("Sentence Embedding:")
print(sentence_embedding)

# Display embedding shape
print("\nSentence Embedding Shape:")
print(sentence_embedding.shape)
