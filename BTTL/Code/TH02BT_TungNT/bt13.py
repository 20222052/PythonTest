#Bài 13: Chuyển N sang nhị phân:
def decimal_to_binary(n):
    # Hàm chuyển đổi số thập phân sang nhị phân
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

# Nhập số tự nhiên N từ người dùng
try:
    N = int(input("Nhập số tự nhiên N (N > 0): "))
    if N <= 0:
        print("Vui lòng nhập một số tự nhiên lớn hơn 0.")
    else:
        binary_representation = decimal_to_binary(N)
        print(f"Số {N} trong hệ nhị phân là: {binary_representation}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")