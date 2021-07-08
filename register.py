from tkinter import *
from tkinter import messagebox
import mysql.connector
from validate_email import validate_email
import rsaidnumber

window = Tk()
window.geometry("400x550")
window.title('Register Page')
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
        self.label = Label(window, text="Sign Up", bg="white", font=("Arial", 15, "bold"))
        self.label.place(x=150, y=60)
        self.name = Label(window, text="Name: ", bg="lime", font=("Arial", 12, "bold"))
        self.name.place(x=30, y=100)
        self.name_entry = Entry(window)
        self.name_entry.place(x=210, y=100)
        self.surname = Label(window, text="Surname: ", bg="blue", fg="white", font=("Arial", 12, "bold"))
        self.surname.place(x=30, y=140)
        self.surname_entry = Entry(window)
        self.surname_entry.place(x=210, y=140)
        self.username = Label(window, text="Username: ", bg="lime", font=("Arial", 12, "bold"))
        self.username.place(x=30, y=180)
        self.username_entry = Entry(window)
        self.username_entry.place(x=210, y=180)
        self.password = Label(window, text="Password: ", bg="blue", fg="white", font=("Arial", 12, "bold"))
        self.password.place(x=30, y=220)
        self.password_entry = Entry(window)
        self.password_entry.place(x=210, y=220)
        self.email = Label(window, text="Email Address: ", bg="lime", font=("Arial", 12, "bold"))
        self.email.place(x=30, y=260)
        self.email_entry = Entry(window)
        self.email_entry.place(x=210, y=260)
        self.ID = Label(window, text="ID number: ", bg="blue", fg="white", font=("Arial", 12, "bold"))
        self.ID.place(x=30, y=300)
        self.ID_entry = Entry(window)
        self.ID_entry.place(x=210, y=300)
        self.number = Label(window, text="Cell number: ", bg="lime", font=("Arial", 12, "bold"))
        self.number.place(x=30, y=340)
        self.number_entry = Entry(window)
        self.number_entry.place(x=210, y=340)
        self.kiname = Label(window, text="Next of kin name: ", bg="blue", fg="white", font=("Arial", 12, "bold"))
        self.kiname.place(x=30, y=380)
        self.kiname_entry = Entry(window)
        self.kiname_entry.place(x=210, y=380)
        self.kinumber = Label(window, text="Next of kin number: ", bg="lime", font=("Arial", 12, "bold"))
        self.kinumber.place(x=30, y=420)
        self.kinumber_entry = Entry(window)
        self.kinumber_entry.place(x=210, y=420)
        self.verify = Button(window, text="Register", command=self.register, bg="blue", fg="white", borderwidth=5,
                             font=("Arial", 12, "bold"))
        self.verify.place(x=30, y=480)
        self.back = Button(window, text="Back", command=self.back, bg="lime", borderwidth=5,
                           font=("Arial", 12, "bold"))
        self.back.place(x=180, y=480)

        self.exit = Button(window, text="Exit", command=self.exit, bg="blue", fg="white", borderwidth=5,
                           font=("Arial", 12, "bold"))
        self.exit.place(x=310, y=480)

    def register(self):


        try:
            if self.name_entry.get() == "" or self.surname_entry.get() == "" or self.username_entry.get() == "" or self.password_entry.get() == "" or self.kiname_entry.get() == "" or self.kinumber_entry.get() == "":
                messagebox.showerror("Error", "Please ensure that all fields are filled in.")

            if 13 != len(self.ID_entry):
                ID = rsaidnumber.parse(self.ID_entry)
                ID.valid
                messagebox.showerror("Error", "Please enter correct ID number")

            elif validate_email(self.email_entry.get()):
                messagebox.showerror("Error", "Please enter the correct email address")

            elif len(self.number_entry) != 10:
                messagebox.showerror("Error", "Please enter correct phone number")

        except:
            mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234",
                                       host="127.0.0.1", database="LifechoicesOnline")
        mycursor = mydb.cursor()
        select = "SELECT user_id FROM Login"
        self.user_id = mycursor.execute(select)
        self.user_id = mycursor.fetchone()

        sql = "INSERT INTO Registration (name, surname, username, password, email, IDNumber, phoneNumber, NextOfKinName, " \
              "NextOfKinNumber, user_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        values = (self.username_entry.get(), self.password_entry.get(), self.email_entry.get(), self.name_entry.get(),
                  self.surname_entry.get(),
                  self.ID_entry.get(), self.number_entry.get(), self.kiname_entry.get(), self.kinumber_entry.get(),
                  self.user_id[0])
        mycursor.execute(sql, values)
        mydb.commit()

        mycursor.execute("Select * from Registration")
        messagebox.showinfo("Success", "Your registration was successful.")
        window.destroy()
        import menu

    def back(self):
        window.destroy()
        import main

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()


obj = Info(window)
window.mainloop()
