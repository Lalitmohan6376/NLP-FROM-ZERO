# Import required libraries
import torch
import torch.nn.functional as F

# Input token representations
# Each row represents one token with 4 features
tokens = torch.tensor([
    [1.0, 0.0, 1.0, 0.0],
    [0.0, 2.0, 0.0, 2.0],
    [1.0, 1.0, 0.0, 1.0]
])

# Create Query, Key and Value matrices
query = tokens
key = tokens
value = tokens

# Calculate attention scores
scores = torch.matmul(query, key.T)

# Scale attention scores
d_k = key.shape[-1]
scores = scores / (d_k ** 0.5)

# Convert scores into attention weights
attention_weights = F.softmax(scores, dim=-1)

# Calculate final attention output
output = torch.matmul(attention_weights, value)

# Display results
print("Input Tokens:")
print(tokens)

print("\nAttention Scores:")
print(scores)

print("\nAttention Weights:")
print(attention_weights)

print("\nSelf-Attention Output:")
print(output)
