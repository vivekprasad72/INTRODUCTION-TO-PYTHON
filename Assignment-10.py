class Transport:
    def __init__(self, type):
        self.type = type


class Bus(Transport):
    def __init__(self, type, seat_no, source, destination):
        super().__init__(type)   # Initialize Transport variable
        self.seat_no = seat_no
        self.source = source
        self.destination = destination

    def display(self):
        print("Transport Type:", self.type)
        print("Seat No:", self.seat_no)
        print("Source:", self.source)
        print("Destination:", self.destination)


# Creating Bus object
b = Bus("Public Transport", 25, "Jamshedpur", "Ranchi")

# Display
b.display()