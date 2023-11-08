import argparse
from pathlib import Path
import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import pickle
import mlflow

parser = argparse.ArgumentParser("train_logistic_regression")
parser.add_argument("--data_train", type=str, help="Path to training data")
parser.add_argument("--model_output_lr_pickle", type=str, help="Path of output model pickle")

args = parser.parse_args()

print("Arguments Logistic Regression model")

lines = [
    f"data_train: {args.data_train}",
    f"model_output_lr_pickle: {args.model_output_lr_pickle}",
]

for line in lines:
    print(line)

# Read data
data_train = pd.read_csv(args.data_train)
X_train = data_train.iloc[:,:-1]
y_train = data_train.iloc[:,-1]

# Create a binary classification model (Logistic Regression in this case)
model_lr = LogisticRegression().fit(X_train, y_train)

# Save model.pkl
new_dir = Path('.', args.model_output_lr_pickle)
with open(f'{new_dir}/model.pkl', 'wb') as f:  # open a text file
    pickle.dump(model_lr, f)




