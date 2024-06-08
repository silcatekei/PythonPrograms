class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.classes = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def remove_teacher(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)

    def create_class(self, class_name, teacher):
        if teacher in self.teachers:
            self.classes.append({"name": class_name, "teacher": teacher})

    def __str__(self):
        return f"School: {self.name}\nStudents: {', '.join(self.students)}\nTeachers: {', '.join(self.teachers)}\nClasses: {', '.join([f'{class_name} ({teacher})' for class_name, teacher in [(class_info['name'], class_info['teacher']) for class_info in self.classes]])}"

# Get input from the user
school_name = input("Enter the name of the school: ")

# Create an instance of the School class
school = School(school_name)

# Print the initial values
print("Initial values:")
print(school)

# Get input from the user to add students
num_students = int(input("Enter the number of students to add: "))
for i in range(num_students):
    student = input(f"Enter student {i+1}: ")
    school.add_student(student)

# Get input from the user to add teachers
num_teachers = int(input("Enter the number of teachers to add: "))
for i in range(num_teachers):
    teacher = input(f"Enter teacher {i+1}: ")
    school.add_teacher(teacher)

# Get input from the user to create classes
num_classes = int(input("Enter the number of classes to create: "))
for i in range(num_classes):
    class_name = input(f"Enter class {i+1}: ")
    teacher = input(f"Enter teacher for class {i+1}: ")
    school.create_class(class_name, teacher)

# Print the updated values
print("\nUpdated values:")
print(school)

# Get input from the user to remove students and teachers
num_students_to_remove = int(input("Enter the number of students to remove: "))
for i in range(num_students_to_remove):
    student = input(f"Enter student {i+1} to remove: ")
    school.remove_student(student)

num_teachers_to_remove = int(input("Enter the number of teachers to remove: "))
for i in range(num_teachers_to_remove):
    teacher = input(f"Enter teacher {i+1} to remove: ")
    school.remove_teacher(teacher)

# Print the updated values
print("\nUpdated values:")
print(school)