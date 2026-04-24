import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('/workspaces/csv/random_weather_energy_data.csv')
df["Timestamp"] = pd.to_datetime(df["date"])
df = df.sort_values("Timestamp")

xpoints = df['Timestamp']
ypoints =  df['temperature']








plt.plot(xpoints,ypoints)
plt.show()
plt.savefig('temperature vs humidity.png')