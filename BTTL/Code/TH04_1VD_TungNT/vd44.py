import numpy as np

# Đường dẫn tệp tin
path = 'Diem_2A.txt'

try:
    # Đọc nội dung file
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read().strip().replace('\n', '').split(',')
    
    # Loại bỏ khoảng trắng, chuyển thành số nguyên
    diem_2a = np.array([int(x.strip()) for x in data if x.strip()], dtype=np.int_)

    # Kiểm tra dữ liệu
    print('Dữ liệu đọc được:\n', diem_2a)
    
    # Lấy 15 phần tử đầu tiên nếu có đủ dữ liệu
    a = diem_2a[:15]
    
    print('Mảng a ban đầu:\n', a)
    print('Số phần tử trong mảng a:', a.size)
    print('Mảng a đã sắp xếp:\n', np.sort(a))
    print('Giá trị trung bình:', np.mean(a))
    print('Giá trị trung vị:', np.median(a))

except FileNotFoundError:
    print(f"Không tìm thấy tệp tin: {path}")
except ValueError as e:
    print(f"Dữ liệu trong tệp không hợp lệ: {e}")
except Exception as e:
    print(f"Đã xảy ra lỗi không mong muốn: {e}")
