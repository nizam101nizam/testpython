import os
data = os.getenv("input_data")
print(data)
print("Hello welocme to Python Git hub")
record = os.getenv("GITHUB_ENV")
print(record)
home = os.getenv("HOME")
pwd= os.getcwd()
files  = os.listdir()
print(pwd)
print(files)
