class Person:
    def __init__(self, name, year, height, weight):
        self.name = name
        self.year = year
        self.height = height
        self.weight = weight

    def bmi(self):
        return round(self.weight / (self.height ** 2), 2)

    def getting(self):
        """Hiển thị thông tin cá nhân."""
        print(f"Tên: {self.name}")
        print(f"Năm sinh: {self.year}")
        print(f"Chiều cao: {self.height} m")
        print(f"Cân nặng: {self.weight} kg")


# Tạo đối tượng Person
p1 = Person('Nguyễn Thanh Tùng', 2004, 1.67, 57)

# Hiển thị thông tin
p1.getting()

# Tính và in chỉ số BMI
print('Chỉ số BMI: ' + str(p1.bmi()))

# # Bài 15: slide 44- Đọc dữ liệu trong dãy số

# def swap_max_min_and_save(input_list, output_file):
#     # Tìm chỉ số của phần tử lớn nhất và nhỏ nhất đầu tiên
#     max_index = input_list.index(max(input_list))
#     min_index = input_list.index(min(input_list))

#     # Đổi chỗ hai phần tử
#     input_list[max_index], input_list[min_index] = input_list[min_index], input_list[max_index]

#     # Ghi dãy đã đổi chỗ vào file
#     with open(output_file, 'w') as file:
#         file.write(' '.join(map(str, input_list)))

#     print(f"Dãy mới đã được lưu vào file: {output_file}")


# # Danh sách đầu vào
# input_list = [3, 5, 9, 2, 7, 9, 1, 8]

# # Đường dẫn tới file đầu ra
# output_file = "dayso2_bai17.txt"

# # Thực hiện đổi chỗ và lưu kết quả
# swap_max_min_and_save(input_list, output_file)

