class Vehicle:

    colour = "White"

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    #def seating_capacity(self, capacity):
        #return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):

    def final_amount(self):
        final_amount = self.fare() + (self.fare()/10)
        return final_amount


class Car(Vehicle):
    pass


School_bus = Bus("School Volvo", 180, 12, 50)


#print("Colour:", School_bus.colour, "Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
print("Bus fare is", School_bus.final_amount())
print(isinstance(School_bus, Vehicle))