import pandas as pd

TRAIN_PATH = "../dataset/dreaddit-train.csv"
TEST_PATH = "../dataset/dreaddit-test.csv"

csv = pd.read_csv(TRAIN_PATH)

print(csv.columns)