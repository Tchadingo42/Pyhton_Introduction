#affectation multiple fonction / retour multiple fonction / conteneur immuable
my_tuple = (12, 13)

print(type(my_tuple))
print(my_tuple[0])

def get_player_position():
    pos_x = 148
    pos_y = 82

    return (pos_x, pos_y)

coord_x = 0
coord_y = 0

print("The player positon before moving is {} {}" .format(coord_x, coord_y))

(coord_x, coord_y) = get_player_position()

coord_x = 150
coord_y = 150

print("player position : {} {}".format(coord_x, coord_y))
