class Garage:
    def __init__(self) -> None:
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]
    

ford = Garage()
ford.cars.append("Fiesta")
ford.cars.append("Focus")


print(len(ford.cars))
print(ford.cars[0])

for car in ford:
    print(car)
