def load_json(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def calculate_accuracy(y_true, y_pred):
    from sklearn.metrics import accuracy_score
    return accuracy_score(y_true, y_pred)

def print_summary_statistics(data):
    print("Summary Statistics:")
    print(f"Count: {len(data)}")
    print(f"Mean: {sum(data) / len(data)}")
    print(f"Min: {min(data)}")
    print(f"Max: {max(data)}")