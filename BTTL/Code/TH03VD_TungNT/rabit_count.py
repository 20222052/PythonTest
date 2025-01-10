def rabbit_count(months):
    if months <= 0:
        return 0  # Không có thỏ nếu số tháng <= 0
    elif months == 1:
        return 3  # Tháng đầu tiên chỉ có 1 cặp thỏ

    # Khởi tạo hai tháng đầu
    prev1, prev2 = 1, 1  # prev1: tháng trước đó, prev2: tháng trước nữa

    for _ in range(2, months):
        current = prev1 + prev2  # Số thỏ hiện tại
        prev2 = prev1  # Cập nhật tháng trước nữa
        prev1 = current  # Cập nhật tháng trước đó

    return prev1

try:
    months = int(input("Nhap so thang: "))
    print(f"So thỏ sau {months} thang: {rabbit_count(months)}")
except ValueError:
    print("Vui long nhap so nguyen.")
