# Ebben a fájlban találhatóak a fájl kezelő műveletek

# Lekérdezzük az árakat a text fájlból
def GetPrices():
    dict = {}
    with open("prices.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for i in lines:
            temp = i.replace(",", "").replace("\n", "").split(" : ")
            dict[temp[0]] = float(temp[1])
    return dict

# Átalakítjuk az adatot egy dictionary-vé és hozzáadjuk az árakat
def TransformData(toppings, size, extras):
    myDict = {"toppings": toppings, "size": size, "extras": extras, "price": 0}
    prices = GetPrices()
    sum = 0
    count = 0
    for i in myDict["toppings"]:
        sum += prices[i]
        count += 1
    myDict["price"] += sum / count
    myDict["price"] *= prices[myDict["size"]]
    for i in myDict["extras"]:
        myDict["price"] += prices[i]
    myDict["price"] = round(myDict["price"])
    return myDict

def ExportData(data:dict):
    with open("orders.txt", "a", encoding="utf-8") as f:
        for i in data.keys():
            f.write(str(data[i]) + ";")
        f.write("\n")
