import numpy as np

#bài 1
# Định nghĩa kích thước ma trận
n = 12

# Tạo ma trận với các số nguyên ngẫu nhiên từ 0 đến 100
matrix = np.random.randint(0, 101, size=(n, n))

#hiển thị ma trận
print(matrix)

#bài 2
# Tìm các phần tử nằm trên đường chọn chính
# Tìm các phần tử nằm trên đường chọn phụ

# Lấy các phần tử trên đường chéo chính
main_diagonal = np.diag(matrix)

# Lấy các phần tử trên đường chéo phụ
anti_diagonal = np.diag(np.fliplr(matrix))

# Hiển thị kết quả
print("Vector các phần tử nằm trên đường chéo chính:")
print(main_diagonal)
print("--------------------------------------------------")
print("Vector các phần tử nằm trên đường chéo phụ:")
print(anti_diagonal)

#bài 3
x = 11  # Giá trị x bạn muốn kiểm tra

# Đếm số phần tử bằng, lớn hơn, và nhỏ hơn x
count_equal = np.sum(matrix == x)
count_greater = np.sum(matrix > x)
count_smaller = np.sum(matrix < x)

# Hiển thị kết quả
print(f"Số phần tử bằng {x}: {count_equal}")
print(f"Số phần tử lớn hơn {x}: {count_greater}")
print(f"Số phần tử nhỏ hơn {x}: {count_smaller}")