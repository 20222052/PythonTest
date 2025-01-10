#Bai11: Kiểm tra số nguyên tố
def is_prime(n):
    # Kiểm tra nếu số nhỏ hơn 2
    if n < 2:
        return False
    
    # Kiểm tra các ước từ 2 đến căn bậc hai của n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

    # Nhập số tự nhiên từ người dùng
try:
    number = int(input("Nhập một số tự nhiên: "))
    if number < 0:
        print("Vui lòng nhập một số tự nhiên không âm.")
    elif is_prime(number):
        print(f"{number} là số nguyên tố.")
    else:
        print(f"{number} không phải là số nguyên tố.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")