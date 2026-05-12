def clean_text(text):
    """Cleans the input text by removing unwanted characters and normalizing whitespace."""
    import re
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.strip()

def remove_stop_words(tokens):
    """Removes stop words from a list of tokens."""
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token.lower() not in stop_words]

def tokenize(text):
    """Tokenizes the input text into words."""
    from nltk.tokenize import word_tokenize
    return word_tokenize(text)

def preprocess_text(text):
    """Preprocesses the input text by cleaning, tokenizing, and removing stop words."""
    cleaned_text = clean_text(text)
    tokens = tokenize(cleaned_text)
    return remove_stop_words(tokens)