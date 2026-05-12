import pandas as pd 
import matplotlib.pyplot as plt 


df=pd.read_csv('/workspaces/csv/tlelve.csv')

#datetime
df['date'] = pd.to_datetime(df['date'])

#cleaning data
df["visitors"] = df["visitors"].fillna(df["visitors"].mean())
df = df.dropna(subset=["orders"])
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["revenue"] = df["revenue"].fillna(df["revenue"].mean())

df['conversion rate'] = df['visitors'] / df['orders']

#Total revenue
total_revenue = df['revenue'].sum()

print('Toral revenue is',total_revenue)

#Average daily visitors

average_visitors = df['visitors'].mean()

print('Average daily visitors is', average_visitors)

#Day with highest revenue
max_row = df.loc[df['revenue'].idxmax()]

print('Highest revenue was', max_row['revenue'], 'on', max_row['date'])



#Line chart revenue over time

plt.plot(df['date'],df['revenue'])
plt.xticks(rotation=45)
plt.xlabel('date')
plt.ylabel('revenue')
plt.savefig('Line chart revenue over time.png')
plt.show()

#Bar chart total orders per week


plt.bar(df['date'],df['orders'])
plt.xticks(rotation=45)
plt.xlabel('date')
plt.ylabel('orders')
plt.savefig('Bar chart total orders per week.png')
plt.show()

#Scatter plot visitors vs revenue


plt.scatter(df["visitors"], df["revenue"], color="purple")

plt.xlabel("Visitors")
plt.ylabel("Revenue")
plt.title("Visitors vs Revenue")
plt.savefig('Scatter plot visitors vs revenue.png')
plt.show()