import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("/workspaces/codespaces-blank/Task_4a_RBSX_data.csv")
'''
#df.info()
#df.head()


# get_conversion_rate()
currency = 'GBP +AC0- EUR'
conversion_rate = round(df[currency].iloc[-1],2)
print("conversion_rate = ", conversion_rate)
'''

# df set to date, plus both GBP currency data series
df1 = df[['Date', 'GBP +AC0- EUR', 'GBP +AC0- USD']]
df1['Date'] = pd.to_datetime(df1['Date'],format='%d/%m/%Y')
print(df1)


start_date = '2024-04-01'
end_date = '2024-05-01'

filtered_df = df1[(df1['Date'] >= start_date) & (df1['Date'] <= end_date)]
# plot both GBP currency data series
plt.plot(df1['Date'], df['GBP +AC0- EUR'], marker='o', linestyle='-', color='blue', label='GBP +AC0- EUR')
plt.plot(df1['Date'], df['GBP +AC0- USD'], marker='x', linestyle='-', color='red', label='GBP +AC0- USD')



plt.plot(filtered_df['Date'], filtered_df['GBP +AC0- EUR'], marker='o', linestyle='-', color='purple', label='GBP +AC0- EUR by date')
plt.plot(filtered_df['Date'], filtered_df['GBP +AC0- USD'], marker='x', linestyle='-', color='orange', label='GBP +AC0- USD by date')
plt.legend()

#plt.plot(x, y, color="red")
plt.grid()
subtitle = f"From {start_date} to {end_date}"
plt.title("Date vs Currency conversion"+"\n"+subtitle)
plt.show()

# save plot to image file
plt.savefig("plot.png", dpi=300)