#Bai6: Nhập chữ cái Hoa
str = input("Nhập chữ cái (Hoa) bất kỳ: ")
phu = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R" , "S", "T", "V", "W" , "X", "Y", "Z"]
nguyen = ["U", "E", "O", "A", "I"]
if str in nguyen:
    print("Đây là nguyên âm!")
else:
    print("Đây là phụ âm!")