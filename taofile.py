import os

# Thư mục để tạo các file
directory = "BTTL\Code\TH08VD_TungNT"

# Danh sách tên file
file_names = [
    "vd1.py", "vd2.py", "vd3.py",
    "vd4.py", "vd5.py", "vd6.py",
    "vd7.py", "vd8.py", "vd9.py",
    "vd10.py", "vd11.py", "vd12.py",
    "vd15.py", "vd14.py", "vd13.py",
    "vd16.py"
    ]

# Tạo thư mục nếu chưa tồn tại
os.makedirs(directory, exist_ok=True)

# Tạo các file rỗng
for file_name in file_names:
    file_path = os.path.join(directory, file_name)
    open(file_path, "w").close()  # Tạo file rỗng
    print(f"Created empty file: {file_path}")
