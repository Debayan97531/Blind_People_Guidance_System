# import json

# f = open("loc.json")
# data = json.load(f)

# # print(data['location'][0])
# for i in range(20):
#     data['location'][0] = data['location'][0]+i/100
#     data['location'][1] = data['location'][1]+i/100
#     print(data['location'][0])

#     out_file = open("loc.json","w")
#     json.dump(data, out_file)

import requests
import random

count = 1
lat = 87
lon = 22
# maximum distance to change coordinates
max_distance = 0.01

while True:
    # ret, frame = self.vid.read()
    # topic = self.socket.recv_string()
    # gnss = self.socket.recv_pyobj()
    # lat, lon = GNSSparser(gnss["gnss"])
    # generate random distance for latitude and longitude
    lat_diff = random.uniform(-max_distance, max_distance)
    lon_diff = random.uniform(-max_distance, max_distance)
    
    # update the coordinates
    lat += 10
    lon += lon_diff
    print(f"final gnss : {lat}, {lon}")
    requests.post(f"http://192.168.0.100:5000/update/{lat}/{lon}", data = None)