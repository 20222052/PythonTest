import numpy as np

# Đường dẫn tệp tin
path = 'Diem_2A.txt'

try:
    # Đọc dữ liệu từ tệp, bỏ qua dòng tiêu đề
    diem_2a = np.loadtxt(path, delimiter=',', dtype=np.int_, skiprows=1, usecols=(1,))
    a = diem_2a[1,:15]
    print('mang a ban dau: \n', a)
    print('so phan tu trong mang a:', a.size)
    print('mang a da sap xep: \n', np.sort(a,))
    print('gia tri trung binhf:', np.mean(a))
    print('gia tri trung vi:', np.median(a))

except FileNotFoundError:
    print(f"Không tìm thấy tệp tin: {path}")
except ValueError as e:
    print(f"Dữ liệu trong tệp không hợp lệ: {e}")
except Exception as e:
    print(f"Đã xảy ra lỗi không mong muốn: {e}")
