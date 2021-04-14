# Sorting Numpy arrays
import numpy as np

def sort_numpy_array(inp_array):
    return np.sort(inp_array)

if __name__ == "__main__":
    inp_list = [np.array([3,2,3]),np.array([5,3,6,2,6])]
    for inp in inp_list:
        print(" Sorted array for {0}  is {1}".format(inp,sort_numpy_array(inp)))
