"""
human class
"""
class Human:
    def __init__(self):
        print("Human creation ...")
        self.name = "Chris"
        self.age = 22
        print(self)

print("Launch Program ...\n")

#instance de class en creant un objet
human_1 = Human()
print("human_1 name {}" .format(human_1.name))
print("human_1 name {}" .format(human_1.age))
