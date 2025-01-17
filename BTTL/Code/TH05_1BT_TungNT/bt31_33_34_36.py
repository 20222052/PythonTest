# Tạo file dữ liệu mẫu Data_BMI.txt với 100 dòng dữ liệu gồm chiều cao và cân nặng.
import random

# Đường dẫn file
file_path = "./BTTL/Code/TH05_1BT_TungNT/Data_BMI.txt"

v_height = []
v_weight = []

# Đọc file và tách dữ liệu
with open(file_path, "r") as file:
    for line in file:
        height, weight = map(int, line.strip().split(" "))
        v_height.append(height)
        v_weight.append(weight)

# Hiển thị dữ liệu
print("v_height:", v_height)
print("v_weight:", v_weight)


# Tạo vector v_height_m2
v_height_m2 = [(h / 100) ** 2 for h in v_height]

# Hiển thị kết quả
print("v_height_m2:", v_height_m2)

# Tính chỉ số BMI và lưu vào vector v_bmi
v_bmi = [round(weight / height_m2, 1) for weight, height_m2 in zip(v_weight, v_height_m2)]

# Hiển thị kết quả
print("v_bmi:", v_bmi)


# Khởi tạo bộ đếm cho từng mức BMI
categories = {
    "Underweight": 0,
    "Normal": 0,
    "Overweight": 0,
    "Obese": 0,
    "Extremely Obese": 0,
}

# Phân loại BMI
for bmi in v_bmi:
    if bmi < 18.5:
        categories["Underweight"] += 1
    elif 18.5 <= bmi < 25:
        categories["Normal"] += 1
    elif 25 <= bmi < 30:
        categories["Overweight"] += 1
    elif 30 <= bmi < 35:
        categories["Obese"] += 1
    else:  # bmi >= 35
        categories["Extremely Obese"] += 1

# Hiển thị kết quả thống kê
print("Thống kê BMI:")
for category, count in categories.items():
    print(f"{category}: {count}")
