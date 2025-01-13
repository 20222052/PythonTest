import numpy as np

# Đọc dữ liệu từ tệp
with open("./Diem_2A.txt", "r", encoding="utf-8") as file:
    data = file.read()

# Chuyển đổi dữ liệu thành mảng số
data_lines = data.strip().split("\n")
scores = [list(map(float, line.split(",")[:-1])) for line in data_lines]

# Chuyển đổi thành numpy array để dễ tính toán
scores_array = np.array(scores)

# 1. ĐTB của từng môn học (theo cột)
average_scores_per_subject = np.mean(scores_array, axis=0)

# 2. Môn học có điểm TB cao nhất
max_average_score_subject = np.max(average_scores_per_subject)
subject_with_max_average = np.argmax(average_scores_per_subject) + 1  # Chỉ số bắt đầu từ 1

# 3. Môn học có điểm TB thấp nhất
min_average_score_subject = np.min(average_scores_per_subject)
subject_with_min_average = np.argmin(average_scores_per_subject) + 1  # Chỉ số bắt đầu từ 1

# Hiển thị kết quả
print("Điểm trung bình của từng môn học:", average_scores_per_subject)
print(f"Môn học có điểm trung bình cao nhất: Môn {subject_with_max_average} (ĐTB = {max_average_score_subject:.2f})")
print(f"Môn học có điểm trung bình thấp nhất: Môn {subject_with_min_average} (ĐTB = {min_average_score_subject:.2f})")
