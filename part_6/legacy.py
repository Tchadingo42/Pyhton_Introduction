#class mere
#gasoline quantity

class Vehicule:
    def __init__(self, name, gq):
        self.c_name = name
        self.c_gq = gq
    def moving(self):
        print("The car is moving")
#son class
    class Car(Vehicule):
        def __init__(self, power):
            

my_car = Car()
