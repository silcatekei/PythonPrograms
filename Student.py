class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def __str__(self):
        return f"Name: {self.name}, Grade: {self.grade}, Courses: {', '.join(self.courses)}"

# Get input from the user
name = input("Enter the name of the student: ")
grade = int(input("Enter the grade of the student: "))

# Create an instance of the Student class
student = Student(name, grade)

# Print the initial values
print("Initial values:")
print(student)

# Get input from the user to add courses
num_courses = int(input("Enter the number of courses to add: "))
for i in range(num_courses):
    course = input(f"Enter course {i+1}: ")
    student.add_course(course)

# Print the updated values
print("\nUpdated values:")
print(student)

# Get input from the user to remove courses
num_courses = int(input("Enter the number of courses to remove: "))
for i in range(num_courses):
    course = input(f"Enter course {i+1}: ")
    student.remove_course(course)

# Print the updated values
print("\nUpdated values:")
print(student)