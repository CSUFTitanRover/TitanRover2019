import numpy as np

# New array filled with val of dtype
''' Example 
np.full((4, 3), -1)
    [[-1. -1. -1.]
    [-1. -1. -1.]
    [-1. -1. -1.]
    [-1. -1. -1.]]'''
def create_array(dimx = 1, dimy = 1, val = 0):#create_array(self, dimx, dimy, val):
    return np.full((dimy, dimx), val)

def getx():
    return (self[0].size)

def gety(self):
    return (self[0].size)

# Add set val to existing array
''' Example
    np.insert(gps_arr, gps_arr[0].size , 2, axis=0) 
    [[-1. -1. -1.]
        [-1. -1. -1.]
        [-1. -1. -1.]
        [ 2.  2.  2.]]'''
def add_base_array(self, val):
    self = np.insert(self, self.getx(), val, axis=0)

''' Example
    np.insert(gps_arr, gps_arr[0].size , 2, axis=1) 
    [[-1. -1. -1.  2.]
        [-1. -1. -1.  2.]
        [-1. -1. -1.  2.]]'''
def extend_array(self, val):
    self = np.insert(self, self.gety(), val, axis=1)

#temp_arr = np.full((1 ,gps_arr[0].size), -1 )
#temp_arr = np.insert(temp_arr,1, gps_arr, axis=0)
'''[[-1. -1. -1.]
    [-1. -1. -1.]
    [-1. -1. -1.]
    [-1. -1. -1.]]'''
#print(temp_arr)
#print(gps_arr)

def main():
    pass

if __name__ == '__main__':
    main()
