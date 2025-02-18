import numpy as np
diem_2a = np.array([
    [3, 5, 3, 10, 9, 1, 9, 8, 3, 1],  # Điểm của học sinh thứ nhất
    [3, 1, 5, 7, 3, 5, 4, 1, 6, 4]    # Điểm của học sinh thứ hai
])

# Truy xuất điểm các môn của học sinh thứ 6
diem_hs5 = diem_2a[:, 5]
print("Điểm các môn của học sinh thứ 6:", diem_hs5)

# Truy xuất điểm của môn học cuối cùng của tất cả học sinh
diem_mon = diem_2a[:, -1]
print("Điểm môn học cuối cùng của tất cả học sinh:\n", diem_mon)

# Truy xuất bảng điểm 5 môn học đầu tiên của 10 học sinh đầu tiên
diem5_hs10 = diem_2a[:10, :5]
print("Bảng điểm 5 môn học đầu tiên của 10 học sinh đầu của lớp:\n", diem5_hs10)
