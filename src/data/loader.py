def load_csv(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def load_json(file_path):
    import pandas as pd
    return pd.read_json(file_path)

def load_excel(file_path):
    import pandas as pd
    return pd.read_excel(file_path)

def load_data(file_path, file_type):
    if file_type == 'csv':
        return load_csv(file_path)
    elif file_type == 'json':
        return load_json(file_path)
    elif file_type == 'excel':
        return load_excel(file_path)
    else:
        raise ValueError("Unsupported file type: {}".format(file_type))