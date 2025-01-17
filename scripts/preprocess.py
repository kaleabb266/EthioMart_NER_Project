import pandas as pd
import re

def preprocess_text(text):
    """
    Preprocesses raw Amharic text by removing noise and normalizing.
    Args:
        text (str): The raw text message.
    Returns:
        str: The cleaned and normalized text.
    """
    if not isinstance(text, str):
        return ""
    
    # Remove links
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    # Remove special characters and numbers
    text = re.sub(r"[^፡-፣፤-፨ሀ-፼ ]", "", text)
    # Normalize spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess_data(input_path, output_path):
    """
    Preprocesses the raw dataset and saves the cleaned dataset.
    Args:
        input_path (str): Path to the raw data CSV file.
        output_path (str): Path to save the preprocessed data.
    """
    df = pd.read_csv(input_path)
    
    # Check if 'Message' column exists
    if 'Message' not in df.columns:
        raise KeyError("'Message' column is missing from the input data.")
    
    df["cleaned_content"] = df["Message"].apply(preprocess_text)  # Changed 'content' to 'Message'
    df = df.dropna(subset=["cleaned_content"])  # Remove rows with empty content
    df.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")
