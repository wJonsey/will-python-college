import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('DHT11_log.csv')

x = data["Timestamp"] 
y1 = data['Temperature']
y2 = data['Humidity']

plt.plot (x,y1, label = 'Temperature'   )
plt.plot (x,y2, label = 'Humidity'    )
plt.xlabel('Timestamp')
plt.suptitle('DHT11 Sensor Data')

plt.legend()
plt.savefig('Dht11_graph.png')
plt.show()
