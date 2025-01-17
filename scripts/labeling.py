def save_to_conll(data, output_path):
    """
    Saves labeled data to a CoNLL format text file.
    Args:
        data (list of dict): List of token-label pairs.
        output_path (str): Path to save the labeled data in CoNLL format.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        for entry in data:
            for token, label in entry["tokens"]:
                f.write(f"{token}\t{label}\n")
            f.write("\n")  # Separate sentences/messages

def label_example_message():
    """
    Example of manual labeling for demonstration.
    Returns:
        list of dict: Labeled data.
    """
    example_message = "አሜሪካ ዋጋ 1000 ብር"
    tokens = [("አሜሪካ", "B-LOC"), ("ዋጋ", "B-PRICE"), ("1000", "I-PRICE"), ("ብር", "I-PRICE")]
    return [{"tokens": tokens}]
