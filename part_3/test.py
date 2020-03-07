db_id = "tchadingo"
db_pswd = "We_are_42"
text = "Here we go {} you are connecting now"

print("Conexion to the acount ...\n")
tmp_id = input("please enter your id ")

if (db_id == tmp_id):
    print("Here you are ", db_id)
    print()
else:
    print("Sorry invalid id")

if (db_id == tmp_id):
    tmp_pswd = input("Please enter your password ")
    if db_pswd == tmp_pswd:
        print("Here we go {} you're connecting now".format(db_id))
    else:
        print("Sorry Invalid password")
