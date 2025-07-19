import numpy as np

arr=np.array([[2,3,4], # row=0
              [5,6,7], # row=1
              [8,9,10]]) # row=2
print(arr[0:2],arr[1:2]) 

print(arr[0:2,0:2]) # Rows= 1 and 2, Columns=1 and 2


total_sum=arr[1].sum() 
print(total_sum)

