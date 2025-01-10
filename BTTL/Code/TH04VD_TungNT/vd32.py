import numpy as np

# Tạo mảng 2 chiều đúng cách
diem_2a = np.array([
    [3, 5, 3, 10, 9, 1, 9, 8, 3, 1],  # Điểm của học sinh thứ nhất
    [3, 1, 5, 7, 3, 5, 4, 1, 6, 4]    # Điểm của học sinh thứ hai
])

# Truy xuất thông tin theo yêu cầu
print('Điểm môn học đầu tiên, của học sinh đầu tiên:', diem_2a[0, 0])
print('Điểm môn học thứ 1, của học sinh thứ 3:', diem_2a[1, 3])
print('Điểm môn cuối cùng, của học sinh cuối cùng:', diem_2a[-1, -1])
print('---------------')
print('Bảng điểm lớp 2A:\n', diem_2a)
