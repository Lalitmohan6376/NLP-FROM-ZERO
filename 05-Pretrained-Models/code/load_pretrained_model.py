# ==========================================
# Load a Pretrained Model using Transformers
# ==========================================

from transformers import AutoTokenizer, AutoModel

# Load pretrained tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load pretrained model
model = AutoModel.from_pretrained("bert-base-uncased")

# Input text
text = "I love learning Natural Language Processing."

# Convert text into model inputs
inputs = tokenizer(text, return_tensors="pt")

# Display tokenizer output
print("Input IDs:")
print(inputs["input_ids"])

print("\nAttention Mask:")
print(inputs["attention_mask"])

# Display model architecture
print("\nPretrained Model:")
print(model)

# Display model information
print("\nModel Hidden Size:")
print(model.config.hidden_size)

print("\nNumber of Transformer Layers:")
print(model.config.num_hidden_layers)
