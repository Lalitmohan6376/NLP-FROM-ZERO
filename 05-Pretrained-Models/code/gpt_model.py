# ==========================================
# Working with Pretrained GPT-2 Model
# ==========================================

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load GPT-2 tokenizer
tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")

# Load pretrained GPT-2 model
model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")

# Input text
text = "Artificial Intelligence is"

# Tokenize input text
inputs = tokenizer(text, return_tensors="pt")

# Set model to evaluation mode
model.eval()

# Generate text
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=30,
        do_sample=False
    )

# Convert token IDs into readable text
generated_text = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

# Display input text
print("Input Text:")
print(text)

# Display generated text
print("\nGenerated Text:")
print(generated_text)
