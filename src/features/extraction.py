from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def extract_features(text_data, method='tfidf'):
    if method == 'tfidf':
        vectorizer = TfidfVectorizer()
        features = vectorizer.fit_transform(text_data)
    elif method == 'count':
        vectorizer = CountVectorizer()
        features = vectorizer.fit_transform(text_data)
    else:
        raise ValueError("Method must be 'tfidf' or 'count'")
    
    return features, vectorizer

def get_feature_names(vectorizer):
    return vectorizer.get_feature_names_out()