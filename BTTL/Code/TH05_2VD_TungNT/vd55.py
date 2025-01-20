import numpy as np

# Dữ liệu vector v_height (đơn vị cm)
a = np.array([
    [9, 4,19,1,18],
    [15,11,1,9,14],
    [17,8,4,10,13]
])
b = np.array([
    [13,8,9,13],
    [17,11,4,3],
    [13,7,2,18],
    [12,1,7,2],
    [1,13,6,4],
])
multi_ab = np.dot(a,b)
print(multi_ab)