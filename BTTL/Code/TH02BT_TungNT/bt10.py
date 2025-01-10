   
#Bai10: Tính điểm học tập
diem = [9.0, 8.9, 7.8]
diem_chu = []
for i in diem:
    if 9.0 < i <= 10:
        diem_chu.append("A+")
    elif 8.5 < i <= 8.9:
        diem_chu.append("A")
    elif 8.0 < i <=8.4:
        diem_chu.append("B+")
    elif 7.5 < i <= 7.9:
        diem_chu.append("B")
    elif 7.0<i<=7.4:
        diem_chu.append("C+")
    elif 6.5<i<=6.9:
        diem_chu.append("C")
    elif 6.0<i<=6.4:
        diem_chu.append("C")
    elif 6.5<i<=6.9:
        diem_chu.append("C")
print(diem_chu)