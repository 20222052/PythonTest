import numpy as np

# Câu 1: Tính hạng của ma trận
matrix_1 = np.array([
    [1, 2, 3],
    [2, 2, 2],
    [3, 3, 3]
])
rank_1 = np.linalg.matrix_rank(matrix_1)
print(f"Hạng của ma trận câu 1: {rank_1}")  # Kết quả: 2

# Câu 2: Tính hạng của ma trận khi định thức bằng 0
matrix_2 = np.array([
    [1, 2, 3],
    [3, 4, 5],
    [4, 5, 6]
])
det_2 = np.linalg.det(matrix_2)
rank_2 = np.linalg.matrix_rank(matrix_2)
print(f"Định thức của ma trận câu 2: {det_2:.2f}")  # Kết quả: 0
print(f"Hạng của ma trận câu 2: {rank_2}")  # Kết quả: 2

# Câu 3: Tính hạng của ma trận chứa các giá trị giống nhau
matrix_3 = np.array([
    [10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10]
])
rank_3 = np.linalg.matrix_rank(matrix_3)
print(f"Hạng của ma trận câu 3: {rank_3}")  # Kết quả: 1
