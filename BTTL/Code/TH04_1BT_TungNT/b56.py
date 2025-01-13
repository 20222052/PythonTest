import numpy as np

# Dữ liệu từ bảng số liệu (thay thế với số liệu của bạn)
square_feet = [1900, 2100, 2500, 1800, 2200, 2300, 2900]
distance = [1, 2, 3, 4, 5, 6, 7]
prices = [328, 340, 385, 299, 355, 362, 420]

# 1. Tính hệ số tương quan giữa diện tích và giá bán nhà
corr_size_price = np.corrcoef(square_feet, prices)[0, 1]

# 2. Tính hệ số tương quan giữa khoảng cách và giá bán nhà
corr_distance_price = np.corrcoef(distance, prices)[0, 1]

# Hiển thị kết quả
print(f"Hệ số tương quan giữa diện tích và giá bán nhà: {corr_size_price:.2f}")
print(f"Hệ số tương quan giữa khoảng cách và giá bán nhà: {corr_distance_price:.2f}")
