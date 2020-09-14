# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:     #this is the base class
    def __init__(self):
        pass 

class GroundVehicle(Vehicle):  # Inherits vehicle class 
    def __init__(self):
        pass 
    
class Car(GroundVehicle): # Inherits GroundVehicle 
    def __init__(self):
        pass 

class Motorcycle(GroundVehicle):  # Inherits GroundVehicle
    pass

class FlightVehicle(Vehicle):  # Inherits Vehicle
    def __init__(self):
        pass 


class Airplane(FlightVehicle):  # Inherits FlightVehicle
    def __init__(self):
        pass 

class Starship(FlightVehicle): # Inherits FlightVehicle
    def __init__(self):
        pass 





