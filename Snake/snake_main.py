import map
from map import Dir

# Ez a fájl a "fő" futtatója a játéknak, itt kapja meg az információt és itt is hívja meg a szükséges függvényeket

meguntam = False

myMatrix = map.CreateMap()

while not meguntam:
    state = input("Hova?\n")
    if state.lower().split(" ")[0] == "meguntam":
        meguntam = True
    elif state.lower().split(" ")[0] not in ["balra", "jobbra", "fel", "le"]:
        print("Rossz bemenet! [balra, jobbra, fel, le]")
    else:
        if len(state.split(" ")) > 1:
            steps = int(state.split(" ")[1])
        else:
            steps = 1
        for i in range(steps):
            meguntam = map.MoveSnake(Dir(state.lower().split(" ")[0]), myMatrix)
            map.DrawMap(myMatrix)
            if meguntam:
                break
else:
    print("Most ennyi volt, szép napot!")
