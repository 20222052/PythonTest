import numpy as np

# Tạo ma trận A (giống như trong hình)
A = np.array([
    [60, 84, 47, 28, 48, 83, 43],
    [59, 56, 32, 80, 52, 76, 91],
    [6, 15, 21, 4, 94, 67, 5],
    [20, 50, 70, 56, 54, 51, 89],
    [76, 56, 82, 78, 3, 77, 41],
    [74, 5, 27, 35, 90, 20, 14],
    [89, 73, 27, 88, 36, 96, 72],
    [95, 15, 67, 75, 83, 36, 96]
])

# 1. Tạo ma trận với các phần tử trên đường chéo chính, cách 2 dòng phía trên
d_A1 = np.triu(A, 2)
print("Ma trận các phần tử trên cách 2 dòng:")
print(d_A1)

# 2. Tạo ma trận với các phần tử dưới đường chéo chính, cách 3 dòng phía dưới
d_A2 = np.tril(A, -3)
print("\nMa trận các phần tử dưới cách 3 dòng:")
print(d_A2)
