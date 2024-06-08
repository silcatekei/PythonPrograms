class Airplane:
    def __init__(self, flight_number, destination, departure_time):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.status = "On Time"
        self.delay = 0

    def check_status(self):
        return self.status

    def check_delay(self):
        return self.delay

    def delay_flight(self, delay_time):
        self.delay = delay_time
        self.status = "Delayed"

    def __str__(self):
        return f"Flight Number: {self.flight_number}, Destination: {self.destination}, Departure Time: {self.departure_time}, Status: {self.status}, Delay: {self.delay} minutes"

# Get input from the user
flight_number = input("Enter the flight number: ")
destination = input("Enter the destination: ")
departure_time = input("Enter the departure time: ")

# Create an instance of the Airplane class
airplane = Airplane(flight_number, destination, departure_time)

# Print the initial values
print("Initial values:")
print(airplane)

# Check the flight status
print(f"Flight status: {airplane.check_status()}")

# Check the flight delay
print(f"Flight delay: {airplane.check_delay()} minutes")

# Get input from the user to delay the flight
delay_time = int(input("Enter the delay time (in minutes): "))
airplane.delay_flight(delay_time)

# Print the updated values
print("\nUpdated values:")
print(airplane)

# Check the flight status
print(f"Flight status: {airplane.check_status()}")

# Check the flight delay
print(f"Flight delay: {airplane.check_delay()} minutes")