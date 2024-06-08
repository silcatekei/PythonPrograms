class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def set_name(self, name):
        self.name = name

    def set_breed(self, breed):
        self.breed = breed

    def __str__(self):
        return f"Name: {self.name}, Breed: {self.breed}"

# Get input from the user
name1 = input("Enter the name of the first dog: ")
breed1 = input("Enter the breed of the first dog: ")
name2 = input("Enter the name of the second dog: ")
breed2 = input("Enter the breed of the second dog: ")

# Create two instances of the Dog class
dog1 = Dog(name1, breed1)
dog2 = Dog(name2, breed2)

# Print the initial values
print("Initial values:")
print(dog1)
print(dog2)

# Get input from the user to modify the attributes
new_name1 = input("Enter the new name for the first dog: ")
new_breed1 = input("Enter the new breed for the first dog: ")
new_name2 = input("Enter the new name for the second dog: ")
new_breed2 = input("Enter the new breed for the second dog: ")

# Modify the attributes using setter methods
dog1.set_name(new_name1)
dog1.set_breed(new_breed1)
dog2.set_name(new_name2)
dog2.set_breed(new_breed2)

# Print the updated values
print("\nUpdated values:")
print(dog1)
print(dog2)