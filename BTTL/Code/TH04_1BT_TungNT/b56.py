import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu
square_feet = [1900, 2100, 2500, 1800, 2200, 2300, 2900]
distance = [1, 2, 3, 4, 5, 6, 7]
prices = [328, 340, 385, 299, 355, 362, 420]

# Tính hệ số tương quan
corr_size_price = np.corrcoef(square_feet, prices)[0, 1]
corr_distance_price = np.corrcoef(distance, prices)[0, 1]

# Vẽ biểu đồ
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Biểu đồ diện tích vs giá bán
axs[0].scatter(square_feet, prices, color='blue', alpha=0.7)
axs[0].set_xlabel("Diện tích (square feet)")
axs[0].set_ylabel("Giá bán (nghìn USD)")
axs[0].set_title(f"Diện tích vs Giá bán\nHệ số tương quan: {corr_size_price:.2f}")

# Biểu đồ khoảng cách vs giá bán
axs[1].scatter(distance, prices, color='red', alpha=0.7)
axs[1].set_xlabel("Khoảng cách (miles)")
axs[1].set_ylabel("Giá bán (nghìn USD)")
axs[1].set_title(f"Khoảng cách vs Giá bán\nHệ số tương quan: {corr_distance_price:.2f}")

plt.tight_layout()
plt.show()
