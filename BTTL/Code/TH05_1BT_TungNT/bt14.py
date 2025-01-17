import numpy as np

# Tạo vector a từ 1 đến 30
a = np.arange(1, 31)

# Tách các vector con
a_le = a[a % 2 != 0]  # Các phần tử là số lẻ
a_chan = a[a % 2 == 0]  # Các phần tử là số chẵn
a_3 = a[a % 3 == 0]  # Các phần tử chia hết cho 3

# In kết quả
print("Vector gốc (a):", a)
print("Vector lẻ (a_le):", a_le)
print("Vector chẵn (a_chan):", a_chan)
print("Vector chia hết cho 3 (a_3):", a_3)
