# ============================================================
# 1. IMPORT LIBRARY
# ============================================================

from transformers import AutoTokenizer


# ============================================================
# 2. LOAD PRETRAINED TOKENIZER
# ============================================================

# BERT ka pretrained tokenizer load kar rahe hain.

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


# ============================================================
# 3. INPUT TEXT
# ============================================================

text = "I love learning Natural Language Processing."


# ============================================================
# 4. TOKENIZATION
# ============================================================

# Text ko tokens mein convert kar rahe hain.

tokens = tokenizer.tokenize(text)

print("Tokens:")
print(tokens)


# ============================================================
# 5. CONVERT TOKENS INTO TOKEN IDs
# ============================================================

# Har token ko vocabulary ke corresponding numerical ID mein
# convert kar rahe hain.

token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("\nToken IDs:")
print(token_ids)


# ============================================================
# 6. ENCODING
# ============================================================

# encode() text ko directly Token IDs mein convert karta hai.
# add_special_tokens=True se BERT ke special tokens bhi add honge.

encoded_ids = tokenizer.encode(text, add_special_tokens=True)

print("\nEncoded IDs:")
print(encoded_ids)


# ============================================================
# 7. CONVERT TOKEN IDs BACK INTO TOKENS
# ============================================================

# Numerical IDs ko wapas tokens mein convert kar rahe hain.

converted_tokens = tokenizer.convert_ids_to_tokens(encoded_ids)

print("\nConverted Tokens:")
print(converted_tokens)


# ============================================================
# 8. DECODING
# ============================================================

# Token IDs ko wapas readable text mein convert kar rahe hain.
# skip_special_tokens=True special tokens ko output se hata deta hai.

decoded_text = tokenizer.decode(
    encoded_ids,
    skip_special_tokens=True
)

print("\nDecoded Text:")
print(decoded_text)
