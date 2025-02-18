import numpy as np

# Đọc dữ liệu từ file, bỏ qua dòng đầu tiên (chứa tên thành phố)
data = np.loadtxt('./temp.txt', delimiter=',', skiprows=1)

# Tính nhiệt độ cao nhất, thấp nhất và trung bình cho từng thành phố
city_max = np.max(data, axis=0)
city_min = np.min(data, axis=0)
city_mean = np.mean(data, axis=0).round(2)

# Tính nhiệt độ thống kê chung cho cả 6 thành phố
overall_max = np.max(data)
overall_min = np.min(data)
overall_mean = np.mean(data).round(2)

# Tạo ma trận data_thongke (3 hàng, 7 cột)
data_thongke = np.zeros((3, 7))
data_thongke[0, :-1] = city_max  # Hàng 0: Nhiệt độ lớn nhất cho từng thành phố
data_thongke[1, :-1] = city_mean  # Hàng 1: Nhiệt độ trung bình cho từng thành phố
data_thongke[2, :-1] = city_min  # Hàng 2: Nhiệt độ nhỏ nhất cho từng thành phố

# Cột cuối cùng: Thống kê chung cho cả 6 thành phố
data_thongke[0, -1] = overall_max  # Max của tất cả
data_thongke[1, -1] = overall_mean  # Mean của tất cả
data_thongke[2, -1] = overall_min  # Min của tất cả

# Lưu kết quả vào file với UTF-8 encoding
with open('thongke.txt', 'w', encoding='utf-8') as f:
    # Ghi tiêu đề (header)
    f.write("Hà Nội\tVinh\tĐà Nẵng\tNha Trang\tHCM\tCà Mau\tChung\n")
    # Lưu dữ liệu vào file
    np.savetxt(f, data_thongke, fmt='%.2f', delimiter='\t')

print("Ma trận thống kê đã được lưu vào file 'thongke.txt'.")
