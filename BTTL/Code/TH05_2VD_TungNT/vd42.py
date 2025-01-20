import numpy as np

# Tạo ma trận A (giống như trong hình)
A = np.array([
    [60, 84, 47, 28, 48, 83, 43],
    [59, 56, 32, 80, 52, 76, 91],
    [6, 15, 21, 4, 94, 67, 5],
    [20, 50, 70, 56, 54, 51, 89],
    [76, 56, 82, 78, 3, 77, 41],
    [74, 5, 27, 35, 90, 20, 14],
    [89, 73, 27, 88, 36, 96, 72],
    [95, 15, 67, 75, 83, 36, 96]
])

# 1. Lấy các phần tử nằm trên đường chéo chính cách 1 phần tử (đường chéo trên)
d_A1 = A.diagonal(1)
print("Đường chéo trên 1 phần tử:", d_A1)

# 2. Lấy các phần tử nằm trên đường chéo chính
d_A = A.diagonal()
print("Đường chéo chính:", d_A)

# 3. Lấy các phần tử nằm dưới đường chéo chính cách 4 phần tử (đường chéo dưới)
d_A_neg4 = A.diagonal(-4)
print("Đường chéo dưới cách 4 phần tử:", d_A_neg4)
