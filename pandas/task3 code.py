import pandas as pd 
df =pd.read_csv('/workspaces/codespaces-blank/Task3_data.csv')
counts=df["Issue Type"].value_counts()
print(counts)