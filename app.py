from tkinter import *
from tkinter import ttk
from inputSet import newset
from tktooltip import ToolTip
from colors import *
from displayResult import getResult
root = Tk()

screen_width = 750
screen_height = 400


class windowFrame:
    def __init__(self):
        self.window=root
        self.mainWindow(screen_width, screen_height)
        self.frameButtons()


    # Main window frame
    def mainWindow(self, width, height):
        self.window.title('PPE - Program for Prelim Exam')
        self.window.iconbitmap("resources/ico/brain.ico")
        self.window.geometry(f"{width}x{height}")
        self.window.resizable(False, False)
        self.window.configure(bg=bg)
    
    # Buttons
    def frameButtons(self):
        self.createSet = Button(
                                self.window, 
                                bg=bgMain,
                                activebackground=activeBG,
                                activeforeground=fg,
                                text="+ Create Set", 
                                justify="center",
                                fg="white",
                                font="sans 10 bold",
                                borderwidth=0,
                                height= 2, 
                                width=20,
                                command=lambda: newset(self.window) 
                        )

       # Deploy buttons
        self.createSet.place(x=640,y=78, anchor="center")
        self.createSet.bind("<Enter>", self.on_enter_createSet)
        self.createSet.bind("<Leave>", self.on_leave_createSet)
        

    def on_enter_createSet(self, e):
        self.createSet.config(background=hoverBG, foreground=fg, cursor="hand2")
    
    def on_leave_createSet(self, e):
        self.createSet.config(background=bgMain, foreground=fg)


        
if __name__ == "__main__":
    getFrame = windowFrame()
    getFrame.window.mainloop()