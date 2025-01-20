import numpy as np

# Giả sử ma trận weight là 10x10
weight = np.array([
    [96,  0,  0,  0,   0,  0,  0,  0,   0,  0],
    [ 0, 80,  0,  0,   0,  0,  0,  0,   0,  0],
    [ 0,  0, 97,  0,   0,  0,  0,  0,   0,  0],
    [ 0,  0,  0, 131,  0,  0,  0,  0,   0,  0],
    [ 0,  0,  0,  0, 126,  0,  0,  0,   0,  0],
    [ 0,  0,  0,  0,   0, 89,  0,  0,   0,  0],
    [ 0,  0,  0,  0,   0,  0, 96,  0,   0,  0],
    [ 0,  0,  0,  0,   0,  0,  0, 90,   0,  0],
    [ 0,  0,  0,  0,   0,  0,  0,  0, 104,  0],
    [ 0,  0,  0,  0,   0,  0,  0,  0,   0, 50]
])

# a) Tạo vector chứa các phần tử trên đường chéo chính
vector_diagonal = np.diag(weight)

# b) Tính trace của ma trận weight
trace = np.trace(weight)

# Kết quả
print("Đường chéo chính của ma trận weight:", vector_diagonal)
print("Trace của ma trận weight:", trace)
