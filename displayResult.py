from logging import root
from tkinter import *
from colors import *



screen_width = 750
screen_height = 400

class getResult:
    def __init__(self, root, results,len,type):
        
        self.root = root
        self.resultLabel(results, len)
        self.resultTextBox()
        self.clear_button()
        self.returnResult(results, len,type)
        

    
        # Labels
    def resultLabel(self,results,len):
        self.showResult = Label(
                            self.root,
                            text=" ",
                            font="sans 15 bold",
                            fg=fg,
                            bg=bg,
                            justify="center",
                            wraplength=300
                        )

    def clear_button(self):
        self.clearButton = Button(
                                self.root, 
                                bg=bgMain,
                                activebackground=activeBG,
                                activeforeground=fg,
                                text="Clear", 
                                justify="center",
                                fg="white",
                                font="sans 10 bold",
                                cursor="hand2",
                                borderwidth=0,
                                height= 2, 
                                width=20,
                                command=lambda: self.clear()
                        )
        self.clearButton.place(x=640,y=140, anchor="center")
        self.clearButton.bind("<Enter>", self.on_enter_clearButton)
        self.clearButton.bind("<Leave>", self.on_leave_clearButton)

    def on_enter_clearButton(self, e):
        self.clearButton.config(background=hoverBG, foreground=fg, cursor="hand2")
    
    def on_leave_clearButton(self, e):
        self.clearButton.config(background=bgMain, foreground=fg)

    def resultTextBox(self):
        # Text Box Widget
        self.newTextBox = Text(
                                self.root,
                                bg=greyBG,
                                fg=fg,
                                relief=FLAT,
                                font="sans 13 italic",
                                height=14,
                                width=50,
                                wrap='word'
                            )

        # Add scrollbar to Text widget
        self.scrollb = Scrollbar(
                                self.root,
                                command=self.newTextBox.yview,
                                )
        
        # Deploy
        self.scrollb.place(x=535, y=screen_height/2, anchor="center",height=284, width=13)
        self.newTextBox.tag_configure("center", justify='center')
        self.newTextBox.config(insertbackground=fg)
        self.newTextBox['yscrollcommand'] = self.scrollb.set
        

    def returnResult(self, results,len,type):
        self.newTextBox.place(x=300, y=screen_height/2, anchor="center")
        self.newTextBox.insert("1.0", f"{results}")
        self.newTextBox.tag_add("center", "1.0", "end")
        self.showResult.place(x=screen_width/2+265,y=screen_height/2+10, anchor="center")
        self.showResult.config(text=f"{type}\n\n{len}")


    def clear(self):
        self.newTextBox.insert("1.0", " ")
        self.scrollb.destroy()
        self.newTextBox.destroy()
        self.showResult.destroy()
        self.clearButton.destroy()
    
        

