import numpy as np
import os  # Để kiểm tra sự tồn tại của tệp

# Đường dẫn tới tệp
path = './Diem_2A.txt'

# Kiểm tra xem tệp có tồn tại hay không
if os.path.exists(path):
    try:
        # Đọc dữ liệu từ tệp, thay giá trị trống bằng 0
        diem_2a = np.genfromtxt(path, delimiter=',', dtype=np.int32, filling_values=0)

        # In thông tin về mảng
        print("Dữ liệu trong mảng diem_2a:")
        print(diem_2a)
        print("Kiểu dữ liệu của phần tử trong mảng diem_2a:", diem_2a.dtype)
        print("Kích thước của mảng diem_2a:", diem_2a.shape)
        print("Số phần tử của mảng diem_2a:", diem_2a.size)
        print("Số chiều của mảng diem_2a:", diem_2a.ndim)
    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc tệp: {e}")
else:
    print(f"Tệp không tồn tại tại đường dẫn: {path}")
