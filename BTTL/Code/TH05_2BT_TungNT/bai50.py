import numpy as np

# Giả sử ma trận weight là 10x10
weight = np.array([
    [0, 87, 110, 104, 61, 104, 92, 111, 90, 103],
    [0, 0, 101, 51, 79, 107, 110, 129, 145, 139],
    [0, 0, 0, 139, 67, 64, 95, 62, 159, 152],
    [0, 0, 0, 0, 153,132,114,80,152,81],
    [0, 0, 0, 0, 0, 76,122,111,72,152],
    [0, 0, 0, 0, 0, 0, 92,127,70,88],
    [0, 0, 0, 0, 0, 0, 0, 59,82,136],
    [0, 0, 0, 0, 0, 0, 0, 0, 122,51],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 140],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Tách phần tử đường chéo trên (không bao gồm đường chéo chính)
upper_triangle = np.triu(weight, k=1)

# Tách phần tử đường chéo dưới (không bao gồm đường chéo chính)
lower_triangle = np.tril(weight, k=-1)

# Tìm giá trị lớn nhất của từng phần
max_upper = np.max(upper_triangle)
max_lower = np.max(lower_triangle)

# In kết quả
print("Phần tử lớn nhất trên đường chéo trên:", max_upper)
print("Phần tử lớn nhất dưới đường chéo dưới:", max_lower)
