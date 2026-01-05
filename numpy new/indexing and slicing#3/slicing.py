"""
slicing
array[start:stop:step]
arr[start:end] ,start to end -1
"""

import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[1:5]) #index 1 to 4
print(arr[:4]) #index 0 to 3
print(arr[::2]) #index with 1 gap from 0
print(arr[::-1]) #start from last element