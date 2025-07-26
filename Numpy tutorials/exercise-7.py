import numpy as np

a=np.array([1,2,3,4])
mask=a>2
print(a[mask])

b=np.array([1,3,5,6])
c=np.where(b%2==0,"even","odd")
print(c)