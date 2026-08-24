class Transport:
    def __init__(self, type):
        self.type = type

    def show(self):
        print("Type of Transport:", self.type)


class Boat(Transport):
    def __init__(self, type, capacity, source, destination):
        super().__init__(type)
        self.capacity = capacity
        self.source = source
        self.destination = destination

    def show(self):
        super().show()
        print("Capacity:", self.capacity)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print()


class Bus(Transport):
    def __init__(self, type, seat_no, source, destination):
        super().__init__(type)
        self.seat_no = seat_no
        self.source = source
        self.destination = destination

    def show(self):
        super().show()
        print("Seat No.:", self.seat_no)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print()


boat1 = Boat("Water Transport", 50, "Kolkata", "Port Blair")
boat2 = Boat("Water Transport", 100, "Mumbai", "Goa")

bus1 = Bus("Road Transport", 25, "Kolkata", "Durgapur")
bus2 = Bus("Road Transport", 40, "Delhi", "Jaipur")


print("----- BOAT RECORDS -----")
boat1.show()
boat2.show()

print("----- BUS RECORDS -----")
bus1.show()
bus2.show()