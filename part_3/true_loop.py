launcher = True
print()

while launcher:
    choose_menu = input("choose a menu ")

    if choose_menu == "again":
        continue
    elif choose_menu == "quit":
        launcher = False
    elif choose_menu == "hello":
        print("Hello there")
    else:
        print("unknow command")

