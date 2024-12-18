from tkinter import *
from functools import partial

class MainLogin:
    def __init__(self, students_list, main_div, menu_div, destroyer):
        self.students_list = students_list
        self.main_div = main_div
        self.menu_div = menu_div
        self.attempts = 4
        self.destroy = destroyer


    def login(self, students_list):
        username = self.name.get()
        studentID = self.student_ID.get()

        if self.attempts > 1:
            for student_info in students_list:
                if student_info[2] == studentID and student_info[0] == username:
                    print("Login successful.")
                    self.myinfo(student_info)
                    self.update_myinfo()
                    self.login_bg.pack_forget()
                    self.main_div.pack(side="left", fill="both", expand=True)
                    self.menu_div.pack(side="left", fill="y")
                     # Hide login UI
                    return

            self.attempts -= 1
            self.attempts_label.config(text=f"Attempts left: {self.attempts}")
            print("Student Not Found!")
        else:
            print("Maximum attempts reached!")
            self.attempts_label.config(text="You've reached the maximum attempts!")

    def login_gui(self, screen_input):
        self.login_bg = Frame(screen_input, bg="#D4D4D4")#backgorund ng login page
        self.login_bg.pack(side="left", fill="both", expand=True)
        self.login_div = Frame(self.login_bg, bg="black", width= 600, height= 450) #yung black na box
        self.login_div.place(relx=0.5, rely=0.5, anchor="center")

        Label(self.login_div, text="Login", font=("Century Gothic", 35), fg="white", bg="black").place(x= 250, y=30)
        self.attempts_label = Label(self.login_div, text="", font=("Century Gothic", 16), fg="red", bg="black")
        self.attempts_label.place(x=50, y=100) #attempts

        Label(self.login_div, text="Student ID:", font=("Century Gothic", 16), fg="white", bg="black").place(x= 50, y=150)
        self.student_ID = Entry(self.login_div, font=("Century Gothic", 14), width=30)
        self.student_ID.place(x= 180, y=152) #kung saan ilalagay yung studnetid

        Label(self.login_div, text="Name:", font=("Century Gothic", 16), fg="white", bg="black").place(x= 50, y=210) #kung saan ilalagay yung name
        self.name = Entry(self.login_div, font=("Century Gothic", 14), width=30)
        self.name.place(x= 180, y=210)

        login_button = Button(self.login_div, text="Login", font=("Century Gothic", 14), command= partial(self.login, self.students_list), padx=20, pady=10, bg="#78909C", fg="white", width= 10)
        login_button.place(x= 235, y=270)
        exit_button = Button(self.login_div, text="Exit", font=("Century Gothic", 14), command= self.destroy, padx=20, pady=10, bg="#78909C", fg="white", width= 10)
        exit_button.place(x= 235, y=340)

    def myinfo(self, student_info):
        self.student_name = student_info[0]
        self.age =  student_info[1]
        self.student_id = student_info[2]
        self.email = student_info[3]
        self.number = student_info[4]

    def myinfo_gui(self, screen_input):
    # Add static labels to the frame for displaying information
        self.info_title = Label(screen_input, text="Your Information", font=("Century Gothic", 18), fg="black", bg="#dadada", pady=20)
        self.info_title.place(x=400, y = 30)

        self.name_label = Label(screen_input, text=f"Name: ", font=("Century Gothic", 16), fg="black", bg="#dadada", pady=10)
        self.name_label.place(x= 50, y =130)

        self.age_label = Label(screen_input, text=f"Age: ", font=("Century Gothic", 16), fg="black", bg="#dadada", pady=10)
        self.age_label.place(x= 50, y =230)

        self.id_label = Label(screen_input, text=f"Student ID: ", font=("Century Gothic", 16), fg="black", bg="#dadada", pady=10)
        self.id_label.place(x= 50, y =330)

        self.email_label = Label(screen_input, text=f"Email: ", font=("Century Gothic", 16), fg="black", bg="#dadada", pady=10)
        self.email_label.place(x= 50, y =430)

        self.phone_label = Label(screen_input, text=f"Phone Number: ", font=("Century Gothic", 16), fg="black", bg="#dadada", pady=10)
        self.phone_label.place(x= 50, y =530)

   
    def update_myinfo(self):
        self.name_label.config(text=f"Name:  {self.student_name}")
        self.age_label.config(text=f"Age:  {self.age}")
        self.id_label.config(text=f"Student ID:  {self.student_id}")
        self.email_label.config(text=f"Email:  {self.email}")
        self.phone_label.config(text=f"Phone Number:  {self.number}")