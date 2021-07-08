from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x500")
window.title("LifeChoices Online")
window.resizable("false", "false")
window["bg"] = "white"


class Info:
    def __init__(self, window):
        self.top_frame = Frame(window, bg='blue')
        self.top_frame.pack(side="top", fill=X)
        self.home2_label = Label(self.top_frame, text="LifeChoices Online", font=("Arial", 15, "bold"), bg="blue",
                                 fg="white", height=2,
                                 padx=20)
        self.home2_label.pack(side="left")

        self.home_label = Label(self.top_frame, text="LC", font=("Arial", 15, "bold"), bg="lime", height=2, padx=20)
        self.home_label.pack(side="right")

        self.welcome = Label(window,
                             text="Your login has been successful!\n Please enjoy your the rest of your day\n Come back soon!",
                             bg="white", font=("Arial", 15, "bold"))
        self.welcome.place(x=10, y=150)
        self.thanks = Button(window, text="Thank you!", command=self.thanks, bg="blue", fg="white", borderwidth=5,
                             font=("Arial", 12, "bold"))
        self.thanks.place(x=140, y=300)

    def thanks(self):
        msg_box = messagebox.askquestion("Successful login", "Would you like to leave this page?")
        if msg_box == "yes":
            window.destroy()
            import logout
        else:
            messagebox.showinfo("Return", "You will remain on this page.")


obj = Info(window)
window.mainloop()
