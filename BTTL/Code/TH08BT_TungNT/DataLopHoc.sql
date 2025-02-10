-- Tạo CSDL
CREATE DATABASE QuanLyLopHoc;
USE QuanLyLopHoc;

-- Tạo bảng Lop
CREATE TABLE Lop (
    ma_lop INT PRIMARY KEY AUTO_INCREMENT,
    ten_lop VARCHAR(100) NOT NULL,
    si_so INT NOT NULL
);

-- Tạo bảng SinhVien
CREATE TABLE SinhVien (
    ma_sv INT PRIMARY KEY AUTO_INCREMENT,
    ho_ten VARCHAR(100) NOT NULL,
    ngay_sinh DATE NOT NULL,
    gioi_tinh ENUM('Nam', 'Nữ') NOT NULL,
    ma_lop INT,
    FOREIGN KEY (ma_lop) REFERENCES Lop(ma_lop) ON DELETE CASCADE
);

-- Tạo bảng MonHoc
CREATE TABLE MonHoc (
    ma_mon INT PRIMARY KEY AUTO_INCREMENT,
    ten_mon VARCHAR(100) NOT NULL,
    so_tin_chi INT NOT NULL
);

-- Tạo bảng GiangVien
CREATE TABLE GiangVien (
    ma_gv INT PRIMARY KEY AUTO_INCREMENT,
    ho_ten VARCHAR(100) NOT NULL,
    chuyen_mon VARCHAR(100) NOT NULL
);

-- Tạo bảng Diem
CREATE TABLE Diem (
    ma_sv INT,
    ma_mon INT,
    diem FLOAT CHECK (diem BETWEEN 0 AND 10),
    PRIMARY KEY (ma_sv, ma_mon),
    FOREIGN KEY (ma_sv) REFERENCES SinhVien(ma_sv) ON DELETE CASCADE,
    FOREIGN KEY (ma_mon) REFERENCES MonHoc(ma_mon) ON DELETE CASCADE
);

-- Chèn dữ liệu vào bảng Lop
INSERT INTO Lop (ten_lop, si_so) VALUES 
('Lop 12A', 40), 
('Lop 12B', 35);

-- Chèn dữ liệu vào bảng SinhVien
INSERT INTO SinhVien (ho_ten, ngay_sinh, gioi_tinh, ma_lop) VALUES 
('Nguyen Van A', '2006-05-10', 'Nam', 1),
('Tran Thi B', '2006-07-20', 'Nữ', 2),
('Le Van C', '2006-03-15', 'Nam', 1);

-- Chèn dữ liệu vào bảng MonHoc
INSERT INTO MonHoc (ten_mon, so_tin_chi) VALUES 
('Toan', 4), 
('Van', 3), 
('Ly', 3);

-- Chèn dữ liệu vào bảng GiangVien
INSERT INTO GiangVien (ho_ten, chuyen_mon) VALUES 
('Le Van C', 'Toan'), 
('Pham Thi D', 'Van');

-- Chèn dữ liệu vào bảng Diem
INSERT INTO Diem (ma_sv, ma_mon, diem) VALUES 
(1, 1, 8.5), 
(2, 2, 7.0), 
(3, 1, 6.5),
(3, 3, 9.0);

-- Hiển thị danh sách CSDL và bảng
SHOW DATABASES;
USE QuanLyLopHoc;
SHOW TABLES;
DESC SinhVien;

-- Truy vấn danh sách sinh viên và lớp
SELECT sv.ma_sv, sv.ho_ten, sv.ngay_sinh, sv.gioi_tinh, lop.ten_lop 
FROM SinhVien sv 
JOIN Lop lop ON sv.ma_lop = lop.ma_lop;

-- Truy vấn sinh viên có điểm > 8
SELECT sv.ho_ten, d.diem 
FROM SinhVien sv 
JOIN Diem d ON sv.ma_sv = d.ma_sv 
WHERE d.diem > 8;

-- Đếm số lượng sinh viên trong mỗi lớp
SELECT lop.ten_lop, COUNT(sv.ma_sv) AS so_luong_sinh_vien 
FROM Lop lop 
LEFT JOIN SinhVien sv ON lop.ma_lop = sv.ma_lop 
GROUP BY lop.ten_lop;

-- Lấy danh sách môn học và giảng viên
SELECT mh.ten_mon, gv.ho_ten AS giang_vien
FROM MonHoc mh 
JOIN GiangVien gv ON mh.ten_mon = gv.chuyen_mon;

-- Lấy danh sách sinh viên và điểm trung bình
SELECT sv.ho_ten, AVG(d.diem) AS diem_trung_binh 
FROM SinhVien sv 
JOIN Diem d ON sv.ma_sv = d.ma_sv 
GROUP BY sv.ho_ten;

-- Sinh viên có điểm trung bình cao nhất
SELECT sv.ho_ten, AVG(d.diem) AS diem_trung_binh 
FROM SinhVien sv 
JOIN Diem d ON sv.ma_sv = d.ma_sv 
GROUP BY sv.ho_ten 
ORDER BY diem_trung_binh DESC 
LIMIT 1;

-- Danh sách sinh viên theo thứ tự tên
SELECT * FROM SinhVien ORDER BY ho_ten ASC;

-- Lấy số môn học đã học của mỗi sinh viên
SELECT sv.ho_ten, COUNT(d.ma_mon) AS so_mon_da_hoc 
FROM SinhVien sv 
JOIN Diem d ON sv.ma_sv = d.ma_sv 
GROUP BY sv.ho_ten;

-- Tìm sinh viên chưa có điểm môn nào
SELECT sv.ho_ten 
FROM SinhVien sv 
LEFT JOIN Diem d ON sv.ma_sv = d.ma_sv 
WHERE d.ma_mon IS NULL;

-- Tổng số tín chỉ sinh viên đã học
SELECT sv.ho_ten, SUM(mh.so_tin_chi) AS tong_tin_chi 
FROM SinhVien sv 
JOIN Diem d ON sv.ma_sv = d.ma_sv 
JOIN MonHoc mh ON d.ma_mon = mh.ma_mon 
GROUP BY sv.ho_ten;

-- Danh sách giảng viên dạy Toán hoặc Văn
SELECT * FROM GiangVien WHERE chuyen_mon IN ('Toan', 'Van');

-- Lớp có sĩ số nhiều nhất
SELECT ten_lop, si_so FROM Lop ORDER BY si_so DESC LIMIT 1;

-- Môn học có số tín chỉ lớn hơn 3
SELECT * FROM MonHoc WHERE so_tin_chi > 3;

-- Sinh viên có ngày sinh năm 2006
SELECT * FROM SinhVien WHERE YEAR(ngay_sinh) = 2006;

-- Sinh viên có tên bắt đầu bằng 'Nguyen'
SELECT * FROM SinhVien WHERE ho_ten LIKE 'Nguyen%';
