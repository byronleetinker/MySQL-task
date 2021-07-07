from tkinter import *

window = Tk()
window.geometry("350x350")
window.title('Menu Page')
window.resizable("False", "False")
window["bg"] = "black"

class Info:
    def __init__(self, window):
        self.label = Label(window, text="Logout", bg="lime", font=("Arial", 20, "bold"))
        self.label.place(x=130, y=30)


obj = Info(window)
window.mainloop()