import numpy as np

arr=np.arange(10)

print("Starting 5 elements : ",arr[:5])
print("Last 3 elements : ",arr[-3:])
print("Every second element : ",arr[::2])
print("1 element gap : ",arr[0:2:1])
print("5 elements gap : ",arr[0:10:5])