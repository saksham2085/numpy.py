""" 
np.insert(array,index,value,asix = none)
array - original array
index- posiion number at which new value will be inserted
value-actual data to be inserted
axis- if it is none then it is inserted into a flatten array
axis = 0, row-wise
axis = 1, column-wise
"""
import numpy as np
arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr,2,100)
print(new_arr)