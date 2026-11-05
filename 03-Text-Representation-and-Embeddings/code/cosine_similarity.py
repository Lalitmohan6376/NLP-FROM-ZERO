
# Import required libraries
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel

# Load pretrained BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load pretrained BERT model
model = AutoModel.from_pretrained("bert-base-uncased")

# Two input sentences
sentence1 = "The cat is drinking milk."
sentence2 = "A cat is drinking some milk."

# Tokenize both sentences
inputs = tokenizer(
    [sentence1, sentence2],
    return_tensors="pt",
    padding=True,
    truncation=True
)

# Generate token embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Extract token embeddings
token_embeddings = outputs.last_hidden_state

# Extract attention mask
attention_mask = inputs["attention_mask"]

# Expand attention mask
mask = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()

# Remove padding tokens
masked_embeddings = token_embeddings * mask

# Calculate sum of token embeddings
sum_embeddings = masked_embeddings.sum(dim=1)

# Count actual tokens
sum_mask = mask.sum(dim=1)

# Generate sentence embeddings using mean pooling
sentence_embeddings = sum_embeddings / sum_mask

# Extract embeddings of both sentences
embedding1 = sentence_embeddings[0]
embedding2 = sentence_embeddings[1]

# Calculate cosine similarity
similarity = F.cosine_similarity(
    embedding1.unsqueeze(0),
    embedding2.unsqueeze(0)
)

# Display result
print("Sentence 1:", sentence1)
print("Sentence 2:", sentence2)

print("\nCosine Similarity:")
print(similarity.item())
