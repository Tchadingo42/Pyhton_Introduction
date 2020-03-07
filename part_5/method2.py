#self methode standard
#cls + classmethod method de class
#staticmethod   methode statique

class Human:
    current_city = "Paris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_city(cls, new_city):
        Human.current_city = new_city
        
    change_city = classmethod(change_city)

    def ft_function():
        print("Here is the static method")

    ft_function = staticmethod(ft_function)

h1 = Human("Chris", 22)

print("The current city where {} is living is {} " .format(h1.name,
    h1.current_city))

Human.change_city("Gold Coast")
print("The new city where {} is living is {} :)" .format(h1.name,
    h1.current_city))

Human.ft_function()
