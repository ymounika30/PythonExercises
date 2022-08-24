##Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    pass
class School_bus(Vehicle):
    pass
s=School_bus()
print(isinstance(s,Vehicle))
