# Danh sách số nguyên
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# Nối hai danh sách
merged_list = list1 + list2

print('danh sách ban đầu: ',merged_list)

merged_list.append(6)
print("Sau khi dùng append(6):", merged_list)

merged_list.insert(2, 99)  # Thêm 99 vào vị trí có chỉ số 2 (giữa 2 và 3)
print("Sau khi dùng insert(2, 99):", merged_list)