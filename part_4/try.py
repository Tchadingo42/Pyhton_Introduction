user_club = input("What's your club mate ? ")

try:
    user_club = int(user_club)
except:
    print("This club doesn't exist mate !")
else:
    print("Oh you're for the {}".format(user_club))
finally:
    print("Goodbye mate !")
