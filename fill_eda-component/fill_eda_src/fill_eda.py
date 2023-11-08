import argparse
from pathlib import Path
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# obtener parámetros:
parser = argparse.ArgumentParser("fill_eda")
parser.add_argument("--data_set", type=str, help="Dataset file")
parser.add_argument("--data_clean", type=str, help="File containing clean dataset")
parser.add_argument("--pairplot_fig", type=str, help="Folder containing pairplot figure")

args = parser.parse_args()
print("Fill gaps with mean...")

lines = [
    f"data_set: {args.data_set}",
    f"data_clean: {args.data_clean}",
    f"pairplot_fig: {args.pairplot_fig}",
]

print("Parameters: ...")

# Print parameters:
for line in lines:
    print(line)

# Fill and clean dataset
data = pd.read_csv(args.data_set)
data_clean = data.fillna(data.mean())
## Save the output data
data_clean.to_csv(args.data_clean, index=False)

# Create a pair plot
sns.set(style="ticks")
fig = sns.pairplot(data, diag_kind='kde')
plt.suptitle("Pair Plot of Columns")
## Save the output data
output_data = fig.savefig((Path(args.pairplot_fig) / "pairplot.png"))





