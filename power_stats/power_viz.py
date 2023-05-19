import os

import pymongo
import matplotlib.pyplot as plt

client = pymongo.MongoClient(os.environ.get('MONGO_CONNECTION'))
collection = client['monitoring']['power']
data = list(collection.find())
cpu = [item['cpu'] for item in data]
time = [item['time'] for item in data]

plt.plot(time, cpu)
plt.xlabel('Timestamp')
plt.ylabel('CPU Usage')
plt.title('CPU Usage Over Time')
plt.savefig('power.png')
