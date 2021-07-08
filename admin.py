from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("400x400")
window.title('Admin Page')
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
        self.label = Label(window, text="Admin", bg="white", font=("Arial", 15, "bold"))
        self.label.place(x=170, y=60)
        self.username = Label(window, text="Username: ", bg="white", font=("Arial", 12, "bold"))
        self.username.place(x=30, y=120)
        self.username_entry = Entry(window)
        self.username_entry.place(x=150, y=120)
        self.password = Label(window, text="Password: ", bg="white", font=("Arial", 12, "bold"))
        self.password.place(x=30, y=160)
        self.password_entry = Entry(window, show='*')
        self.password_entry.place(x=150, y=160)
        self.verify = Button(window, text="Login", command=self.login, bg="blue", fg="white", borderwidth=5,
                             font=("Arial", 12, "bold"))
        self.verify.place(x=170, y=230)
        self.clear = Button(window, text="Clear", command=self.clear, bg="lime", borderwidth=5,
                            font=("Arial", 12, "bold"))
        self.clear.place(x=30, y=330)
        self.exit = Button(window, text="Exit", command=self.exit, bg="lime", borderwidth=5,
                           font=("Arial", 12, "bold"))
        self.exit.place(x=310, y=330)

    def login(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='LifechoicesOnline')
        mycursor = mydb.cursor()
        mycursor.execute('Select * from Registration')

        if self.username_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error", "Please enter valid details")

        else:
            messagebox.showinfo("Successful login", "Welcome to the Admin Menu page")
            window.destroy()
            import adminmenu

    def clear(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()



obj = Info(window)
window.mainloop()