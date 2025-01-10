def greeting(name, birth_year):
    return f"Xin chào {name}, bạn sinh năm {birth_year}!"

def rabbit_count(months):
    if months == 1 or months == 2:
        return 1
    else:
        return rabbit_count(months - 1) + rabbit_count(months - 2)

def count_mark(scores):
    total_students = len(scores)
    failed_students = sum(1 for score in scores if score < 5)
    return failed_students, total_students

def bmi_show(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "Gầy"
    elif 18.5 <= bmi < 24.9:
        return "Bình thường"
    elif 25 <= bmi < 29.9:
        return "Thừa cân"
    else:
        return "Béo phì"

def cal_point(scores):
    avg_10 = sum(scores) / len(scores)
    if avg_10 >= 8.5:
        avg_4 = 4.0
    elif avg_10 >= 7.0:
        avg_4 = 3.0
    elif avg_10 >= 5.5:
        avg_4 = 2.0
    elif avg_10 >= 4.0:
        avg_4 = 1.0
    else:
        avg_4 = 0.0
    return avg_10, avg_4

def list_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return [x for x in range(2, n + 1) if is_prime(x)]

def main_menu():
    while True:
        print("\n=== MENU THỰC HÀNH ===")
        print("1. Bài 1: Hàm greeting()")
        print("2. Bài 2: Hàm rabbit_count()")
        print("3. Bài 3: Hàm count_mark()")
        print("4. Bài 4: Hàm bmi_show()")
        print("5. Bài 5: Hàm cal_point()")
        print("6. Bài 6: Hàm list_prime()")
        print("0. Thoát")
        
        choice = input("Chọn chức năng (0-6): ")
        
        if choice == "1":
            name = input("Nhập tên: ")
            birth_year = input("Nhập năm sinh: ")
            print(greeting(name, birth_year))
        elif choice == "2":
            months = int(input("Nhập số tháng: "))
            print(f"Số thỏ sau {months} tháng: {rabbit_count(months)}")
        elif choice == "3":
            scores = list(map(float, input("Nhập danh sách điểm, cách nhau bởi dấu cách: ").split()))
            failed, total = count_mark(scores)
            print(f"Số sinh viên học lại: {failed}, Tổng số sinh viên: {total}")
        elif choice == "4":
            height = float(input("Nhập chiều cao (m): "))
            weight = float(input("Nhập cân nặng (kg): "))
            print("Nhận xét BMI:", bmi_show(height, weight))
        elif choice == "5":
            scores = list(map(float, input("Nhập danh sách điểm, cách nhau bởi dấu cách: ").split()))
            avg_10, avg_4 = cal_point(scores)
            print(f"Điểm trung bình hệ 10: {avg_10}, hệ 4: {avg_4}")
        elif choice == "6":
            n = int(input("Nhập số n: "))
            print(f"Các số nguyên tố từ 1 đến {n}: {list_prime(n)}")
        elif choice == "0":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chạy chương trình
if __name__ == "__main__":
    main_menu()
