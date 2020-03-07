class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#methode d'instance
    def speak(self, message):
        print("{} just said {}" .format(self.name, str(message)))

h1 = Human("Chris", 22)

h1.speak("Hi")
