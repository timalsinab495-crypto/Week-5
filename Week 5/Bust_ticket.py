# Question 4 - Bus Ticket Booking
# Sajha Yatayat

class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = {}  

    def book_seat(self, seat_number, passenger_name):
        if seat_number in self.booked:
            print(f"Seat {seat_number} already booked")
        else:
            self.booked[seat_number] = passenger_name
            print(f"Seat {seat_number} booked for {passenger_name}")

    def available_seats(self):
        return self.total_seats - len(self.booked)

    def passenger_list(self):
        print("\n--- Passenger List ---")
        for seat, name in sorted(self.booked.items()):
            print(f"  Seat {seat}: {name}")


bus = Bus("Kathmandu - Pokhara", 10)

bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),       # duplicate
    (1, "Prakash Magar"),
    (7, "Suman Tamang"),    # duplicate
]

print(f"Route: {bus.route}\n")
for seat, name in bookings:
    bus.book_seat(seat, name)

print(f"\nAvailable Seats: {bus.available_seats()}")
bus.passenger_list()