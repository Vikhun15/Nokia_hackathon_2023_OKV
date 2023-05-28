import tkinter as tk
import threading
import time
import multiprocessing
from pizzarendelo_assistant import PizzaType, PizzaSize, Final, WaitForInput
from pizzarendelo_file import TransformData, ExportData


def Main():

    # Globális változó, ami tartalmazza a kommunikációs szálat
    gui_thread = threading.Thread()
    event = threading.Event()

    # A GUI-nk osztálya, a konstruktőrben építi fel az interface-t
    class PizzarendeloGUI:
        def __init__(self, master):
            self.master = master
            master.title("Pizza ordering")

            # A változó ami őrzi azt, hogy kapott-e üzenetet a gui, illetve, hogy mi volt az
            self.gotAnswer = False
            self.latest_message = ""

            self.label = tk.Label(master, text="Pizza ordering", height=3)
            self.label.pack()

            self.scrolltext = tk.Scrollbar(root, orient="vertical")
            self.scrolltext.pack(side="right", fill="y")

            self.texts = tk.Text(width=90, height=15, yscrollcommand=self.scrolltext.set, wrap="word")
            self.texts.config(state="disabled")
            self.texts.pack()

            self.scrolltext.config(command=self.texts.yview)

            self.message = tk.Text(width=60, height=1)
            self.message.pack(side="left", padx=(60, 0))

            self.send_message = tk.Button(master, text="Send", height=1, width=20, command=self.SentMessage)
            self.send_message.pack(side="right", padx=(0, 60))

            master.bind('<Return>', self.SentMessage)

        # Elem hozzáadása a textbox-hoz
        def Addelem(self, elem):
            self.texts.config(state="normal")
            self.texts.insert("end", elem)
            self.texts.see("end")
            self.texts.config(state="disabled")

        # Az üezenet küldésének Event-je
        def SentMessage(self, event=None):
            self.Addelem("User:  " + self.message.get("1.0", "end").replace("\n", "") + "\n")
            self.latest_message = self.message.get("1.0", "end").replace("\n", "")
            self.message.delete("1.0", "end")
            self.gotAnswer = True

    root = tk.Tk()
    root.geometry("800x400")
    my_gui = PizzarendeloGUI(root)

    stopped = False

    # A függvény, ami irányítja a felhasználó - "bot" kommunikációját
    def Run(stopped):
        ordering = True
        while True:
            if ordering:
                types = PizzaType(my_gui, stopped)
                time.sleep(1)
                size, extra = PizzaSize(my_gui, types, stopped)
                time.sleep(1)
                Final(my_gui, types, size, extra)
                export = TransformData(types, size, extra)
                ExportData(export)
                ordering = False
                my_gui.Addelem("Assistant: Thank you for your order, your order is being prepared. =)\n")
                my_gui.Addelem("Assistant: If you want to continue ordering, please say 'order'"
                               " and our assistant will be with you shortly!\n")
            else:
                if stopped():
                    break
                time.sleep(0.5)
                ordering = WaitForInput(my_gui, "order", stopped)

    gui_thread = threading.Thread(target=Run, args=(lambda : stopped, ))
    gui_thread.start()
    root.mainloop()
    stopped = True
    gui_thread.join()
    # A gui kilépésének problémája "megoldva", de még mindig nem optimális
    # Most nem tervezem újra az alkalmazást, de a megoldás a "stopped" bool körbepasszolása
    # Addig csak kilépéskor dob "RuntimeError"-t a program, az még megfelelő
