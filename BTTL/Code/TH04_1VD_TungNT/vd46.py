import numpy as np

# Đường dẫn đến file
path = 'Diem_2A.txt'

# Đọc dữ liệu từ cột thứ 2 (index = 1)
diem_2a = np.loadtxt(path, delimiter=',', dtype=np.int_, skiprows=1, usecols=(1,))

# Tính độ chênh lệch điểm
do_chenh_lech = diem_2a.max() - diem_2a.min()
print('Độ chênh lệch điểm của học sinh:', do_chenh_lech)
