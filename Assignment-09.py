class Transport:
    def getval(self, type):
        self.type = type

    def show(self):
        print("Transport Type:", self.type)


class Bus(Transport):
    def input(self, seat_no, source, destination):
        self.seat_no = seat_no
        self.source = source
        self.destination = destination

    def display(self):
        print("Transport Type:", self.type)
        print("Seat No:", self.seat_no)
        print("Source:", self.source)
        print("Destination:", self.destination)


b = Bus()

b.getval("Road transport")

b.input(25, "Jamshedpur", "Ranchi")

b.display()