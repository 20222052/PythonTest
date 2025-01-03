#Bài 4: Chuỗi văn bản 
# Đoạn văn
doan_van = "Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 – 1969)"

# 1. Số ký tự trong đoạn văn
so_ky_tu = len(doan_van)
print(f"Số ký tự có trong đoạn văn: {so_ky_tu}")

# 2. Kiểm tra từ có xuất hiện hay không (không phân biệt hoa thường)
tim_ho_chi_minh = "hồ chí minh" in doan_van.lower()
tim_non_song = "non sông" in doan_van.lower()
print(f"Có chứa 'hồ chí minh': {tim_ho_chi_minh}")
print(f"Có chứa 'non sông': {tim_non_song}")

# 3. Tách đoạn văn thành các câu bằng dấu '.'
cac_cau = doan_van.split('.')
print(f"Các câu trong đoạn văn: {cac_cau}")

# 4. Kiểm tra có ký tự nào khác chữ và số hay không
ky_tu_dac_biet = any(not char.isalnum() and not char.isspace() for char in doan_van)
print(f"Có ký tự nào khác chữ và số: {ky_tu_dac_biet}")

# 5. Thay thế 'Việt Nam' bằng 'VIỆT NAM'
doan_van_thay_the = doan_van.replace('Việt Nam', 'VIỆT NAM')
print(f"Đoạn văn sau khi thay thế: {doan_van_thay_the}")