import os

# Thư mục để tạo các file
directory = "BTTL\Code\TH02BT_TungNT"

# Danh sách tên file
file_names = [
    "bt6.py", "bt7.py", "bt8.py",
    "bt9.py", "bt10.py", "bt11.py",
    "bt14.py", "bt13.py", "bt12.py"
    ]

# Tạo thư mục nếu chưa tồn tại
os.makedirs(directory, exist_ok=True)

# Tạo các file rỗng
for file_name in file_names:
    file_path = os.path.join(directory, file_name)
    open(file_path, "w").close()  # Tạo file rỗng
    print(f"Created empty file: {file_path}")
