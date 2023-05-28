from enum import Enum
import random

# Ez a fájl építi fel a pályát és helyezi el a kígyót


# Az irány meghatározására szolgáló enumeráció
class Dir(Enum):
    BAL = "balra"
    JOBB = "jobbra"
    FEL = "fel"
    LE = "le"


# A Kígyó oszztályunk
class Snake:
    x = 0
    y = 0


# A kígyó részeit tartalmazó lista, a 0. elemmel (fejjel)
snakes = [Snake()]


# Ez a függvény felel azért, hogy a követelményeknek megfelelően épüljön fel a pálya
def CreateMap():
    myMatrix = []

    yc = 30
    xc = 60

    for i in range(yc + 2):
        sublist = []
        for j in range(xc + 2):
            if i == 0 or i == yc+1 or j == 0 or j == xc+1:
                sublist.append("*")
            else:
                sublist.append(" ")
        myMatrix.append(sublist)

    y = random.randint(1, yc)
    x = random.randint(1, xc)

    myMatrix[y][x] = "@"
    snakes[0].x = x
    snakes[0].y = y
    SpawnCherry(myMatrix)
    DrawMap(myMatrix)
    return myMatrix


# Ez a függvény hozza létre random pozicióban a térképen a "cseresznyét"
def SpawnCherry(myMatrix):
    y = random.randint(1, len(myMatrix)-1)
    x = random.randint(1, len(myMatrix[0])-1)

    while myMatrix[y][x] == "@" or myMatrix[y][x] == "*":
        y = random.randint(1, len(myMatrix)-1)
        x = random.randint(1, len(myMatrix[0])-1)
    else:
        myMatrix[y][x] = "$"


# Ez a függvény rajzolja ki a 2 Dimenziós mátrixot
def DrawMap(myMatrix):
    for i in myMatrix:
        for j in i:
            print(j, end="")
        print("\n", end="")


# Ez a függvény ellenőrzi, hogy a megadott írányba a paraméterként adott karakter van-e
def CheckPath(myMatrix, dir, char):
    if dir.name == "BAL":
        if myMatrix[snakes[0].y][snakes[0].x-1] != char:
            return True
        else:
            return False
    if dir.name == "JOBB":
        if myMatrix[snakes[0].y][snakes[0].x+1] != char:
            return True
        else:
            return False
    if dir.name == "FEL":
        if myMatrix[snakes[0].y-1][snakes[0].x] != char:
            return True
        else:
            return False
    if dir.name == "LE":
        if myMatrix[snakes[0].y+1][snakes[0].x] != char:
            return True
        else:
            return False


# A Kígyó mozgatására szolgáló algoritmus
def MoveSnake(dir, myMatrix):

    result = CheckPath(myMatrix, dir, "*")
    cherry = CheckPath(myMatrix, dir, "$")

    if not cherry:
        snakes.append(Snake())
        SpawnCherry(myMatrix)
        print(len(snakes))
        for i in snakes:
            print(i.x, i.y)

    for i in snakes:
        myMatrix[i.y][i.x] = " "

    if len(snakes) > 1:
        for i in range(len(snakes)-1, 0, -1):
            snakes[i].x = snakes[i - 1].x
            snakes[i].y = snakes[i - 1].y
    if dir.name == "BAL":
        snakes[0].x -= 1
    if dir.name == "JOBB":
        snakes[0].x += 1
    if dir.name == "FEL":
        snakes[0].y -= 1
    if dir.name == "LE":
        snakes[0].y += 1
    for i in snakes:
        myMatrix[i.y][i.x] = "@"
    return not result


if __name__ == "__main__":
    myMatrix = CreateMap()
