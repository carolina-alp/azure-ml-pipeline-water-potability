import argparse
from pathlib import Path
import os
import pandas as pd
from sklearn.model_selection import train_test_split

# obtener parámetros:
parser = argparse.ArgumentParser("split")
parser.add_argument("--data_set", type=str, help="Dataset file")
parser.add_argument("--split_ratio_train", type=float, help="split ration train")
parser.add_argument("--data_train", type=str, help="File containing dataset for training")
parser.add_argument("--data_test", type=str, help="File containing dataset for testing")

args = parser.parse_args()

lines = [
    f"data_set: {args.data_set}",
    f"split_ratio_train: {args.split_ratio_train}",
    f"data_train: {args.data_train}",
    f"data_test: {args.data_test}",
]

print("Parameters: ...")
# Print parameters:
for line in lines:
    print(line)

# Split dataset
data = pd.read_csv(args.data_set)
train_data, test_data = train_test_split(data, train_size=args.split_ratio_train, random_state=42)
train_data.to_csv(args.data_train, index=False)
test_data.to_csv(args.data_test, index=False)

