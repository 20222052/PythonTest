import numpy as np

# Đường dẫn tệp tin
path = 'Diem_2A.txt'

try:
    # Đọc dữ liệu từ tệp, bỏ qua dòng tiêu đề
    diem_2a = np.loadtxt(path, delimiter=',', dtype=np.int_, skiprows=1, usecols=(1,))

    # Hiển thị dữ liệu đã đọc
    print("Dữ liệu điểm của lớp:")
    print(diem_2a)

    # Tìm điểm cao nhất và thấp nhất
    max_score = diem_2a.max()
    min_score = diem_2a.min()

    print('Điểm cao nhất của lớp:', max_score)
    print('Điểm thấp nhất của lớp:', min_score)

except FileNotFoundError:
    print(f"Không tìm thấy tệp tin: {path}")
except ValueError as e:
    print(f"Dữ liệu trong tệp không hợp lệ: {e}")
except Exception as e:
    print(f"Đã xảy ra lỗi không mong muốn: {e}")
