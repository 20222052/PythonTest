import numpy as np

# Đọc dữ liệu từ tệp
with open("./Diem_2A.txt", "r", encoding="utf-8") as file:
    data = file.read()

# Chuyển đổi dữ liệu thành mảng số
data_lines = data.strip().split("\n")
scores = [list(map(float, line.split(",")[:-1])) for line in data_lines]

# Chuyển đổi thành numpy array để dễ tính toán
scores_array = np.array(scores)

# 1. ĐTB của từng học sinh
average_scores = np.mean(scores_array, axis=1)

# 2. Học sinh có điểm TB cao nhất
max_average_score = np.max(average_scores)
student_with_max_average = np.argmax(average_scores) + 1  # Chỉ số bắt đầu từ 1

# 3. Học sinh có điểm TB thấp nhất
min_average_score = np.min(average_scores)
student_with_min_average = np.argmin(average_scores) + 1  # Chỉ số bắt đầu từ 1

# Hiển thị kết quả
print("Điểm trung bình của từng học sinh:", average_scores)
print(f"Học sinh có điểm trung bình cao nhất: Học sinh {student_with_max_average} (ĐTB = {max_average_score:.2f})")
print(f"Học sinh có điểm trung bình thấp nhất: Học sinh {student_with_min_average} (ĐTB = {min_average_score:.2f})")
