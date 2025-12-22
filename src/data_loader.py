from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

def load_sample_data():
    """
    Load the tracked sample dataset for local development and EDA.
    """
    file_path = DATA_DIR / "sample.csv"

    if not file_path.exists():
        raise FileNotFoundError(f"Sample data not found at {file_path}")

    df = pd.read_csv(file_path)

    return df
