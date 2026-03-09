import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('/workspaces/codespaces-blank/Task_4a_RBSX_data.csv')

#print(df.to_string())

#print(pd.DataFrame(df))


#just change the currency to change the conversion rate 
#currency = 'JPY +IBM- GBP'
#conversion_rate = round(df[currency].iloc[-1],2)
#print("conversion_rate = ", conversion_rate)

myvar=pd.DataFrame(df)
#print(myvar)
#print(df.loc[[0,1]])

df2=pd.DataFrame(df, index=['GBP +AC0- EUR'])
#print(df2)
#print(df2.loc['GBP +AC0- EUR'])
#print(pd.options.display.max_rows)
#print(df.head(60))
#print(df.tail(10))
print(df.info())