import json
import os

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

DATA_FILE = os.path.join(DATA_DIR, 'predictions.json')
SCORES_FILE = os.path.join(DATA_DIR, 'scores.json')


def load_data(file_path):
    """Loads data from a JSON file.

    Args:
        file_path (str): The absolute or relative path to the file.

    Returns:
        dict: The loaded data, or an empty dictionary if it does not exist.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    return {}


def save_data(data, file_path):
    """Saves data to a JSON file.

    Args:
        data (dict): The data to save.
        file_path (str): The path to the destination file.

    Returns:
        None
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    return None