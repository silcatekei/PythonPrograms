class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu_items = {}
        self.ratings = {}

    def add_item(self, item, price):
        self.menu_items[item] = price

    def remove_item(self, item):
        if item in self.menu_items:
            del self.menu_items[item]

    def add_rating(self, item, rating):
        if item in self.menu_items:
            if item in self.ratings:
                self.ratings[item].append(rating)
            else:
                self.ratings[item] = [rating]

    def calculate_average_rating(self, item):
        if item in self.ratings:
            return sum(self.ratings[item]) / len(self.ratings[item])
        else:
            return 0

    def __str__(self):
        output = f"Restaurant: {self.name}\n"
        output += "Menu Items:\n"
        for item, price in self.menu_items.items():
            output += f"  {item}: ${price:.2f}\n"
        output += "Ratings:\n"
        for item, ratings in self.ratings.items():
            output += f"  {item}: {self.calculate_average_rating(item):.2f}/5\n"
        return output

# Get input from the user
restaurant_name = input("Enter the name of the restaurant: ")

# Create an instance of the Restaurant class
restaurant = Restaurant(restaurant_name)

# Print the initial values
print("Initial values:")
print(restaurant)

# Get input from the user to add menu items
num_items = int(input("Enter the number of menu items to add: "))
for i in range(num_items):
    item = input(f"Enter menu item {i+1}: ")
    price = float(input(f"Enter price for {item}: $"))
    restaurant.add_item(item, price)

# Get input from the user to add ratings
num_ratings = int(input("Enter the number of ratings to add: "))
for i in range(num_ratings):
    item = input(f"Enter menu item for rating {i+1}: ")
    rating = float(input(f"Enter rating for {item} (1-5): "))
    restaurant.add_rating(item, rating)

# Print the updated values
print("\nUpdated values:")
print(restaurant)

# Get input from the user to remove menu items
num_items_to_remove = int(input("Enter the number of menu items to remove: "))
for i in range(num_items_to_remove):
    item = input(f"Enter menu item {i+1} to remove: ")
    restaurant.remove_item(item)

# Print the updated values
print("\nUpdated values:")
print(restaurant)