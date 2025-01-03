#Bài 1: Chia kẹo.
# Nhập số kẹo và số học sinh
so_keo = int(input("Nhập số kẹo của cô: "))
so_hoc_sinh = int(input("Nhập số học sinh trong lớp: "))

# Tính toán
if so_hoc_sinh == 0:
    print("Không thể chia kẹo vì không có học sinh!")
else:
    if so_keo < so_hoc_sinh:
        print("Không thể chia đều vì số kẹo nhỏ hơn số học sinh!")
    else:
        so_keo_moi_hoc_sinh = so_keo // so_hoc_sinh
        so_keo_con_lai = so_keo % so_hoc_sinh

        # Kết quả
        print(f"Mỗi học sinh được nhận: {so_keo_moi_hoc_sinh} cái kẹo")
        print(f"Số kẹo còn lại: {so_keo_con_lai}")