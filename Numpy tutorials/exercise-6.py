import numpy as np

arr=np.array([[[2,3],
               [4,5]],
             [ [5,6],
              [7,8]
              ]])


arr0=arr[0]
print(arr0)
arr1=arr[0,1,1]
print(arr1)
arr2=arr[1,0,1]
print(arr2)
arr_1=arr[0:1:1]
print(arr_1)
print(arr[0])
print(arr[0:1])
print(arr[0:1:3])
print(arr[1])
