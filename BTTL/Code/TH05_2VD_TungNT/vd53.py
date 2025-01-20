import numpy as np

# Dữ liệu vector v_height (đơn vị cm)
a = np.array([
    [9, 4,19,1,18],
    [15,11,1,9,14],
    [17,8,4,10,13]
])
b = np.array([
    [9, 4,19,1,18],
    [15,11,1,9,14],
    [17,8,4,10,13]
])
equal_ab = np.equal(a,b)
print(equal_ab)