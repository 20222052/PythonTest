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
sum_ab = np.add(a,b)
print(sum_ab)
sub_ab = np.subtract(a,b)
print(sub_ab)