import numpy as np

# Đọc dữ liệu từ tệp
with open("./Diem_2A.txt", "r", encoding="utf-8") as file:
    data = file.read()

# Chuyển đổi dữ liệu thành mảng số
data_lines = data.strip().split("\n")
scores = [list(map(float, line.split(",")[:-1])) for line in data_lines]

# Chuyển đổi thành numpy array để dễ tính toán
scores_array = np.array(scores)

# 1. Sinh viên có điểm đồng đều nhất và lệch nhất
std_per_student = np.std(scores_array, axis=1)  # Độ lệch chuẩn theo từng học sinh

# Sinh viên có độ lệch chuẩn nhỏ nhất (đồng đều nhất)
min_std_student = np.min(std_per_student)
student_with_min_std = np.argmin(std_per_student) + 1  # Chỉ số bắt đầu từ 1

# Sinh viên có độ lệch chuẩn lớn nhất (lệch nhất)
max_std_student = np.max(std_per_student)
student_with_max_std = np.argmax(std_per_student) + 1  # Chỉ số bắt đầu từ 1

# 2. Môn học có điểm đồng đều nhất và lệch nhất
std_per_subject = np.std(scores_array, axis=0)  # Độ lệch chuẩn theo từng môn học

# Môn học có độ lệch chuẩn nhỏ nhất (đồng đều nhất)
min_std_subject = np.min(std_per_subject)
subject_with_min_std = np.argmin(std_per_subject) + 1  # Chỉ số bắt đầu từ 1

# Môn học có độ lệch chuẩn lớn nhất (lệch nhất)
max_std_subject = np.max(std_per_subject)
subject_with_max_std = np.argmax(std_per_subject) + 1  # Chỉ số bắt đầu từ 1

# Hiển thị kết quả
print(f"Sinh viên có điểm đồng đều nhất: Sinh viên {student_with_min_std} (Độ lệch chuẩn = {min_std_student:.2f})")
print(f"Sinh viên có điểm lệch nhất: Sinh viên {student_with_max_std} (Độ lệch chuẩn = {max_std_student:.2f})")

print(f"Môn học có điểm đồng đều nhất: Môn {subject_with_min_std} (Độ lệch chuẩn = {min_std_subject:.2f})")
print(f"Môn học có điểm lệch nhất: Môn {subject_with_max_std} (Độ lệch chuẩn = {max_std_subject:.2f})")
