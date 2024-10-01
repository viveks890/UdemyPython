class Flights:
    def __init__(self, id, name, model, origin, destination) -> None:
        self.id = id
        self.name = name
        self.model = model
        self.origin = origin
        self.destination = destination
        self.journey = [self.origin, self.destination]

    def __repr__(self):
        return f"""Flights('{self.name}', '{self.model}')"""
    
    def __str__(self):
        return f"""Flight name is {self.name} and {self.model}"""
    
class ConnectingFlights(Flights):
    def __init__(self, id, name, model, origin, destination):
        super().__init__(id, name, model, origin, destination)
        self.ConnectingFlight = [self.origin, self.destination]

    def stop_input(self):
        prompt = "please add flight stops"
        self.stop = input(prompt)
        return self.stop

    def stops(self):
        self.stop_input()
        self.connect = []

        while self.stop != 'q':
            self.connect.append(self.stop)
            self.stop_input()
        else:
            print(f"Flights stops are {self.connect}")

flight1 = Flights(1,"AirIndia", 2009, "Delhi", "Banglore")
flight2 = ConnectingFlights(2,"GoAir", 2014, "Mumbai", "Kolkata")

flight2.stops()

print(flight1)
print(flight2)

# class PassengerDetails(ConnectingFlights):
#     def __init__(self, id, name, model, origin, destination, connect):
#         super().__init__(id, name, model, origin, destination, connect)
#         self.age = []

    
        