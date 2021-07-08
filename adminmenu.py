from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

window = Tk()
window.geometry("400x400")
window.title('Admin Menu')
window.resizable("False", "False")
window["bg"] = "white"

class Info:
    def __init__(self, window):
        self.top_frame = Frame(window, bg='blue')
        self.top_frame.pack(side="top", fill=X)
        self.home2_label = Label(self.top_frame, text="LifeChoices Online", font=("Arial", 15, "bold"), bg="blue",
                                 fg="white", height=2,
                                 padx=20)
        self.home2_label.pack(side="left")

        self.home_label = Label(self.top_frame, text="LC", font=("Arial", 15, "bold"), bg="lime", height=2,
                                padx=20)
        self.home_label.pack(side="right")

        self.exit = Button(window, text="Exit", command=self.exit, bg="lime", borderwidth=5,
                           font=("Arial", 12, "bold"))
        self.exit.place(x=310, y=330)


    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()


obj = Info(window)
window.mainloop()