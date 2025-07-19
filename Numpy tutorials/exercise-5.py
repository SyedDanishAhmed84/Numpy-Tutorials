import numpy as np

arr=np.array([[1,4,6],
              [2,5,8],
              [3,6,7]])

row_addition=arr.sum(axis=1)
print(f"Row wise addition : ,{row_addition}")

column_addtion=arr.sum(axis=0)
print(f"Column wise addition : {column_addtion}")