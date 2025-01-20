import numpy as np

# Giả sử vector_weight là một vector kích thước 100
vector_weight = np.arange(1, 101)  # Vector từ 1 đến 100

# Chuyển vector_weight thành ma trận 10x10
weight = vector_weight.reshape(10, 10)
print("Ma trận weight:\n", weight)

# Kiểm tra ma trận weight có nghịch đảo hay không
det_weight = np.linalg.det(weight)  # Tính định thức
print("\nĐịnh thức của ma trận weight:", det_weight)

if det_weight != 0:
    # Tính nghịch đảo của ma trận
    weight_inverse = np.linalg.inv(weight)
    print("\nMa trận nghịch đảo weight^-1:\n", weight_inverse)
else:
    print("\nMa trận weight không có nghịch đảo (định thức = 0).")
