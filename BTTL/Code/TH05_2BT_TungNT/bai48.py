import numpy as np

# Giả sử vector_weight là một vector có 100 phần tử
vector_weight = np.arange(1, 101)  # Tạo vector chứa các số từ 1 đến 100

# Chuyển vector_weight thành ma trận kích thước 10x10
matrix_weight = vector_weight.reshape(10, 10)

# In kết quả
print("Vector ban đầu:")
print(vector_weight)

print("\nMa trận kích thước 10x10:")
print(matrix_weight)
