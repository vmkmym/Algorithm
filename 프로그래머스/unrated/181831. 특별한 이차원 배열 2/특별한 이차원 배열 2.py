import numpy as np

def solution(arr):
    np_arr = np.array(arr)
    
    transpose_arr = np_arr.T
    
    if np.array_equal(np_arr, transpose_arr):
        return 1
    else:
        return 0
