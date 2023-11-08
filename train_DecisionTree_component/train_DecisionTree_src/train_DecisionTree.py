import argparse
from pathlib import Path
import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier
import pickle
import mlflow

parser = argparse.ArgumentParser("train_decision_tree")
parser.add_argument("--data_train", type=str, help="Path to training data")
parser.add_argument("--criterion", type=str, help="The function to measure the quality of a split.")
parser.add_argument("--min_samples_split", type=int, help="The minimum number of samples required to split an internal node")
parser.add_argument("--max_depth", type=int, help="The maximum depth of the tree. ")
parser.add_argument("--model_output_dt_pickle", type=str, help="Path of output model pickle")

args = parser.parse_args()

print("Arguments Decision Tree model")

lines = [
    f"data_train: {args.data_train}",
    f"criterion: {args.criterion}",
    f"min_samples_split: {args.min_samples_split}",
    f"max_depth: {args.max_depth}",
    f"model_output_dt_pickle: {args.model_output_dt_pickle}",
]

for line in lines:
    print(line)

# Read data
data_train = pd.read_csv(args.data_train)
X_train = data_train.iloc[:,:-1]
y_train = data_train.iloc[:,-1]

# Train model
model_dt = DecisionTreeClassifier(criterion= args.criterion, min_samples_split= args.min_samples_split, max_depth=args.max_depth)
model_dt.fit(X_train,y_train)

# Save model.pkl
new_dir = Path('.', args.model_output_dt_pickle)
with open(f'{new_dir}/model.pkl', 'wb') as f:  # open a text file
    pickle.dump(model_dt, f)
