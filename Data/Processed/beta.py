import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("./Data/Processed/beta_lap.csv", header=None)
print(data.shape)
sns.heatmap(data.values)
plt.savefig("1.png")