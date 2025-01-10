#Bai9: Hiển thị bảng cửu chương
giatri = input("Nhập bảng cửu chương bạn muốn in: ")
print(f"Bảng cửu chương {giatri}: ")
for x in range(1, 11):
    print(f"{giatri} x {x} = {giatri * x}")