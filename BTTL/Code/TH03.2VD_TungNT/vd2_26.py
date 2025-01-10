class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = round(self.width * self.height, 1)
        return area

    def getPerimeter(self):
        perimeter = round((self.width + self.height) * 2, 1)
        return perimeter

# Tạo các đối tượng
r1 = Rectangle(10, 5)
r2 = Rectangle(20, 11)

# Lấy thuộc tính
x = r1.width
y = r1.height

# In thông tin
print('--- Thuộc tính ---')
print('1. Thuộc tính Chiều rộng:', x)
print('2. Thuộc tính Chiều dài:', y)

# Sử dụng phương thức
dt = r1.getArea()
cv = r1.getPerimeter()

print('-- Phương thức --')
print('1. Phương thức tính Diện tích:', dt)
print('2. Phương thức tính Chu vi:', cv)
