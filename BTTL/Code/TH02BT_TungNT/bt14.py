#Bài 14:Tìm max - min - mean
# Khởi tạo danh sách chiều cao (dữ liệu mẫu)
student_heights = [1.65, 1.70, 1.80, 1.55, 1.60, 1.75, 1.68, 1.72]

# 1. Chiều cao cao nhất và thấp nhất
max_height = max(student_heights)
min_height = min(student_heights)

# 2. Chiều cao trung bình
average_height = sum(student_heights) / len(student_heights)

# 3. Số lượng sinh viên có chiều cao >= chiều cao trung bình
above_average_count = sum(1 for height in student_heights if height >= average_height)

# Hiển thị kết quả
print(f"Chiều cao cao nhất trong lớp: {max_height:.2f} m")
print(f"Chiều cao thấp nhất trong lớp: {min_height:.2f} m")
print(f"Chiều cao trung bình của lớp: {average_height:.2f} m")
print(f"Số lượng sinh viên có chiều cao lớn hơn hoặc bằng trung bình: {above_average_count}")


