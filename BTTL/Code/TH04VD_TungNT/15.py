import numpy as np
c = np.array([[(2,4,0,6),(4,7,5,6)],[(0,3,2,1),(9,4,5,6)],[(5,8,6,4),(1,4,6,8)]])
print(c)
print('loai du lieu cua bien c:', c[0,0,0])
print('kieu du lieu cua phan tu trong mang c:', c.dtype)
print('kich thuoc cua mang c:', c.shape)
print('so phan tu trong mang c:', c.size)
print('so chieu cua mang c:', c.ndim)