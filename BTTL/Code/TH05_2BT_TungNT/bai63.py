import numpy as np

# Dữ liệu ma trận height và weight
height_matrix = np.array([
    [174, 189, 185, 195, 149, 189, 147, 154, 174, 169],
    [195, 159, 192, 155, 191, 153, 157, 140, 144, 172],
    [157, 153, 169, 185, 172, 151, 190, 187, 163, 179],
    [153, 178, 195, 167, 161, 174, 184, 162, 185, 145],
    [175, 149, 172, 165, 182, 167, 172, 152, 154, 143],
    [168, 176, 162, 166, 195, 173, 191, 155, 185, 143],
    [191, 141, 184, 153, 163, 180, 185, 185, 152, 179],
    [164, 166, 160, 165, 192, 159, 163, 173, 157, 154],
    [164, 166, 191, 157, 163, 185, 172, 123, 163, 179],
    [178, 183, 194, 185, 172, 162, 169, 195, 185, 190]
])

weight_matrix = np.array([
    [96, 87, 110, 104, 61, 104, 92, 111, 90, 103],
    [81, 80, 101, 51, 79, 107, 110, 129, 145, 139],
    [110, 149, 97, 137, 153, 125, 129, 125, 159, 152],
    [121, 52, 93, 105, 118, 143, 105, 94, 127, 98],
    [120, 108, 105, 112, 123, 113, 72, 152, 127, 86],
    [135, 145, 54, 144, 95, 110, 119, 118, 106, 127],
    [88, 141, 105, 75, 118, 110, 121, 123, 154, 123],
    [75, 140, 145, 118, 123, 118, 127, 113, 85, 140],
    [154, 96, 91, 150, 145, 154, 95, 106, 61, 119],
    [154, 96, 119, 61, 104, 96, 69, 50, 119, 96]
])

# Tìm ma trận chuyển vị (transpose)
height_transpose = height_matrix.T
weight_transpose = weight_matrix.T

# Tính hạng của ma trận
rank_height = np.linalg.matrix_rank(height_matrix)
rank_weight = np.linalg.matrix_rank(weight_matrix)

# Hiển thị kết quả
print("Ma trận chuyển vị height.T:")
print(height_transpose)

print("\nMa trận chuyển vị weight.T:")
print(weight_transpose)

print("\nHạng của ma trận height:", rank_height)
print("Hạng của ma trận weight:", rank_weight)
