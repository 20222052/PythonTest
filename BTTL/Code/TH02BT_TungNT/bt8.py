#Bai8: Xác định mùa trong năm
namsinh = input("Nhập tháng sinh: ")
xuan = ["1", "2", "3"]
ha = ["4", "5", "6"]
thu = ["7", "8", "9"]
dong = ["10", "11", "12"]
if namsinh in xuan:
    print("Bạn sinh vào mùa Xuân")
elif namsinh in ha:
    print("Bạn sinh vào mùa Hạ")
elif namsinh in thu:
    print("Bạn sinh vào mùa Thu")
elif namsinh in dong:
    print("Bạn sinh vào mùa Đông")
else:
    print("Vui lòng nhập tháng sinh từ 1-12")