import random

class Flight:
    def __init__(self, id, origin, destination, date, num_passengers, price):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.date = date
        self.num_passengers = num_passengers
        self.price = price
        self.confirmation_number = random.randint(100000, 999999)

    def __str__(self):
        return f"Flight {self.id}: {self.origin} to {self.destination} on {self.date} for {self.num_passengers} passengers. Price: ${self.price:.2f}. Confirmation number: {self.confirmation_number}"

class Hotel:
    def __init__(self, id, name, location, check_in_date, check_out_date, num_guests, price):
        self.id = id
        self.name = name
        self.location = location
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.num_guests = num_guests
        self.price = price
        self.confirmation_number = random.randint(100000, 999999)

    def __str__(self):
        return f"Hotel {self.id}: {self.name} in {self.location} from {self.check_in_date} to {self.check_out_date} for {self.num_guests} guests. Price: ${self.price:.2f}. Confirmation number: {self.confirmation_number}"

class TravelApp:
    def __init__(self):
        self.flights = []
        self.hotels = []
        self.reservations = {}

    def search_flights(self, origin, destination, date, num_passengers):
        print(f"Searching for flights from {origin} to {destination} on {date} for {num_passengers} passengers.")
        # Add some sample flights
        self.flights.append(Flight(1, origin, destination, date, num_passengers, 200.0))
        self.flights.append(Flight(2, origin, destination, date, num_passengers, 250.0))
        self.flights.append(Flight(3, origin, destination, date, num_passengers, 300.0))
        print("Available flights:")
        for flight in self.flights:
            print(flight)

    def search_hotels(self, location, check_in_date, check_out_date, num_guests):
        print(f"Searching for hotels in {location} from {check_in_date} to {check_out_date} for {num_guests} guests.")
        # Add some sample hotels
        self.hotels.append(Hotel(1, "Hotel A", location, check_in_date, check_out_date, num_guests, 150.0))
        self.hotels.append(Hotel(2, "Hotel B", location, check_in_date, check_out_date, num_guests, 200.0))
        self.hotels.append(Hotel(3, "Hotel C", location, check_in_date, check_out_date, num_guests, 250.0))
        print("Available hotels:")
        for hotel in self.hotels:
            print(hotel)

    def book_flight(self, id, origin, destination, date, num_passengers, price):
        flight = Flight(id, origin, destination, date, num_passengers, price)
        self.reservations[flight.confirmation_number] = flight
        print(f"Flight booked! Confirmation number: {flight.confirmation_number}")

    def book_hotel(self, id, name, location, check_in_date, check_out_date, num_guests, price):
        hotel = Hotel(id, name, location, check_in_date, check_out_date, num_guests, price)
        self.reservations[hotel.confirmation_number] = hotel
        print(f"Hotel booked! Confirmation number: {hotel.confirmation_number}")

    def cancel_reservation(self, confirmation_number):
        if confirmation_number in self.reservations:
            del self.reservations[confirmation_number]
            print(f"Reservation cancelled. Confirmation number: {confirmation_number}")
        else:
            print(f"No reservation found with confirmation number {confirmation_number}.")

def main():
    app = TravelApp()
    while True:
        print("1. Search for flights")
        print("2. Search for hotels")
        print("3. Book a flight")
        print("4. Book a hotel")
        print("5. Cancel a reservation")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            date = input("Enter date: ")
            num_passengers = int(input("Enter number of passengers: "))
            app.search_flights(origin, destination,)