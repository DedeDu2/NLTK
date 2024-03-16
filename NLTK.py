import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# Sample text
text = "Hello, how are you?"

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)
