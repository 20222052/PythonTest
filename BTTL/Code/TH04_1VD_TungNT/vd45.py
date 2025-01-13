import numpy as np
from scipy import stats

# Đọc toàn bộ dữ liệu, bỏ qua cột đầu tiên (ID)
path = 'Diem_2A.txt'
diem_2a = np.loadtxt(path, delimiter=',', dtype=np.int_, skiprows=1)

# Lặp qua từng cột từ cột thứ 2 trở đi
for i in range(1, diem_2a.shape[1]):
    a = stats.mode(diem_2a[:, i])  # Tính mode cho cột i
    print(f'Môn {i}: Điểm xuất hiện nhiều nhất: {a.mode[0]}, Số lần: {a.count[0]}')

# In kiểu dữ liệu của mode
print(type(a))
