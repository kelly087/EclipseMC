from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os.path

class FleetBuilder:
    def __init__(self):
        # Tk root
        root = Toplevel()
        root.title("Fleet Builder")
        root.geometry("1200x275")

        mainframe = ttk.Frame(root)
        mainframe.pack(fill=BOTH, expand=1)

        # Load Images
        self.images = {}
        self.images['blank'] = PhotoImage(file="images/80.png")
        self.images['ion_cannon'] = PhotoImage(file="images/ion_cannon.png")
        self.images['hull'] = PhotoImage(file="images/hull.png")
        self.images['nuclear_drive'] = PhotoImage(file="images/nuclear_drive.png")
        self.images['nuclear_source'] = PhotoImage(file="images/nuclear_source.png")
        self.images['electron_computer'] = PhotoImage(file="images/electron_computer.png")
        self.images['plasma_cannon'] = PhotoImage(file="images/plasma_cannon.png")
        self.images['plasma_missile'] = PhotoImage(file="images/plasma_missile.png")
        self.images['positron_computer'] = PhotoImage(file="images/positron_computer.png")
        self.images['gluon_computer'] = PhotoImage(file="images/gluon_computer.png")
        self.images['antimatter_cannon'] = PhotoImage(file="images/antimatter_cannon.png")
        self.images['improved_hull'] = PhotoImage(file="images/improved_hull.png")
        self.images['gauss_shield'] = PhotoImage(file="images/gauss_shield.png")
        self.images['phase_shield'] = PhotoImage(file="images/phase_shield.png")
        self.images['fusion_drive'] = PhotoImage(file="images/fusion_drive.png")
        self.images['tachyon_drive'] = PhotoImage(file="images/tachyon_drive.png")
        self.images['fusion_source'] = PhotoImage(file="images/fusion_source.png")
        self.images['tachyon_source'] = PhotoImage(file="images/tachyon_source.png")
        self.images['axion_computer'] = PhotoImage(file="images/axion_computer.png")
        self.images['conifold_field'] = PhotoImage(file="images/conifold_field.png")
        self.images['flux_missile'] = PhotoImage(file="images/flux_missile.png")
        self.images['flux_shield'] = PhotoImage(file="images/flux_shield.png")
        self.images['hypergrid_source'] = PhotoImage(file="images/hypergrid_source.png")
        self.images['interceptor_bay'] = PhotoImage(file="images/interceptor_bay.png")
        self.images['ion_disruptor'] = PhotoImage(file="images/ion_disruptor.png")
        self.images['ion_turret'] = PhotoImage(file="images/ion_turret.png")
        self.images['jump_drive'] = PhotoImage(file="images/jump_drive.png")
        self.images['morph_shield'] = PhotoImage(file="images/morph_shield.png")
        self.images['muon_source'] = PhotoImage(file="images/muon_source.png")
        self.images['sentient_hull'] = PhotoImage(file="images/sentient_hull.png")
        self.images['shard_hull'] = PhotoImage(file="images/shard_hull.png")
        self.images['zero-point_module'] = PhotoImage(file="images/zero-point_module.png")

        # Ship Parts and buttons
        self.iparts = []
        self.iship = ['blank', 'blank', 'blank', 'blank']
        self.cparts = []
        self.cship = ['blank', 'blank', 'blank', 'blank', 'blank', 'blank']
        self.dparts = []
        self.dship = ['blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank']
        self.sparts = []
        self.sship = ['blank', 'blank', 'blank', 'blank', 'blank']

        # Save/Load Buttons
        ttk.Button(mainframe, text="Save", command=self.save).place(x=5, y=5)
        ttk.Button(mainframe, text="Load", command=self.load).place(x=85, y=5)

        # Build Interceptor
        Label(mainframe, text="Interceptor: Base 2 Initiative").place(x=10, y=250)

        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(1, 1), borderwidth=0)
        b.place(x=0, y=120)
        self.iparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(1, 2), borderwidth=0)
        b.place(x=80, y=80)
        self.iparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(1, 3), borderwidth=0)
        b.place(x=80, y=160)
        self.iparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(1, 4), borderwidth=0)
        b.place(x=160, y=120)
        self.iparts.append(b)

        # Build Cruiser
        Label(mainframe, text="Cruiser: Base 1 Initiative").place(x=330, y=250)

        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(2, 1), borderwidth=0)
        b.place(x=320, y=80)
        self.cparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(2, 2), borderwidth=0)
        b.place(x=320, y=160)
        self.cparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(2, 3), borderwidth=0)
        b.place(x=400, y=40)
        self.cparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(2, 4), borderwidth=0)
        b.place(x=400, y=120)
        self.cparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(2, 5), borderwidth=0)
        b.place(x=480, y=80)
        self.cparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(2, 6), borderwidth=0)
        b.place(x=480, y=160)
        self.cparts.append(b)

        # Build Dreadnaught
        Label(mainframe, text="Dreadnaught: Base 0 Initiative").place(x=650, y=250)

        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(3, 1), borderwidth=0)
        b.place(x=640, y=0)
        self.dparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(3, 2), borderwidth=0)
        b.place(x=640, y=80)
        self.dparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(3, 3), borderwidth=0)
        b.place(x=640, y=160)
        self.dparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(3, 4), borderwidth=0)
        b.place(x=720, y=40)
        self.dparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(3, 5), borderwidth=0)
        b.place(x=720, y=120)
        self.dparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(3, 6), borderwidth=0)
        b.place(x=800, y=0)
        self.dparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(3, 7), borderwidth=0)
        b.place(x=800, y=80)
        self.dparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(3, 8), borderwidth=0)
        b.place(x=800, y=160)
        self.dparts.append(b)

        # Build Starbase
        Label(mainframe, text="Starbase: Base 4 Initiative").place(x=970, y=250)

        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(4, 1), borderwidth=0)
        b.place(x=960, y=80)
        self.sparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(4, 2), borderwidth=0)
        b.place(x=1040, y=0)
        self.sparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(4, 3), borderwidth=0)
        b.place(x=1040, y=80)
        self.sparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(4, 4), borderwidth=0)
        b.place(x=1040, y=160)
        self.sparts.append(b)
        b = Button(mainframe, image=self.images['blank'], command=lambda: self.click(4, 5), borderwidth=0)
        b.place(x=1120, y=80)
        self.sparts.append(b)

        # Default load if human.efU exists
        if os.path.isfile("human.efU"):
            self.loadfromfile("human.efU")

        # Start window loop
        mainloop()

    def click(self, ship, part):
        root = Toplevel()
        root.title("Upgrades")

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        # Build default buttons
        Button(mainframe, image=self.images['blank'], command=lambda: self.callback(root, ship, part, 'blank'), borderwidth=0).grid(row=0, column=0)
        Button(mainframe, image=self.images['ion_cannon'], command=lambda: self.callback(root, ship, part, 'ion_cannon'), borderwidth=0).grid(row=0, column=1)
        Button(mainframe, image=self.images['electron_computer'], command=lambda: self.callback(root, ship, part, 'electron_computer'), borderwidth=0).grid(row=0, column=2)
        Button(mainframe, image=self.images['nuclear_drive'], command=lambda: self.callback(root, ship, part, 'nuclear_drive'), borderwidth=0).grid(row=0, column=3)
        Button(mainframe, image=self.images['nuclear_source'], command=lambda: self.callback(root, ship, part, 'nuclear_source'), borderwidth=0).grid(row=0, column=4)
        Button(mainframe, image=self.images['hull'], command=lambda: self.callback(root, ship, part, 'hull'), borderwidth=0).grid(row=0, column=5)

        # Row 2
        Button(mainframe, image=self.images['plasma_cannon'], command=lambda: self.callback(root, ship, part, 'plasma_cannon'), borderwidth=0).grid(row=1, column=0)
        Button(mainframe, image=self.images['plasma_missile'], command=lambda: self.callback(root, ship, part, 'plasma_missile'), borderwidth=0).grid(row=1, column=1)
        Button(mainframe, image=self.images['positron_computer'], command=lambda: self.callback(root, ship, part, 'positron_computer'), borderwidth=0).grid(row=1, column=2)
        Button(mainframe, image=self.images['gluon_computer'], command=lambda: self.callback(root, ship, part, 'gluon_computer'), borderwidth=0).grid(row=1, column=3)
        Button(mainframe, image=self.images['antimatter_cannon'], command=lambda: self.callback(root, ship, part, 'antimatter_cannon'), borderwidth=0).grid(row=1, column=4)
        Button(mainframe, image=self.images['improved_hull'], command=lambda: self.callback(root, ship, part, 'improved_hull'), borderwidth=0).grid(row=1, column=5)

        # Row 3
        Button(mainframe, image=self.images['gauss_shield'], command=lambda: self.callback(root, ship, part, 'gauss_shield'), borderwidth=0).grid(row=2, column=0)
        Button(mainframe, image=self.images['phase_shield'], command=lambda: self.callback(root, ship, part, 'phase_shield'), borderwidth=0).grid(row=2, column=1)
        Button(mainframe, image=self.images['fusion_drive'], command=lambda: self.callback(root, ship, part, 'fusion_drive'), borderwidth=0).grid(row=2, column=2)
        Button(mainframe, image=self.images['tachyon_drive'], command=lambda: self.callback(root, ship, part, 'tachyon_drive'), borderwidth=0).grid(row=2, column=3)
        Button(mainframe, image=self.images['fusion_source'], command=lambda: self.callback(root, ship, part, 'fusion_source'), borderwidth=0).grid(row=2, column=4)
        Button(mainframe, image=self.images['tachyon_source'], command=lambda: self.callback(root, ship, part, 'tachyon_source'), borderwidth=0).grid(row=2, column=5)

        # Row 4, expansion
        Button(mainframe, image=self.images['conifold_field'], command=lambda: self.callback(root, ship, part, 'conifold_field'), borderwidth=0).grid(row=3, column=0)
        Button(mainframe, image=self.images['interceptor_bay'], command=lambda: self.callback(root, ship, part, 'interceptor_bay'), borderwidth=0).grid(row=3, column=1)
        Button(mainframe, image=self.images['sentient_hull'], command=lambda: self.callback(root, ship, part, 'sentient_hull'), borderwidth=0).grid(row=3, column=2)
        Button(mainframe, image=self.images['flux_missile'], command=lambda: self.callback(root, ship, part, 'flux_missile'), borderwidth=0).grid(row=3, column=3)
        Button(mainframe, image=self.images['zero-point_module'], command=lambda: self.callback(root, ship, part, 'zero-point_module'), borderwidth=0).grid(row=3, column=4)

        # Row 5, discoveries
        Button(mainframe, image=self.images['axion_computer'], command=lambda: self.callback(root, ship, part, 'axion_computer'), borderwidth=0).grid(row=4, column=0)
        Button(mainframe, image=self.images['flux_shield'], command=lambda: self.callback(root, ship, part, 'flux_shield'), borderwidth=0).grid(row=4, column=1)
        Button(mainframe, image=self.images['hypergrid_source'], command=lambda: self.callback(root, ship, part, 'hypergrid_source'), borderwidth=0).grid(row=4, column=2)
        Button(mainframe, image=self.images['ion_disruptor'], command=lambda: self.callback(root, ship, part, 'ion_disruptor'), borderwidth=0).grid(row=4, column=3)
        Button(mainframe, image=self.images['ion_turret'], command=lambda: self.callback(root, ship, part, 'ion_turret'), borderwidth=0).grid(row=4, column=4)
        Button(mainframe, image=self.images['jump_drive'], command=lambda: self.callback(root, ship, part, 'jump_drive'), borderwidth=0).grid(row=4, column=5)
        Button(mainframe, image=self.images['morph_shield'], command=lambda: self.callback(root, ship, part, 'morph_shield'), borderwidth=0).grid(row=4, column=6)

        mainloop()

    def callback(self, destroy_root, ship, part, upgrade):
        destroy_root.destroy()
        # Callback from upgrade window with ship type and part location and the upgrade to give it
        if ship == 1:
            self.iparts[part - 1].configure(image=self.images[upgrade])
            self.iship[part - 1] = upgrade
        elif ship == 2:
            self.cparts[part - 1].configure(image=self.images[upgrade])
            self.cship[part - 1] = upgrade
        elif ship == 3:
            self.dparts[part - 1].configure(image=self.images[upgrade])
            self.dship[part - 1] = upgrade
        elif ship == 4:
            self.sparts[part - 1].configure(image=self.images[upgrade])
            self.sship[part - 1] = upgrade

    def save(self):
        # Saves fleet to file
        file_path = filedialog.asksaveasfilename(defaultextension='.efU', filetypes=[('Eclipse Fleet Units', '.efU')])
        f = open(file_path, 'w')
        f.write(self.iship[0] + ',' + self.iship[1] + ',' + self.iship[2] + ',' + self.iship[3] + '\n')
        f.write(self.cship[0] + ',' + self.cship[1] + ',' + self.cship[2] + ',' + self.cship[3] + ',' + self.cship[4] + ',' + self.cship[5] + '\n')
        f.write(self.dship[0] + ',' + self.dship[1] + ',' + self.dship[2] + ',' + self.dship[3] + ',' + self.dship[4] + ',' + self.dship[5] + ',' + self.dship[6] + ',' + self.dship[7] + '\n')
        f.write(self.sship[0] + ',' + self.sship[1] + ',' + self.sship[2] + ',' + self.sship[3] + ',' + self.sship[4])
        f.flush()
        f.close()

    def load(self):
        # Load dialog
        file_path = filedialog.askopenfilename(defaultextension='.efU', filetypes=[('Eclipse Fleet Units', '.efU')])
        self.loadfromfile(file_path)
    
    def loadfromfile(self, filename):
        # Loads fleet from file
        f = open(filename, 'r')
        count = 0
        for line in f:
            if count == 0:
                self.iship = line.strip().split(',')
            elif count == 1:
                self.cship = line.strip().split(',')
            elif count == 2:
                self.dship = line.strip().split(',')
            elif count == 3:
                self.sship = line.strip().split(',')
            count += 1

        for i in range(len(self.iship)):
            self.iparts[i].configure(image=self.images[self.iship[i]])
        for i in range(len(self.cship)):
            self.cparts[i].configure(image=self.images[self.cship[i]])
        for i in range(len(self.dship)):
            self.dparts[i].configure(image=self.images[self.dship[i]])
        for i in range(len(self.sship)):
            self.sparts[i].configure(image=self.images[self.sship[i]])