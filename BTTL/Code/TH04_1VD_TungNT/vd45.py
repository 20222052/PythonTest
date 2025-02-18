import numpy as np
from scipy import stats

# Đọc dữ liệu, thay giá trị trống bằng 0
path = 'Diem_2A.txt'
diem_2a = np.genfromtxt(path, delimiter=',', dtype=np.int_, skip_header=1, filling_values=0)

# Lặp qua từng cột từ cột thứ 2 trở đi
for i in range(1, diem_2a.shape[1]):
    a = stats.mode(diem_2a[:, i], keepdims=True)  # Tính mode cho cột i
    print(f'Môn {i}: Điểm xuất hiện nhiều nhất: {a.mode[0]}, Số lần: {a.count[0]}')

# In kiểu dữ liệu của mode
print(type(a))
