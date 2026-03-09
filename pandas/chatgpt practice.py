import pandas as pd 
df=pd.read_csv('customers-1000.csv')
counts=df["Country"].value_counts()
print(counts)