import numpy as np
a_giohoc = np.array([4,7,1,2,8,0,3,8,6])
b_diem = np.array([7,9,3,4,9,0,5,10,8])
co = np.corrcoef(a_giohoc,b_diem)
print(type(co))
print('he so tuong quan:', co)