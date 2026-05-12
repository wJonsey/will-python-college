import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('sales.csv')


plt.bar(df['Date'],df['Units_Sold'])

plt.savefig('practice4.png')
plt.show()
plt.clf()

