def load_model(model_path):
    import joblib
    return joblib.load(model_path)

def predict_sentiment(model, features):
    return model.predict(features)

def main(model_path, features):
    model = load_model(model_path)
    predictions = predict_sentiment(model, features)
    return predictions

if __name__ == "__main__":
    import sys
    model_path = sys.argv[1]
    features = sys.argv[2]  # This should be preprocessed features
    predictions = main(model_path, features)
    print(predictions)