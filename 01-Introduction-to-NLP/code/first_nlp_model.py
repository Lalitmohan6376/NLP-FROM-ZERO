
# ============================================================
# 1. INTRODUCTION TO NLP
# ============================================================

# Transformers library se pipeline import kar rahe hain.
# Pipeline pretrained NLP models ko easily use karne deti hai.

from transformers import pipeline


# Ek simple text input le rahe hain.

text = "I love learning Artificial Intelligence."


# Text ko NLP model ke through process kar rahe hain.
# sentiment-analysis ek predefined NLP task hai.
# Pipeline automatically suitable pretrained model load karti hai.

sentiment_model = pipeline("sentiment-analysis")


# Model se prediction karwa rahe hain.

result = sentiment_model(text)


# Prediction print kar rahe hain.

print("Original Text:", text)
print("NLP Prediction:", result)


# ============================================================
# 2. NLP APPLICATIONS
# ============================================================

# Yahan hum different text examples par sentiment analysis
# perform karenge.

sentences = [
    "This product is amazing.",
    "I am very disappointed with this service.",
    "The product is okay."
]


# Har sentence ka sentiment predict kar rahe hain.

results = sentiment_model(sentences)


# Har sentence aur uska prediction print kar rahe hain.

print("\nNLP Application: Sentiment Analysis")

for sentence, prediction in zip(sentences, results):
    print("\nText:", sentence)
    print("Sentiment:", prediction["label"])
    print("Confidence:", prediction["score"])


# ============================================================
# 3. NLP WORKFLOW
# ============================================================

# Step 1: Raw Text
# Sabse pehle original text input le rahe hain.

raw_text = "I REALLY love this product!"


# Step 2: Text Processing
# Text ko lowercase mein convert kar rahe hain.
# strip() starting aur ending ke extra spaces remove karta hai.

processed_text = raw_text.lower().strip()


# Step 3: Tokenization
# Tokenizer text ko smaller units yani tokens mein divide karta hai.

tokenizer = sentiment_model.tokenizer

tokens = tokenizer.tokenize(processed_text)


# Step 4: Numerical Representation
# Tokens ko numerical IDs mein convert kar rahe hain.

token_ids = tokenizer.encode(processed_text)


# Step 5: Model Processing
# Processed text ko sentiment model mein pass kar rahe hain.

prediction = sentiment_model(processed_text)


# Step 6: Output Generation
# Model ka final prediction display kar rahe hain.

print("\nNLP Workflow")

print("\nStep 1 - Raw Text:")
print(raw_text)

print("\nStep 2 - Processed Text:")
print(processed_text)

print("\nStep 3 - Tokens:")
print(tokens)

print("\nStep 4 - Token IDs:")
print(token_ids)

print("\nStep 5 - Model Processing:")
print("Sentiment model has processed the input.")

print("\nStep 6 - Final Output:")
print("Label:", prediction[0]["label"])
print("Confidence:", prediction[0]["score"])
