from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("350x350")
window.title('Login_Base')
window.resizable("False", "False")
window["bg"] = "black"


class Info:
    def __init__(self, window):
        self.username = Label(window, text="Username: ", bg="lime", font=("Arial", 12, "bold"))
        self.username.place(x=30, y=50)
        self.username_entry = Entry(window)
        self.username_entry.place(x=150, y=50)
        self.password = Label(window, text="Password: ", bg="lime", font=("Arial", 12, "bold"))
        self.password.place(x=30, y=90)
        self.password_entry = Entry(window, show='*')
        self.password_entry.place(x=150, y=90)
        self.verify = Button(window, text="Login", command=self.login, bg="lime", borderwidth=5,
                             font=("Arial", 12, "bold"))
        self.verify.place(x=150, y=130)
        self.create = Button(window, text="Register New User", command=self.create, bg="lime", borderwidth=5,
                             font=("Arial", 12, "bold"))
        self.create.place(x=100, y=180)
        self.clear = Button(window, text="Clear", command=self.clear, bg="lime", borderwidth=5,
                            font=("Arial", 12, "bold"))
        self.clear.place(x=30, y=250)
        self.exit = Button(window, text="Exit", command=self.exit, bg="lime", borderwidth=5,
                           font=("Arial", 12, "bold"))
        self.exit.place(x=250, y=250)

    def check_table(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='Hospital', auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        xy = mycursor.execute('Select * from Login')
        for i in mycursor:
            print(i)

    def login(self):
        self.check_table()

    def create(self):
        name = self.username_entry.get()
        password = self.password_entry.get()
        if self.username_entry == "" or self.password_entry == "":
            messagebox.showerror("ERROR", "Please fill in username and password")
        elif name.isdigit():
            messagebox.showerror("Error", "Name does not contain letters")
        else:
            mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                           database='Hospital', auth_plugin='mysql_native_password')

            mycursor = mydb.cursor()

            sql = "INSERT INTO Login  VALUES (%s, %s)"
            val = (self.username_entry.get(), self.password_entry.get())
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
            mycursor.execute('Select * from Login')
            messagebox.showinfo("SUCCESS", "New user and password added")

            # text file
            with open("Login.txt", "a+") as file:
                file.write("Username: " + self.username_entry.get() + "\n")
                file.write("Password: " + self.password_entry.get() + "\n")
                file.write("\n")
                file.close()

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
