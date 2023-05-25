from enum import Enum
#Ez a fájl építi fel a pályát és helyezi el a kígyót

class Dir(Enum):
    BAL = "balra"
    JOBB = "jobbra"
    FEL = "fel"
    LE = "le"

class snake:
    x = 0
    y = 0
    


def CreateMap():
    myMatrix = []
    import random

    for i in range(62):
        sublist = []
        for j in range(32):
            if i == 0 or i == 61 or j == 0 or j == 31:
                sublist.append("*")
            else:
                sublist.append(" ")
        myMatrix.append(sublist)

    y = random.randint(1, 60)
    x = random.randint(1, 30)

    myMatrix[y][x] = "@"
    snake.x = x
    snake.y = y
    DrawMap(myMatrix)
    return myMatrix

def DrawMap(myMatrix):
    for i in myMatrix:
        for j in i:
            print(j, end="")
        print("\n", end="")

def CheckPath(myMatrix, dir ):
    if dir.name == "BAL":
        if myMatrix[snake.y][snake.x-1] != "*":
            return True
        else:
            return False
    if dir.name == "JOBB":
        if myMatrix[snake.y][snake.x+1] != "*":
            return True
        else:
            return False
    if dir.name == "FEL":
        if myMatrix[snake.y-1][snake.x] != "*":
            return True
        else:
            return False
    if dir.name == "LE":
        if myMatrix[snake.y+1][snake.x] != "*":
            return True
        else:
            return False

def MoveSnake(dir, myMatrix):
    print(snake.x, snake.y)
    if CheckPath(myMatrix, dir):
        myMatrix[snake.y][snake.x] = " "
        if dir.name == "BAL":
            snake.x -= 1
        if dir.name == "JOBB":
            snake.x += 1
        if dir.name == "FEL":
            snake.y -= 1
        if dir.name == "LE":
            snake.y += 1
        myMatrix[snake.y][snake.x] = "@"
        return False
    else:
        return True





if __name__ == "__main__":
    import random

    myMatrix = CreateMap()







