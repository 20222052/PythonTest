try:
    # Mở file 'anh.txt' ở chế độ đọc
    with open('anh.txt', 'r') as f:
        # Hỏi người dùng muốn in tất cả hay một số dòng cụ thể
        choice = input("Bạn muốn in (1) toàn bộ file hoặc (2) một số dòng cụ thể? Nhập 1 hoặc 2: ").strip()

        if choice == "1":
            # In toàn bộ nội dung file
            print("Nội dung toàn bộ file:")
            for line in f:
                print(line.strip())
        elif choice == "2":
            # Hỏi số dòng cần in
            num_lines = int(input("Nhập số dòng bạn muốn in: "))
            print(f"In {num_lines} dòng đầu tiên:")
            for i in range(num_lines):
                line = f.readline()
                if line:  # Kiểm tra nếu dòng tồn tại
                    print(line.strip())
                else:
                    print("Không còn dòng nào để in.")
                    break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chạy lại và nhập 1 hoặc 2.")
except FileNotFoundError:
    print("Lỗi: File 'anh.txt' không tồn tại.")
except ValueError:
    print("Lỗi: Giá trị nhập không hợp lệ. Vui lòng nhập một số nguyên.")
except IOError:
    print("Lỗi: Không thể đọc file 'anh.txt'.")
