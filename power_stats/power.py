import datetime
import os
import time

import psutil
import pymongo


class PowerStat:
    def __init__(self, cpu, ram_total, ram_use, time):
        self.cpu = cpu
        self.ram_total = ram_total
        self.ram_use = ram_use
        self.time = time

    def __init__(self, cpu, ram_total, ram_use):
        self.cpu = cpu
        self.ram_total = ram_total
        self.ram_use = ram_use
        self.time = datetime.datetime.now()


client = pymongo.MongoClient(os.environ.get('MONGO_CONNECTION'))
collection = client["monitoring"]["power"]

while True:
    if collection.count_documents({}) >= 10000:
        oldest_document = collection.find_one({}, sort=[('date', 1)])
        document_filter = {'_id': oldest_document['_id']}
        collection.delete_one(document_filter)
        print('oldest document removed')
    power = PowerStat(psutil.cpu_percent(), psutil.virtual_memory().total, psutil.virtual_memory().used)
    collection.insert_one(power.__dict__)
    print('Stat saved')
    time.sleep(1)
