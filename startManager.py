from tkinter import *
from tkinter.font import *

class Main:
    def __init__(self, master):
        
        #Creates Main Window
        Win.buildMainWindow(self, master)
 
class Win: 
    def buildMainWindow(self, master):
        # User can interact with Main Window after successfully logging in
        # Window is created then set off-screen

        self.master = master
        self.window_main = master

        self.window_main.geometry('1200x800+300+100')
        #self.window_main.geometry(f'{winStat.getScreenSize("x")}x{winStat.getScreenSize("y")}+0+0')
        self.window_main.overrideredirect(True)
        self.window_main.title("Window app")


        keyInput.addHotKey(master, "<Escape>", lambda event, r=self.window_main: keyInput.escape(event, r))


        #btn = Button(self.window_main, text="Create a widget", command= lambda s=master: WidgetCreation.create(s))
        #btn.pack(pady = 10) 

class winStat:
    def getScreenSize(v):
        if v == 'x':
            return root.winfo_screenwidth()
        return root.winfo_screenheight()

class keyInput:
    def addHotKey(root, key, command):
        root.bind(key, command)

    def escape(event, root):
        root.destroy()


class WidgetCreation:
    def create(rootlevel):
        win = Toplevel(rootlevel)
        win.geometry('800x600+0+0')
        win.overrideredirect(False)

root = Tk()
window = Main(root)
root.mainloop()