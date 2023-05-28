import tkinter as tk
import threading
import time
from pizzarendelo_assistant import PizzaType, PizzaSize, Final, WaitForInput
from pizzarendelo_file import TransformData, ExportData


def Main():

    gui_thread = threading.Thread()
    class PizzarendeloGUI:
        def __init__(self, master):
            self.master = master
            master.title("Pizza ordering")

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


        def addelem(self, elem):
            self.texts.config(state="normal")
            self.texts.insert("end", elem)
            self.texts.see("end")
            self.texts.config(state="disabled")

        def SentMessage(self, event=None):
            self.addelem("User:  " + self.message.get("1.0", "end").replace("\n", "") + "\n")
            self.latest_message = self.message.get("1.0", "end").replace("\n", "")
            self.message.delete("1.0", "end")
            self.gotAnswer = True


    root = tk.Tk()
    root.geometry("800x400")
    my_gui = PizzarendeloGUI(root)

    def Run():
        ordering = True
        while True:
            if ordering:
                types = PizzaType(my_gui)
                time.sleep(1)
                size, extra = PizzaSize(my_gui, types)
                time.sleep(1)
                Final(my_gui, types, size, extra)
                export = TransformData(types, size, extra)
                ExportData(export)
                ordering = False
                my_gui.addelem("Assistant: Thank you for your order, your order is being prepared. =)\n")
                my_gui.addelem("Assistant: If you want to continue ordering, please say 'order'"
                               " and our assistant will be with you shortly!\n")
            else:
                time.sleep(0.5)
                ordering = WaitForInput(my_gui)


    def thread():
        gui_thread = threading.Thread(target=Run)
        gui_thread.start()
    thread()
    root.mainloop()


