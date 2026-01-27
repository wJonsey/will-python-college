import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
df = pd.read_csv("Task_4a_RBSX_data.csv")
 
#df.info()
 
df.head()
 
 
# get_conversion_rate()
currency = 'GBP +AC0- EUR'
conversion_rate = round(df[currency].iloc[-1],2)
print("conversion_rate = ", conversion_rate)
 
df1 = df[['Date', 'USD +AC0- GBP', 'GBP +AC0- USD']]
print(df1.head())
plt.plot(df1['USD +AC0- GBP'], label='USD +AC0- GBP')
plt.plot(df1['GBP +AC0- USD'], label='GBP +AC0- USD')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.savefig('exchange_rates.png')
print("Chart saved to exchange_rates.png")