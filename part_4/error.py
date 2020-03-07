user_age = input("How old are you ? ")
#user_age = int(user_age)
#print("So you are {}" .format(user_age))

try:
    user_age = int(user_age)
except:
    print("Incorret age !")
else:
    print("You are ", user_age, "years old")
