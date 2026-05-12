def train_model(X_train, y_train, model):
    model.fit(X_train, y_train)
    return model

def save_model(model, filename):
    import joblib
    joblib.dump(model, filename)

def load_model(filename):
    import joblib
    return joblib.load(filename)

def evaluate_model(model, X_test, y_test):
    from sklearn.metrics import accuracy_score, classification_report
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    return accuracy, report

# Example usage:
# if __name__ == "__main__":
#     from sklearn.model_selection import train_test_split
#     from sklearn.ensemble import RandomForestClassifier
#     from data.loader import load_data  # Assuming load_data is defined in loader.py
#     
#     data = load_data('path/to/dataset.csv')
#     X = data['features']
#     y = data['target']
#     
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     model = RandomForestClassifier()
#     trained_model = train_model(X_train, y_train, model)
#     save_model(trained_model, 'model.joblib')
#     accuracy, report = evaluate_model(trained_model, X_test, y_test)
#     print(f"Accuracy: {accuracy}")
#     print(report)