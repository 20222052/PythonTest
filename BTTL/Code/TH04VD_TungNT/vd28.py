import numpy as np

# Giả sử mảng a_int đã được tạo sẵn với kiểu int32
a_int = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# Chuyển từ kiểu int --> str
a_str = a_int.astype(np.str_)
print(a_str)
print('Dữ liệu sau khi chuyển:', a_str.dtype)
print('--------------------------------')

# Chuyển từ kiểu int --> bool
a_bol = a_int.astype(np.bool_)
print(a_bol)
print('Dữ liệu sau khi chuyển:', a_bol.dtype)
