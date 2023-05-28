import time


pizzatypes = ["pepperoni", "eggplant", "salami"]
pizzasizes = ["small", "medium", "large"]
extras = ["coke", "pepsi", "water", "fanta"]

def Count(elem, list):
    count = 0
    for i in list:
        if i == elem:
            count += 1
    return count

def LinSearch(what, where):
    for i in what:
        if i in where:
            return i

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

def GetAnswer(my_gui):
    while not my_gui.gotAnswer:
        time.sleep(0.5)
    else:
        ipt = my_gui.latest_message
        my_gui.gotAnswer = False
    return ipt

def PizzaType(my_gui):
    while True:
        my_gui.addelem("Assistant: Hello ! Welcome to our pizza restaurant. What can I get you today?\n")

        ipt = GetAnswer(my_gui)

        if any(ele in ipt.lower() for ele in pizzatypes):
            my_gui.addelem("Assistant: The kind of pizza you want is: ")
            types = list(ele for ele in pizzatypes if(ele in ipt.lower()))
            my_gui.addelem(PrintMultpiple(types))
            my_gui.addelem("\nAssistant: Is that right?\n")
            ipt = GetAnswer(my_gui)

            if ipt.lower() in ["y", "yes"]:
                my_gui.addelem("Assistant: Great choice!\n")
                return types
        else:
            my_gui.addelem("Assistant: I'm sorry, but we do not have that type of pizza topping!\n")

def PizzaSize(my_gui, types):
    while True:
        my_gui.addelem("Assistant: Would you like a small, medium or large ")
        for i in types:
            my_gui.addelem(i + " ")
        my_gui.addelem("pizza?\n")
        ipt = GetAnswer(my_gui)
        if Count(True, list(ele in ipt.lower() for ele in pizzasizes)) == 1:
            size = LinSearch(pizzasizes, ipt)
            extra = list(ele for ele in extras if(ele in ipt.lower()))
            my_gui.addelem("Assistant: The size of pizza you want is: " + size + " ")
            if len(extra) > 0:
                my_gui.addelem("with a ")
                my_gui.addelem(PrintMultpiple(extra))
            my_gui.addelem("\nAssistant: Is that right?\n")
            ipt = GetAnswer(my_gui)
            if ipt.lower() in ["y", "yes"]:
                return size, extra
        else:
            my_gui.addelem("Assistant: Your choice doesn't seem to be right, please choose from the available sizes!")

def Final(my_gui, types, size, extra):
    my_gui.addelem(f"Assistant: Your final order is a {size} pizza with ")
    my_gui.addelem(PrintMultpiple(types) + " ")
    my_gui.addelem("toppings")
    if len(extra) > 0:
        my_gui.addelem(" with " + PrintMultpiple(extra))

    my_gui.addelem(".\n")
    my_gui.addelem("Assistant: Your order has been placed!\n")

def WaitForInput(my_gui):
    return "order" in GetAnswer(my_gui).lower()