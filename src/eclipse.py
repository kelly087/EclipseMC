from tkinter import *
from tkinter import ttk
import fleetbuilder

class Application:
    def __init__(self):
        root = Tk()
        root.title("Battle Simulator")

        mainframe = ttk.Frame(root, padding="11")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        ttk.Button(mainframe, text="Fleet Builder", width=40, command=self.fleetbuilder).grid(column=1, row=2)
        ttk.Button(mainframe, text="Simulate Battle", width=40, command=self.simulatebattle).grid(column=1, row=3)
        ttk.Button(mainframe, text="Quit", command=lambda: root.destroy(), width=40).grid(column=1, row=4)

        root.mainloop()

    def fleetbuilder(self):
        fleetbuilder.FleetBuilder()

    def simulatebattle(self):
        root = Toplevel()
        root.title("Simulation")

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        mainloop()

if __name__ == '__main__':
    Application()