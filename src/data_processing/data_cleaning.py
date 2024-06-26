# src/data_processing/data_cleaning.py

def clean_data(data):
    # Implement data cleaning steps
    # For example, handling missing values, removing duplicates, etc.
    cleaned_data = data.dropna().drop_duplicates()
    return cleaned_data
