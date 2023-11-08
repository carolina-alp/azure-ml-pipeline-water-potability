import argparse
from pathlib import Path
import pandas as pd
#from sklearn.linear_model import LogisticRegression
#from sklearn.tree import DecisionTreeClassifier
import pickle
import numpy as np

parser = argparse.ArgumentParser("score")
parser.add_argument("--model_input", type=str, help="Path of input model")
parser.add_argument("--test_data", type=str, help="Path to test data")
parser.add_argument("--score_output", type=str, help="Path of scoring output")

args = parser.parse_args()

lines = [
    f"Model path: {args.model_input}",
    f"Test data path: {args.test_data}",
    f"Scoring output path: {args.score_output}",
]

for line in lines:
    print(line)

# Read test data
test_data = pd.read_csv(args.test_data)
X_test = test_data.iloc[:,:-1]
y_test = test_data.iloc[:,-1]

# Load model
folder = args.model_input
model  = pickle.load(open(f'{folder}/model.pkl', "rb"))
y_pred = model.predict(X_test)

# Dataframe y_test & y_pred
score_output_data = pd.DataFrame(data=np.array([np.array(y_test),y_pred]).T, columns=['y_test','y_predict'])
score_output_data.to_csv(args.score_output, index=False)

