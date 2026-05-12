import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('/workspaces/csv/advanced_data.csv')
df['date'] = pd.to_datetime(df['date'])

print(df.isnull().sum())

df['visitors'] = df['visitors'].fillna(df['visitors'].mean)
df['revenue'] = df['revenue'].fillna(df['revenue'].mean)
df['marketing_spend'] = df['marketing_spend'].fillna(df['marketing_spend'].median)
df = df.dropna(subset= ['orders'])

df['conversion rate'] = 
df['revenue per visitor'] = 
df['profit'] = 