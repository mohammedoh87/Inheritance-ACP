class Vehicle:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def display(self):
        print("Vehicle name: {}".format(self.name))
        print("Vehicle number: {}".format(self.number))

class Bus(Vehicle):
    def __init__(self, name, number, fare_per_passenger):
        super().__init__(name, number) 
        self.fare_per_passenger = fare_per_passenger

    def total_fare(self):
        return self.number * self.fare_per_passenger 

    def display_fare(self):
        print("Total Fare for the bus: ${}".format(self.total_fare()))

city_bus = Bus(name="City Bus", number=50, fare_per_passenger=2)

city_bus.display()

city_bus.display_fare()
