from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def calculate_perimeter(self):
        return self.a + self.b + self.c

# Get input from the user
shape_type = input("Enter the type of shape (Rectangle, Circle, Triangle): ")

if shape_type == "Rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    shape = Rectangle(length, width)
elif shape_type == "Circle":
    radius = float(input("Enter the radius: "))
    shape = Circle(radius)
elif shape_type == "Triangle":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    shape = Triangle(a, b, c)
else:
    print("Invalid shape type")
    exit()

# Calculate and print the area and perimeter
print(f"Area: {shape.calculate_area():.2f}")
print(f"Perimeter: {shape.calculate_perimeter():.2f}")