import os
import json
data = os.getenv("input_data")
print(data)
print("Hello welocme to Python Git hub")
record = os.getenv("GITHUB_PATH")
print(record)
home = os.getenv("HOME")
pwd= os.getcwd()
files  = os.listdir()
print(pwd)
print(files)

with open(sample1.json','r') as fil:
     jdata1 = json.load(fil)

print(jdata1)

print('============')

with open(home+'/sample1.json','r') as fil:
     jdata = json.load(fil)

print(jdata)



