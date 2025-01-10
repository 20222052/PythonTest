try:
    # Mở file 'anh.txt' ở chế độ đọc
    with open('anh.txt', "r") as f:
        # Đọc tối đa 15 ký tự từ file
        st = f.read()
        
        # Kiểm tra nếu nội dung đọc được rỗng
        if not st:
            print("File rỗng hoặc không có nội dung.")
        else:
            # Hiển thị kết quả
            print(st, 'số ký tự là:', len(st))
            print(st)
except FileNotFoundError:
    print("Lỗi: File 'anh.txt' không tồn tại.")
except IOError:
    print("Lỗi: Không thể đọc file 'anh.txt'.")
