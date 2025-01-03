#Bài 5: Thống kê điểm Học Viên
# Danh sách điểm thi môn "Python for Analysis" của lớp AIV_EVNICT
diem_thi = ['A', 'B', 'C', 'A', 'F', 'D', 'B', 'A', 'F', 'C', 'B', 'D', 'F', 'A', 'C']

# 1) Số sinh viên trong lớp
so_sinh_vien = len(diem_thi)
print(f"Số sinh viên trong lớp: {so_sinh_vien}")

# 2) Số sinh viên phải học lại môn này (điểm F)
so_sinh_vien_hoc_lai = diem_thi.count('F')
print(f"Số sinh viên phải học lại môn này: {so_sinh_vien_hoc_lai}")

# 3) Số sinh viên có điểm từ B trở lên (B, A)
so_sinh_vien_b_or_up = sum(1 for diem in diem_thi if diem in ['A', 'B'])
print(f"Số sinh viên có điểm từ B trở lên: {so_sinh_vien_b_or_up}")

# 4) Tạo bảng điểm mới sau khi loại bỏ điểm của sinh viên đầu tiên và cuối cùng
diem_thi_moi = diem_thi[1:-1]  # Loại bỏ sinh viên đầu tiên và cuối cùng
print(f"Bảng điểm mới sau khi loại bỏ sinh viên đầu tiên và cuối cùng: {diem_thi_moi}")

