import datetime
from datetime import datetime
import Tkinter
from Tkinter import *


class EdwinButtons():

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text = datetime.now().time(), command = self.watch)
        self.printButton.pack(side = LEFT)

        self.quitButton = Button(frame, text = 'quit', command = frame.quit) #This breaks main loop
        self.quitButton.pack(side = LEFT)

    def watch(self):
        print datetime.now()


root = Tk()
edwin = EdwinButtons(root)
root.mainloop()

#Displays the current time using the Tkinter library.
