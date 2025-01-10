import numpy as np # type: ignore

# Phương thức arange(a, b, steps):
# Tạo vector:
# - Phần tử đầu tiên = a,
# - Kết thúc < b,
# - Mỗi phần tử cách nhau một khoảng = steps
d = np.arange(1, 15, 2)
print("Vector d:", d)
print("Số phần tử của vector d:", d.size)

print()

# Phương thức linspace(a, b, num):
# Tạo vector:
# - Phần tử đầu tiên = a,
# - Phần tử cuối = b,
# - Số phần tử của ma trận = num
f = np.linspace(1, 15, 11)
print("Vector f:", f)
print("Số phần tử của vector f:", f.size)
