# Bài 12: Hiển thị số NT từ 2 Tới N
def is_prime(num):
    # Hàm kiểm tra số nguyên tố
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_up_to_n(n):
    # Hàm lấy danh sách các số nguyên tố từ 2 đến n
    prime_numbers = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers

# Nhập số N từ người dùng
try:
    N = int(input("Nhập số tự nhiên N: "))
    if N < 2:
        print("Không có số nguyên tố nào trong khoảng này.")
    else:
        prime_list = primes_up_to_n(N)
        print(f"Các số nguyên tố từ 2 tới {N} là: {prime_list}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")