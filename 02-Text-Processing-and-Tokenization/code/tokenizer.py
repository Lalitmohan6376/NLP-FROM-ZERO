# ============================================================
# 1. IMPORT LIBRARY
# ============================================================

# AutoTokenizer pretrained model ka tokenizer load karta hai.

from transformers import AutoTokenizer


# ============================================================
# 2. LOAD PRETRAINED TOKENIZER
# ============================================================

# BERT ka pretrained tokenizer load kar rahe hain.
# bert-base-uncased lowercase text ke liye designed hai.

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


# ============================================================
# 3. INPUT TEXT
# ============================================================

text = "I love Natural Language Processing."


# ============================================================
# 4. WORD-LEVEL TOKENIZATION
# ============================================================

# split() text ko spaces ke basis par words mein divide karta hai.
# Ye Python ka basic word splitting hai, Transformer tokenizer nahi.

word_tokens = text.split()

print("Word-Level Tokens:")
print(word_tokens)


# ============================================================
# 5. CHARACTER-LEVEL TOKENIZATION
# ============================================================

# list() text ko individual characters mein divide karta hai.

character_tokens = list(text)

print("\nCharacter-Level Tokens:")
print(character_tokens)


# ============================================================
# 6. SUBWORD TOKENIZATION
# ============================================================

# Hugging Face tokenizer text ko subword tokens mein divide karta hai.
# BERT WordPiece tokenization use karta hai.

subword_tokens = tokenizer.tokenize(text)

print("\nSubword Tokens:")
print(subword_tokens)


# ============================================================
# 7. TOKEN COUNT
# ============================================================

# Total tokens count kar rahe hain.

print("\nTotal Word Tokens:", len(word_tokens))
print("Total Character Tokens:", len(character_tokens))
print("Total Subword Tokens:", len(subword_tokens))
