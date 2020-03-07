#car_nbr attribut de class
class Car:
    nbr = 0
    def __init__(self, brand, speed, turbo):
        self.brand = brand
        self.speed = speed
        self.turbo = turbo
        Car.nbr += 1

print("Launch Program ...\n")

car = Car("Jaguar", 240, True)
print("This {} can go until {} klm h and there is turbo {} there is now {} car" .format(car.brand,
    car.speed, car.turbo, Car.nbr))

car = Car("Maseratti", 220, False)
print("This {} can go until {} klm h there us turbo {} there is now {} cars" .format(car.brand,
    car.speed, car.turbo, Car.nbr))

