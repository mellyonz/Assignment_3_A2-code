# created by Kieran Jerry Jonathon
import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox


class GuiInterface:
    master = tkinter.Tk()
    canvas = tkinter.Canvas(master, bg='white', width=500, height=500)

    def __init__(self, source_reader):
        self.canvas.pack(side='bottom', fill='x', expand='yes')
        self.init_widgets()
        self.SourceReader = source_reader

    def init_widgets(self):
        self.master.title('TkinterGUI')
        width = 1200
        height = 600
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()
        center = '%dx%d+%d+%d' % (width, height, (screenwidth - 800) / 2, (screenheight - height) / 2)
        self.master.geometry(center)
        self.master.draw_btn = Button(self.master, text='Draw', command=self.draw)
        self.master.draw_btn.pack(side='left', fill='both', expand='yes')
        self.master.import_btn = Button(self.master, text='import', command=self.to_import)
        self.master.import_btn.pack(side='left', fill='both', expand='yes')

        self.master.selectDrawer = tkinter.Label(self.master, text="Select Drawer")
        self.master.selectDrawer.pack(side='left', fill='both', expand='yes')

        self.master.comboDrawer = Combobox(self.master, values=["DrawerJack", "DrawerKieran", "DrawerTurtleJack"])
        # self.master.comboDrawer.set(self.config[0])
        self.master.comboDrawer.pack(side='left', fill='both', expand='yes')

        self.master.selectParser = tkinter.Label(self.master, text="Select Parser")
        self.master.selectParser.pack(side='left', fill='both', expand='yes')

        self.master.selectInterface = tkinter.Label(self.master, text="Select Interface")
        self.master.selectInterface.pack(side='left', fill='both', expand='yes')

        self.master.close_btn = Button(self.master, text='Restart', command=self.restart_program)
        self.master.close_btn.pack(side='left', fill='both', expand='yes')

        self.master.instruction = Label(self.master, text='Please enter command:', font=('serif', 18))
        self.master.instruction.pack(side='left', fill='both', expand='yes')

        self.master.text = Text(self.master, height=27, width=32)
        self.master.text.pack(side='left', fill='both', expand='yes')

    def draw(self):
        # print(self.text.get(1.0, "end-1c"))
        self.SourceReader.parser.parse(self.master.text.get(1.0, "end-1c"))

    def restart_program(self):
        """Crashes the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        file = open('config.txt', 'w')
        file.write(self.master.comboDrawer.get() + '\n'
                   + self.master.comboParser.get() + '\n'
                   + self.master.comboInterface.get())
        file.close()
        self.master.destroy()

    def insert_text(self, row_source):
        self.master.text.insert('0.0', row_source)

    def to_import(self):
        self.importedFile = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                                       filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        if self.importedFile is not '':
            self.insert_text(open(self.importedFile, "r+").read())

    def start(self):
        self.master.mainloop()
