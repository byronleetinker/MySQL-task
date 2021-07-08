from tkinter import *

window = Tk()
window.geometry("400x400")
window.title('Logout Page')
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
        self.label = Label(window, text="Logout", bg="white", font=("Arial", 15, "bold"))
        self.label.place(x=170, y=60)
        self.verify = Button(window, text="Logout", bg="blue", fg="white", borderwidth=5,
                             font=("Arial", 12, "bold"))
        self.verify.place(x=160, y=280)
        self.back = Button(window, text="Admin", command=self.admin, bg="lime", borderwidth=5,
                           font=("Arial", 12, "bold"))
        self.back.place(x=163, y=330)

    def admin(self):
        window.destroy()
        import admin


obj = Info(window)
window.mainloop()