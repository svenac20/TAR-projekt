import pandas as pd
from pathlib import Path

TRAIN_PATH = Path(__file__).parent.parent / 'dataset' / 'dreaddit-test.csv'
TEST_PATH = Path(__file__).parent.parent / 'dataset' / 'dreaddit-train.csv'

csv = pd.read_csv(TRAIN_PATH)


# Data preprocessing

print(csv.columns)