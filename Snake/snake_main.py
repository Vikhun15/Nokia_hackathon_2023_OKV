import map
from map import Dir


meguntam = False

myMatrix = map.CreateMap()

while not meguntam:
    state = input("Hova?\n")
    if state.lower() == "meguntam":
        meguntam = True
    elif state.lower() not in ["balra", "jobbra", "fel", "le"]:
        print("Rossz bemenet! [balra, jobbra, fel, le]")
    else:
        meguntam = map.MoveSnake(Dir(state.lower()), myMatrix)
        map.DrawMap(myMatrix)
else:
    print("Most ennyi volt, szép napot!")