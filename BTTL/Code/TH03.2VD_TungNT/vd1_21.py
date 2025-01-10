class Rectangle:
    def __init__ (self, width, height):
        self.width = width
        self .height = height
    def getArea(self):
        area = round(self.width * self.height,1)
        return area
    def getPerimeter (self) :
        perimeter = round((self.width + self.height)*2,1)
        return perimeter