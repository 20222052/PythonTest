import os

# Thư mục để tạo các file
directory = "BTTL\Code\TH06BT_TungNT"

# Danh sách tên file
file_names = [
    "bt4_1.py", "bt5_1.py", "bt5_2.py",
    "bt6_1.py", "bt4_2.py"
    ]

# Tạo thư mục nếu chưa tồn tại
os.makedirs(directory, exist_ok=True)

# Tạo các file rỗng
for file_name in file_names:
    file_path = os.path.join(directory, file_name)
    open(file_path, "w").close()  # Tạo file rỗng
    print(f"Created empty file: {file_path}")
