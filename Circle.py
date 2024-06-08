import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Radius: {self.radius}, Area: {self.calculate_area():.2f}, Circumference: {self.calculate_circumference():.2f}"

# Get input from the user
radius = float(input("Enter the radius of the circle: "))

# Create an instance of the Circle class
circle = Circle(radius)

# Print the initial values
print("Initial values:")
print(circle)

# Get input from the user to modify the radius
new_radius = float(input("Enter the new radius for the circle: "))

# Modify the radius using the setter method
circle.set_radius(new_radius)

# Print the updated values
print("\nUpdated values:")
print(circle)