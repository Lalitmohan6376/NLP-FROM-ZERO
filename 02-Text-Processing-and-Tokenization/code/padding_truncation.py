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

# Do sentences le rahe hain jinki length different hai.

texts = [
    "I love NLP.",
    "Natural Language Processing helps computers understand human language."
]


# ============================================================
# 4. PADDING
# ============================================================

# padding=True batch ke longest sequence ke according
# chhote sequences mein padding tokens add karta hai.

padded_output = tokenizer(
    texts,
    padding=True,
    return_attention_mask=True
)

print("Padded Input IDs:")
print(padded_output["input_ids"])


# ============================================================
# 5. ATTENTION MASK
# ============================================================

# Attention Mask batata hai ki kaunse tokens actual input hain.
# 1 = Actual Token
# 0 = Padding Token

print("\nAttention Mask:")
print(padded_output["attention_mask"])


# ============================================================
# 6. PADDING WITH FIXED LENGTH
# ============================================================

# padding='max_length' har sequence ko fixed length deta hai.
# max_length=12 ka matlab har sequence mein 12 positions hongi.

fixed_output = tokenizer(
    texts,
    padding="max_length",
    max_length=12,
    return_attention_mask=True
)

print("\nFixed Length Input IDs:")
print(fixed_output["input_ids"])

print("\nFixed Length Attention Mask:")
print(fixed_output["attention_mask"])


# ============================================================
# 7. TRUNCATION
# ============================================================

# truncation=True maximum length se extra tokens remove karta hai.
# max_length=12 se har sequence ki maximum length 12 hogi.

truncated_output = tokenizer(
    texts,
    padding="max_length",
    truncation=True,
    max_length=12,
    return_attention_mask=True
)

print("\nTruncated Input IDs:")
print(truncated_output["input_ids"])


# ============================================================
# 8. DECODE OUTPUT
# ============================================================

# Token IDs ko readable text mein convert kar rahe hain.
# Special aur padding tokens output se remove honge.

for ids in truncated_output["input_ids"]:
    decoded_text = tokenizer.decode(
        ids,
        skip_special_tokens=True
    )

    print("\nDecoded Text:")
    print(decoded_text)
