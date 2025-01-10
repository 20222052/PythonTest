def example_4():
    print("Ví dụ Slide 4 (Trang 4): Định nghĩa hàm cơ bản")
    def ten_ham(tham_so):
        """Mô tả chức năng của hàm"""
        return f"Đầu vào là: {tham_so}"
    
    tham_so = input("Nhập tham số: ")
    print(ten_ham(tham_so))

def example_6():
    print("Ví dụ Slide 6 (Trang 6): Gọi hàm")
    def say_hello():
        print("Xin chào!")
    
    print("Gọi hàm say_hello()...")
    say_hello()

def example_7():
    print("Ví dụ Slide 7 (Trang 7): Lệnh return")
    def cong_hai_so(a, b):
        return a + b

    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    print(f"Tổng của {a} và {b} là: {cong_hai_so(a, b)}")

def example_8():
    print("Ví dụ Slide 8 (Trang 8): Trả về nhiều giá trị")
    def tinh_toan(a, b):
        tong = a + b
        hieu = a - b
        return tong, hieu

    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    tong, hieu = tinh_toan(a, b)
    print(f"Tổng: {tong}, Hiệu: {hieu}")

def example_9():
    print("Ví dụ Slide 9 (Trang 9): Tham số bắt buộc")
    def say_hello(name):
        print(f"Xin chào, {name}!")

    name = input("Nhập tên của bạn: ")
    say_hello(name)

def example_10():
    print("Ví dụ Slide 10 (Trang 10): Tham số mặc định (Cơ bản)")
    def greeting(name="bạn"):
        print(f"Xin chào, {name}!")

    print("Gọi hàm greeting() không truyền tham số:")
    greeting()
    name = input("Nhập tên của bạn: ")
    print("Gọi hàm greeting() có truyền tham số:")
    greeting(name)

def example_11():
    print("Ví dụ Slide 11 (Trang 11): Tham số mặc định (Nâng cao)")
    def sum_ab(a=0, b=0):
        return a + b

    print("Gọi hàm không truyền tham số:")
    print(f"Kết quả: {sum_ab()}")  # Sử dụng giá trị mặc định

    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    print(f"Gọi hàm với tham số a={a}, b={b}: Kết quả: {sum_ab(a, b)}")

def example_12():
    print("Ví dụ Slide 12 (Trang 12): Tham số có độ dài biến")
    def tong(*args):
        return sum(args)

    nums = list(map(int, input("Nhập các số, cách nhau bởi dấu cách: ").split()))
    print(f"Tổng các số: {tong(*nums)}")

def example_13():
    print("Ví dụ Slide 13 (Trang 13): Phạm vi của biến")
    x = 10  # Biến toàn cục

    def thay_doi():
        global x
        x = 5  # Thay đổi giá trị biến toàn cục
        print("Giá trị bên trong hàm:", x)

    print("Giá trị ban đầu của x:", x)
    thay_doi()
    print("Giá trị sau khi thay đổi:", x)

def example_14():
    print("Ví dụ Slide 14 (Trang 14): Hàm ẩn danh (Lambda)")
    binh_phuong = lambda x: x ** 2
    tong_hai_so = lambda a, b: a + b

    x = int(input("Nhập số x: "))
    print(f"Bình phương của {x} là: {binh_phuong(x)}")

    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    print(f"Tổng của {a} và {b} là: {tong_hai_so(a, b)}")

def example_15():
    print("Ví dụ Slide 15 (Trang 15): Lambda với map và filter")
    numbers = list(map(int, input("Nhập các số, cách nhau bởi dấu cách: ").split()))

    squared = list(map(lambda x: x ** 2, numbers))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    print(f"Danh sách bình phương: {squared}")
    print(f"Danh sách số chẵn: {even_numbers}")

def main_menu_examples():
    while True:
        print("\n=== MENU VÍ DỤ (SLIDES 4-15) ===")
        print("1. Ví dụ Slide 4 (Trang 4): Định nghĩa hàm")
        print("2. Ví dụ Slide 6 (Trang 6): Gọi hàm")
        print("3. Ví dụ Slide 7 (Trang 7): Lệnh return")
        print("4. Ví dụ Slide 8 (Trang 8): Trả về nhiều giá trị")
        print("5. Ví dụ Slide 9 (Trang 9): Tham số bắt buộc")
        print("6. Ví dụ Slide 10 (Trang 10): Tham số mặc định (Cơ bản)")
        print("7. Ví dụ Slide 11 (Trang 11): Tham số mặc định (Nâng cao)")
        print("8. Ví dụ Slide 12 (Trang 12): Tham số có độ dài biến")
        print("9. Ví dụ Slide 13 (Trang 13): Phạm vi của biến")
        print("10. Ví dụ Slide 14 (Trang 14): Hàm Lambda")
        print("11. Ví dụ Slide 15 (Trang 15): Lambda với map và filter")
        print("0. Thoát")

        choice = input("Chọn chức năng (0-11): ")

        if choice == "1":
            example_4()
        elif choice == "2":
            example_6()
        elif choice == "3":
            example_7()
        elif choice == "4":
            example_8()
        elif choice == "5":
            example_9()
        elif choice == "6":
            example_10()
        elif choice == "7":
            example_11()
        elif choice == "8":
            example_12()
        elif choice == "9":
            example_13()
        elif choice == "10":
            example_14()
        elif choice == "11":
            example_15()
        elif choice == "0":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chạy chương trình
if __name__ == "__main__":
    main_menu_examples()
