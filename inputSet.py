from cgitb import text
from tkinter import *
import tkinter
from colors import *
from elements_of_sets import elements

width = 500
height = 320
centerX = width / 2

class newset:
    def __init__(self,root):
        super().__init__()
        self.root = root
        self.setNotationBuilder_var = tkinter.IntVar()
        self.rosterMethod_var = tkinter.IntVar()
        self.display()

    def createEntry(self):
        self.newWindow = Toplevel(self.root)
        self.newWindow.title("Create Set")
        self.newWindow.iconbitmap("resources/ico/brain.ico")
        self.newWindow.geometry(f"{width}x{height}")
        self.newWindow.configure(bg=bg)
        self.newWindow.resizable(False, False)
        self.newWindow.grab_set()
        self.label = Label(
                            self.newWindow,
                            text="Separate your inputs with \",\".   e.g: 1,2,3,4,5",
                            font="sans 10 bold",
                            fg=fg,
                            bg=bg
                        )
        
        self.optionLabel = Label(
                            self.newWindow,
                            text="Options:",
                            font="sans 10 bold",
                            fg=fg,
                            bg=bg
                        )
        
        self.bracket = Label(
                            self.newWindow,
                            text="{                          }",
                            font="sans 20 bold",
                            fg=fg,
                            bg=bg
                        )

        self.entrySet = Entry(
                            self.newWindow,textvariable = "createSetInput",
                            font=('sans',10,'normal'),
                            justify='center',
                            exportselection=0,
                            width=30,
                            borderwidth=0,
                            bg=greyBG,
                            fg=fg
                            )
        self.entrySet.delete(0, END)
        self.entrySet.config(insertbackground=fg)
        self.entrySet.focus()
        self.label.place(x=centerX,y=20, anchor="center")
        self.bracket.place(x=centerX,y=58, anchor="center")
        self.entrySet.place(x=centerX, y=60, anchor="center")
        self.optionLabel.place(x=centerX, y=98, anchor="center")

    def submitButton(self):
        self.submitSet = Button(
                                self.newWindow, 
                                bg=bgMain,
                                activebackground=activeBG,
                                activeforeground=fg,
                                text="Submit", 
                                justify="center",
                                fg="white",
                                font="sans 10 bold",
                                borderwidth=0,
                                cursor="hand2",
                                height= 2, 
                                width=15,
                                command=self.submitEntry     
                        )
        
        self.submitSet.bind("<Enter>", self.on_enter)
        self.submitSet.bind("<Leave>", self.on_leave)
        self.submitSet.place(x=centerX,y=260, anchor='center') 


    def on_enter(self, e):
        self.submitSet.config(background=hoverBG, foreground= fg, cursor="hand2")
    
    def on_leave(self, e):
        self.submitSet.config(background=bgMain, foreground=fg)

    def dropDownMenu(self):
        self.OPTIONS = [
            "Display elements and cardinality",
            "Set-builder Notation and Roster Method",
            "Display Power-set"
            ] #etc
        
        
        

        self.variable = StringVar(self.newWindow)
        self.variable.set(self.OPTIONS[0]) # default value
        self.OptionMenu_CheckButton(self.variable)

        self.menuButton = OptionMenu(self.newWindow, self.variable, *self.OPTIONS, command=self.OptionMenu_CheckButton)
        self.menuButton.config(
                                bg=bgMain,
                                fg=fg,
                                activebackground=activeBG,
                                activeforeground=fg,
                                width=38,
                                height=1,
                                cursor="hand2",
                                highlightbackground = bgMain,
                                highlightcolor= bgMain,
                            )
        self.menuButton["menu"].config(
                                        bg=greyBG,
                                        fg=fg,
                                        activebackground=bgMain,
                                        activeforeground=fg
                                )
        self.menuButton["highlightthickness"]=0
        self.menuButton.place(x=centerX,y=125, anchor='center')

    def checkButtons(self):
        self.setNotationBuilder = Checkbutton(
                                                self.newWindow,
                                                bg=bg,
                                                fg=fg,
                                                activebackground=bg,
                                                activeforeground=fg,
                                                variable=self.setNotationBuilder_var,
                                                onvalue=1, 
                                                offvalue=0,
                                                cursor="hand2",
                                                selectcolor=bg,
                                                text="Set-builder Notation"
                                        )

        self.rosterMethod = Checkbutton(
                                                self.newWindow,
                                                bg=bg,
                                                fg=fg,
                                                activebackground=bg,
                                                activeforeground=fg,
                                                variable=self.rosterMethod_var,
                                                onvalue=1, 
                                                offvalue=0,
                                                cursor="hand2",
                                                selectcolor=bg,
                                                text="Roster Method"
                                        )
        
    def submitEntry(self):
        if self.variable.get() == self.OPTIONS[0]:
            elements(self.root,self.entrySet.get(), 1)
            self.newWindow.destroy()
        if self.variable.get() == self.OPTIONS[2]:
            elements(self.root,self.entrySet.get(), 3)
            self.newWindow.destroy()
        if self.variable.get() == self.OPTIONS[1]:
            if self.setNotationBuilder_var.get():
                pass
            elif self.rosterMethod_var.get():
                elements(self.root,self.entrySet.get(), 4)
            elif self.setNotationBuilder_var.get() and self.rosterMethod_var.get():
                elements(self.root,self.entrySet.get(), 4)
            self.newWindow.destroy()
            
        

    def OptionMenu_CheckButton(self,event):
            if self.variable.get() == self.OPTIONS[1]:
                self.setNotationBuilder.place(x=centerX,y=175, anchor='center')
                self.rosterMethod.place(x=centerX-15,y=210, anchor='center')
            else:
                self.setNotationBuilder.place_forget()
                self.rosterMethod.place_forget()


        


    def display(self):
        self.createEntry()
        self.submitButton()
        self.checkButtons()
        self.dropDownMenu()
        
        

    