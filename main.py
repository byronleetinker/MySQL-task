from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import date
from datetime import timedelta


window = Tk()
window.geometry("400x400")
window.title('Login_Base')
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
        self.username = Label(window, text="Username: ", bg="white", font=("Arial", 12, "bold"))
        self.username.place(x=30, y=100)
        self.username_entry = Entry(window)
        self.username_entry.place(x=150, y=100)
        self.password = Label(window, text="Password: ", bg="white", font=("Arial", 12, "bold"))
        self.password.place(x=30, y=140)
        self.password_entry = Entry(window, show='*')
        self.password_entry.place(x=150, y=140)
        self.verify = Button(window, text="Login", command=self.login, bg="lime", borderwidth=5,
                             font=("Arial", 12, "bold"))
        self.verify.place(x=170, y=200)
        self.create = Button(window, text="Sign Up", command=self.create, bg="blue", borderwidth=5,
                             font=("Arial", 12, "bold"), fg="white")
        self.create.place(x=160, y=250)
        self.clear = Button(window, text="Clear", command=self.clear, bg="lime", borderwidth=5,
                            font=("Arial", 12, "bold"))
        self.clear.place(x=30, y=330)
        self.exit = Button(window, text="Exit", command=self.exit, bg="lime", borderwidth=5,
                           font=("Arial", 12, "bold"))
        self.exit.place(x=310, y=330)

    def login(self):
        mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234",
                                       host="127.0.0.1", database="LifechoicesOnline")
        mycursor = mydb.cursor()
        select = "SELECT user_id FROM Login"
        self.userid = mycursor.execute(select)
        self.userid = mycursor.fetchone()
        self.sign_in_date = date.today()
        self.sign_in_time = timedelta()

        sql = "INSERT INTO Users (userid, username, sign_in_date, sign_in_time) VALUES(%s, %s, %s, %s) "
        values = (self.userid[0], self.username_entry.get(), self.sign_in_date, self.sign_in_time)
        mycursor.execute(sql, values)
        mydb.commit()

        mycursor.execute("Select * from Registration")
        messagebox.showinfo("Success", "Your registration was successful.")
        window.destroy()
        import menu

        if self.username_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error", "Please enter valid details")

        else:
            messagebox.showinfo("Successful login", "Welcome to the Menu page")
            window.destroy()
            import menu

    def create(self):
        window.destroy()
        import register

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
