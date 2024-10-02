class Car:
    def __init__(self, name, make, year, ownership) -> None:
        self.name = name
        self.year = year
        self.make = make
        self.ownership = ownership

    @classmethod
    def creator(cls, name, make, year):
        """_summary_

        Args:
            name (_type_): _description_
            make (_type_): _description_
            year (_type_): _description_

        Returns:
            _type_: _description_
        """
        ownership = 2024-year
        return cls(name, make, year, ownership)

class Garage:
    def __init__(self, make, year) -> None:
        self.make = make
        self.year = year
        self.cars = []

    def __repr__(self) -> str:
        return f"Garage('{self.make}',{self.year})"
    
    def add_cars(self, car):
        if not isinstance(car, Car):
            raise TypeError()
        

car1 = Car.creator('Focus', 'Ford', 1994)

print(car1.ownership)