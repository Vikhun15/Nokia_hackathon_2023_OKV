import os
def TransformData(toppings, size, extras):
    myDict = {}
    myDict["id"] = 0
    myDict["toppings"] = toppings
    myDict["size"] = size
    myDict["extras"] = extras
    for i in myDict.keys():
        print(i, myDict[i])
    return myDict

def ExportData(data:dict):
    with open("orders.txt", "a", encoding="utf-8") as f:
        for i in data.keys():
            f.write(i + ":" + str(data[i]) + "\n")
