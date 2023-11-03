import json

import requests

# print("Cancer")
# url = 'http://127.0.0.1:5000/cancer'
# x = [17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]
# r = requests.post(url, json=x)
# print(r.content)
#
# print("MNIST")
# url = 'http://127.0.0.1:5000/mnist'
# with open("data/mnist/mnist_0.json") as f:
#     x = json.load(f)
# r = requests.post(url, json=x)
# print(r.content)

print("Cancer TF")
url = 'http://127.0.0.1:5001/cancer'
x = [17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]
r = requests.post(url, json=x)
print(r.content)

print("Mug")
url = 'http://127.0.0.1:5001/imagenet'
path = "data/img/mug.jpg"
files = {'image': open(path, 'rb')}
r = requests.post(url, files=files)
print(r.content)

print("MNIST TF")
url = 'http://127.0.0.1:5001/mnist'
with open("data/mnist/mnist_0.json") as f:
    x = json.load(f)
r = requests.post(url, json=x)
print(r.content)

print("Pets")
url = 'http://127.0.0.1:5001/pets'
path = "data/dogsvscats/large/validation/cats/cat.1000.jpg"
files = {'image': open(path, 'rb')}
r = requests.post(url, files=files)
print(r.content)

print("Drivers")
url = 'http://127.0.0.1:5001/drivers'
path = "data/drivers/img_1.jpg"
files = {'image': open(path, 'rb')}
r = requests.post(url, files=files)
print(r.content)

#
# #docker compose up --build
# #Si bug de build docker build .

# Driver
# Noise
# AE