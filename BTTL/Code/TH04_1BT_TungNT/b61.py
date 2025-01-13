import numpy as np

# Đọc dữ liệu từ file Temp.txt
try:
    data_numpy = np.loadtxt('Temp.txt', delimiter=',')  # Đọc dữ liệu với dấu phẩy làm dấu phân cách

    # Lấy thông tin về kích thước, số chiều, kiểu dữ liệu và số phần tử
    shape = data_numpy.shape          # Kích thước của mảng
    ndim = data_numpy.ndim            # Số chiều của mảng
    dtype = data_numpy.dtype          # Kiểu dữ liệu của mảng
    size = data_numpy.size            # Số phần tử trong mảng

    # In các thông tin
    print(f"Kích thước của data_numpy: {shape}")
    print(f"Số chiều của data_numpy: {ndim}")
    print(f"Kiểu dữ liệu của data_numpy: {dtype}")
    print(f"Số phần tử trong data_numpy: {size}")

except OSError:
    print("Không thể mở file Temp.txt. Vui lòng kiểm tra lại đường dẫn hoặc file.")
except ValueError:
    print("Dữ liệu trong file không hợp lệ hoặc không thể phân tích.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
