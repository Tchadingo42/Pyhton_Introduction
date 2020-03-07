class Human:
    def __init__(self, name, age):
        print("Ningen creation ...")
        self.c_name = name
        self.c_age = age

    def get_age(self):
        try:
            return(self.c_age)
        except AttributeError:
            print("It does not exist !")

    def set_age(self, new_age):
        self.c_age = new_age
        if (new_age < 0):
            self.c_age = 0
        else:
            selc.c_age = new_age

    def del_age(self):
        del self.c_age

    age = property(get_age, set_age, del_age)

h1 = Human("Chris", 22)

help(Human)
print(h1.age)
