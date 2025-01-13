import numpy as np

# Đọc dữ liệu từ file và lưu vào numpy array
data = np.loadtxt('./BTTL/Code/TH04_1BT_TungNT/temp.txt')

# Yêu cầu 2: Tính Max, Min, và Nhiệt độ trung bình của cả 6 thành phố
max_temp_all = np.max(data)
min_temp_all = np.min(data)
mean_temp_all = np.mean(data)

print(data)

print("Yêu cầu 2:")
print(f"Nhiệt độ cao nhất (Max) của cả 6 thành phố: {max_temp_all:.2f}")
print(f"Nhiệt độ thấp nhất (Min) của cả 6 thành phố: {min_temp_all:.2f}")
print(f"Nhiệt độ trung bình của cả 6 thành phố: {mean_temp_all:.2f}")

# Yêu cầu 3: Tính Max, Min, và Nhiệt độ trung bình của từng thành phố
print("\nYêu cầu 3:")
city_names = ["Hà Nội", "Vinh", "Đà Nẵng", "Nha Trang", "HCM", "Cà Mau"]

for i, city in enumerate(city_names):
    max_temp_city = np.max(data[:, i])
    min_temp_city = np.min(data[:, i])
    mean_temp_city = np.mean(data[:, i])

    print(f"{city}:")
    print(f"  - Nhiệt độ cao nhất (Max): {max_temp_city:.2f}")
    print(f"  - Nhiệt độ thấp nhất (Min): {min_temp_city:.2f}")
    print(f"  - Nhiệt độ trung bình: {mean_temp_city:.2f}")
