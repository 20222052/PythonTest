import numpy as np

# Đường dẫn tệp tin
path = 'Diem_2A.txt'

try:
    # Đọc dữ liệu từ tệp, bỏ qua dòng tiêu đề
    diem_2a = np.loadtxt(path, delimiter=',', dtype=np.int_, skiprows=1, usecols=(1,))
    print('diem trung binh cua ca lop 2A:', diem_2a.mean())
    for i in range(0,diem_2a.shape[1]):
        print('diem trung binh cua hoc sinh',i,':', diem_2a[:,i].mean())

except FileNotFoundError:
    print(f"Không tìm thấy tệp tin: {path}")
except ValueError as e:
    print(f"Dữ liệu trong tệp không hợp lệ: {e}")
except Exception as e:
    print(f"Đã xảy ra lỗi không mong muốn: {e}")
