class Human:
    def __init__(self, name, age):
        self.c_name = name
        self.c_age = age

    def get_age(self):
        if self.c_age <= 1:
            return(" {} {}" .format(self.c_age, text1))
        else:
            return(" {} {}" .format(self.c_age, text2))
        
        age = property(get_age)

text1 = "years old"
text2 = "years old"

h1 = Human("chris", 22)
print("{} is {}" .format(h1.name, h1.age))
