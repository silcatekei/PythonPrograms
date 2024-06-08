class TrafficLight:
    def __init__(self, color, duration):
        self.color = color
        self.duration = duration

    def change_color(self, new_color):
        self.color = new_color

    def check_red(self):
        return self.color == "Red"

    def check_green(self):
        return self.color == "Green"

    def __str__(self):
        return f"Color: {self.color}, Duration: {self.duration} seconds"

# Create an instance of the TrafficLight class
traffic_light = TrafficLight("Red", 30)

# Print the initial values
print("Initial values:")
print(traffic_light)

# Check if the traffic light is red
if traffic_light.check_red():
    print("The traffic light is red.")
else:
    print("The traffic light is not red.")

# Check if the traffic light is green
if traffic_light.check_green():
    print("The traffic light is green.")
else:
    print("The traffic light is not green.")

# Change the color of the traffic light
traffic_light.change_color("Green")

# Print the updated values
print("\nUpdated values:")
print(traffic_light)

# Check if the traffic light is red
if traffic_light.check_red():
    print("The traffic light is red.")
else:
    print("The traffic light is not red.")

# Check if the traffic light is green
if traffic_light.check_green():
    print("The traffic light is green.")
else:
    print("The traffic light is not green.")