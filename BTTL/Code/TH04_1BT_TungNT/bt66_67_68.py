import numpy as np
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file Diamonds.txt vào mảng numpy
data_diamond = np.loadtxt('./BTTL/Code/TH04_1BT_TungNT/data.txt')
# Thông tin về mảng data_diamond
print(data_diamond)
print(f"Kích thước biến data_diamond: {data_diamond.shape}")
print(f"Số chiều của biến data_diamond: {data_diamond.ndim}")
print(f"Kiểu dữ liệu của các phần tử: {data_diamond.dtype}")
print(f"Số phần tử: {data_diamond.size}")

# Yêu cầu 2: Tách thành 2 vector: trọng lượng (carat) và giá bán ($)
diamond_size = data_diamond[:, 0]  # Cột 0: Trọng lượng
diamond_price = data_diamond[:, 1]  # Cột 1: Giá bán

print(diamond_size)
print(diamond_price)

# Yêu cầu 3: Vẽ đồ thị và tính hệ số tương quan
# Vẽ đồ thị
plt.figure(figsize=(8, 6))
plt.scatter(diamond_size, diamond_price, color='blue', alpha=0.7, label='Dữ liệu')
plt.title("Mối quan hệ giữa kích thước và giá bán kim cương")
plt.xlabel("Kích thước (carat)")
plt.ylabel("Giá bán ($)")
plt.grid(True)
plt.legend()
plt.show()

# Tính hệ số tương quan giữa kích thước và giá bán
correlation_coefficient = np.corrcoef(diamond_size, diamond_price)[0, 1]
print(f"Hệ số tương quan giữa kích thước và giá bán kim cương: {correlation_coefficient:.2f}")