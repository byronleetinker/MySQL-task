from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("400x500")
window.title('Menu Page')
window.resizable("False", "False")
window["bg"] = "black"

class Info:
    def __init__(self, window):
        self.label = Label(window, text="Sign Up", bg="lime", font=("Arial", 20, "bold"))
        self.label.place(x=150, y=20)
        self.name = Label(window, text="Name: ", bg="lime", font=("Arial", 12, "bold"))
        self.name.place(x=30, y=80)
        self.name_entry = Entry(window)
        self.name_entry.place(x=210, y=80)
        self.surname = Label(window, text="Surname: ", bg="lime", font=("Arial", 12, "bold"))
        self.surname.place(x=30, y=120)
        self.surname_entry = Entry(window)
        self.surname_entry.place(x=210, y=120)
        self.username = Label(window, text="Username: ", bg="lime", font=("Arial", 12, "bold"))
        self.username.place(x=30, y=160)
        self.username_entry = Entry(window)
        self.username_entry.place(x=210, y=160)
        self.password = Label(window, text="Password: ", bg="lime", font=("Arial", 12, "bold"))
        self.password.place(x=30, y=200)
        self.password_entry = Entry(window)
        self.password_entry.place(x=210, y=200)
        self.ID = Label(window, text="ID number: ", bg="lime", font=("Arial", 12, "bold"))
        self.ID.place(x=30, y=240)
        self.ID_entry = Entry(window)
        self.ID_entry.place(x=210, y=240)
        self.number = Label(window, text="Cell number: ", bg="lime", font=("Arial", 12, "bold"))
        self.number.place(x=30, y=280)
        self.number_entry = Entry(window)
        self.number_entry.place(x=210, y=280)
        self.kiname = Label(window, text="Next of kin name: ", bg="lime", font=("Arial", 12, "bold"))
        self.kiname.place(x=30, y=320)
        self.kiname_entry = Entry(window)
        self.kiname_entry.place(x=210, y=320)
        self.kinumber = Label(window, text="Next of kin number: ", bg="lime", font=("Arial", 12, "bold"))
        self.kinumber.place(x=30, y=360)
        self.kinumber_entry = Entry(window)
        self.kinumber_entry.place(x=210, y=360)
        self.verify = Button(window, text="Register", command=self.register, bg="purple", borderwidth=5,
                             font=("Arial", 12, "bold"))
        self.verify.place(x=30, y=420)
        self.exit = Button(window, text="Exit", command=self.exit, bg="purple", borderwidth=5,
                           font=("Arial", 12, "bold"))
        self.exit.place(x=310, y=420)

    def register(self):
        name = self.username_entry.get()
        password = self.password_entry.get()
        if self.username_entry == "" or self.password_entry == "" or self.name_entry == "" or self.number_entry== "" or self.ID_entry == "" or self.kiname_entry == "" or self.kinumber_entry == "":
            messagebox.showerror("ERROR", "Please fill in username and password")
        elif name.isdigit():
            messagebox.showerror("Error", "Name does not contain letters")
        else:
            mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                           database='LifechoicesOnline', auth_plugin='mysql_native_password')

            mycursor = mydb.cursor()

            sql = "INSERT INTO Login  VALUES (%s, %s)"
            val = (self.username_entry.get(), self.password_entry.get())
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
            mycursor.execute('Select * from Registeration')
            messagebox.showinfo("SUCCESS", "New user and password added")
            window.destroy()
            import menu

            # text file
            with open("Login.txt", "a+") as file:
                file.write("Username: " + self.username_entry.get() + "\n")
                file.write("Password: " + self.password_entry.get() + "\n")
                file.write("\n")
                file.close()

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()


obj = Info(window)
window.mainloop()