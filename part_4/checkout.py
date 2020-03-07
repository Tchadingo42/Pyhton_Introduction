nb1 = 150

nb2 = input("Choose the number you want for the division -> ")

try:
    nb2 = int(nb2)
    print("res = {}".format(nb2 / nb1))
except ZeroDivisionError:
    print("you cannot done a division by 0 dude !")
except ValueError:
    print("This is not a number mate !")
except:
    print("Invalid value")
else:
    print("Here it is you find a valid number")
finally:
    print("End of program")
