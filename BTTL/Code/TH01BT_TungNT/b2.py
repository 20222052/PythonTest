#Bài 2: Tính Tuổi 
from datetime import datetime

# Họ tên và năm sinh đã được xác định
ho_ten = "Thu Phương"  # Tên đã được xác định
nam_sinh = 2000  # Năm sinh đã được xác định

# Tính tuổi
nam_hien_tai = datetime.now().year
tuoi = nam_hien_tai - nam_sinh

# Hiển thị kết quả
print(f"Chào bạn {ho_ten}, bạn {tuoi} tuổi.")