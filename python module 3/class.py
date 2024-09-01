"""Write a Python class named Rectangle constructed by a length
and width and a method which will compute the area of a
rectangle"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

rectangle = Rectangle(length, width)
print("The area of the rectangle is", rectangle.area())

    