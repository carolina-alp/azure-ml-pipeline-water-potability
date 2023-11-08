import argparse
from pathlib import Path
from datetime import datetime
import pandas as pd
from sklearn.metrics import classification_report


parser = argparse.ArgumentParser("score")
parser.add_argument("--scoring_result", type=str, help="Path of scoring result")
parser.add_argument("--eval_output", type=str, help="Path of output evaluation result")

args = parser.parse_args()

lines = [
    f"Scoring result path: {args.scoring_result}",
    f"Evaluation output path: {args.eval_output}",
]

for line in lines:
    print(line)

# Read test and prediction data
data   = pd.read_csv(args.scoring_result)
y_test = data.iloc[:,0]
y_pred = data.iloc[:,1]

# Performance 
output = classification_report(y_test, y_pred,target_names=["Not Potable", "Potable"], output_dict=True)
df_rep = pd.DataFrame(output).transpose()
df_rep.to_csv(Path(args.eval_output) / "report.csv")

