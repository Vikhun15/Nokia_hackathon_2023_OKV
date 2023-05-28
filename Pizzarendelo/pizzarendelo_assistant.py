import time

# Globális változók

# Lehetséges pizza típusok
pizzatypes = ["pepperoni", "eggplant", "salami"]

# Lehetséges pizza méretek
pizzasizes = ["small", "medium", "large"]

# Lehetséges, opcionális extrák
extras = ["coke", "pepsi", "water", "fanta"]

#  Egy gyors algoritmus, hogy megnézzük, hányszor tartalmazza a szöveg a keresett szót
def Count(elem, list):
    count = 0
    for i in list:
        if i == elem:
            count += 1
    return count

# Egy algoritmus ami visszaadja a legelső előfordulását a keresett lista akármelyik elemének
def LinSearch(what, where):
    for i in what:
        if i in where:
            return i

# Egy függvény, ami formázza a kiírt lista elemeket
# Ha az utolsó elem, akkor "."-ra végződik,
# ha az utolsó előtti, akkor " and "-ra végződik
# egyébként meg ", "-re
def PrintMultpiple(list):
    str = ""
    if len(list) > 1:
        for i in list:
            if i in list[0:-2]:
                str += i + ", "
            elif i == list[-1]:
                str += i + ""
            else:
                str += i + " and "
    else:
        str = list[0]
    return str

# Egy függvény ami addig vár, amíg nem kap választ a GUI
def GetAnswer(my_gui, stopped):
    while not my_gui.gotAnswer:
        time.sleep(0.5)
        if stopped():
            return ""
    else:
        ipt = my_gui.latest_message
        my_gui.gotAnswer = False
    return ipt

# A függvény, ami a futásideje alatt megállapítja a felhasználó által preferált pizza típust
def PizzaType(my_gui, stopped):
    while True:
        my_gui.Addelem("Assistant: Hello ! Welcome to our pizza restaurant. What can I get you today?\n")
        if stopped():
            return ""
        ipt = GetAnswer(my_gui, stopped)

        if any(ele in ipt.lower() for ele in pizzatypes):
            my_gui.Addelem("Assistant: The kind of pizza you want is: ")
            types = list(ele for ele in pizzatypes if(ele in ipt.lower()))
            my_gui.Addelem(PrintMultpiple(types))
            my_gui.Addelem("\nAssistant: Is that right?\n")
            ipt = GetAnswer(my_gui, stopped)

            if ipt.lower() in ["y", "yes"]:
                my_gui.Addelem("Assistant: Great choice!\n")
                return types
        else:
            my_gui.Addelem("Assistant: I'm sorry, but we do not have that type of pizza topping!\n")

# A függvény, ami a futásideje alatt megállapítja a felhasználó által preferált pizza méretét, illetve akármilyen extrát
def PizzaSize(my_gui, types, stopped):
    while True:
        if stopped():
            return None,None
        my_gui.Addelem("Assistant: Would you like a small, medium or large ")
        for i in types:
            my_gui.Addelem(i + " ")
        my_gui.Addelem("pizza?\n")
        ipt = GetAnswer(my_gui, stopped)
        if Count(True, list(ele in ipt.lower() for ele in pizzasizes)) == 1:
            size = LinSearch(pizzasizes, ipt)
            extra = list(ele for ele in extras if(ele in ipt.lower()))
            my_gui.Addelem("Assistant: The size of pizza you want is: " + size + " ")
            if len(extra) > 0:
                my_gui.Addelem("with a ")
                my_gui.Addelem(PrintMultpiple(extra))
            my_gui.Addelem("\nAssistant: Is that right?\n")
            ipt = GetAnswer(my_gui, stopped)
            if ipt.lower() in ["y", "yes"]:
                return size, extra
        else:
            my_gui.Addelem("Assistant: Your choice doesn't seem to be right, please choose from the available sizes!")

# A végső összesítés
def Final(my_gui, types, size, extra):
    my_gui.Addelem(f"Assistant: Your final order is a {size} pizza with ")
    my_gui.Addelem(PrintMultpiple(types) + " ")
    my_gui.Addelem("toppings")
    if len(extra) > 0:
        my_gui.Addelem(" with " + PrintMultpiple(extra))

    my_gui.Addelem(".\n")


# Egy függvény, ami addig vár, amíg nem kapja meg a megfelelő bemeneti értéket a felhasználótól
def WaitForInput(my_gui, string, stopped):
    return string in GetAnswer(my_gui, stopped).lower()

