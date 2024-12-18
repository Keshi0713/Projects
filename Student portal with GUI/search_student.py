from tkinter import *

class infosearch:
    def __init__(self, students_list, screen_input):
        self.students_list = students_list
        self.screen_input = screen_input
        self.student_name = None
        self.age = None
        self.student_id = None
        self.email = None
        self.number = None

    def search_student(self, student_id):
        for student_info in self.students_list:
            if student_info[2] == student_id:
                self.student_name = student_info[0]
                self.age = student_info[1]
                self.student_id = student_info[2]
                self.email = student_info[3]
                self.number = student_info[4]
                return True
        return False

    def search_gui(self, screen_input):
        self.search_title = Label(screen_input, text="Search a Student", font=("Century Gothic", 18), fg="black", bg="#dadada", pady=20)
        self.search_title.place(x=400, y=30)

        # Entry sa Student ID
        self.search_entry_label = Label(screen_input, text="Enter Student ID:", font=("Century Gothic", 16), fg="black", bg="#dadada")
        self.search_entry_label.place(x=50, y=150)

        self.student_id_entry = Entry(screen_input, font=("Century Gothic", 16), width=30)
        self.student_id_entry.place(x=250, y=150)

        # Search Button
        self.search_button = Button(screen_input, text="Search", font=("Century Gothic", 13), command=self.display_student_info)
        self.search_button.place(x=540, y=200)
        self.result_label = Label(screen_input, text="", font=("Century Gothic", 16), fg="black", bg="#dadada")
        self.result_label.place(x=50, y=250)
        self.name_label = Label(screen_input, text="", font=("Century Gothic", 16), fg="black", bg="#dadada")
        self.name_label.place(x=50, y=350)
        self.age_label = Label(screen_input, text="", font=("Century Gothic", 16), fg="black", bg="#dadada")
        self.age_label.place(x=50, y=400)
        self.id_label = Label(screen_input, text="", font=("Century Gothic", 16), fg="black", bg="#dadada")
        self.id_label.place(x=50, y=450)
        self.email_label = Label(screen_input, text="", font=("Century Gothic", 16), fg="black", bg="#dadada")
        self.email_label.place(x=50, y=500)
        self.phone_label = Label(screen_input, text="", font=("Century Gothic", 16), fg="black", bg="#dadada")
        self.phone_label.place(x=50, y=550)

    def display_student_info(self):
        student_id = self.student_id_entry.get()

        if self.search_student(student_id):
            self.name_label.config(text=f"Name: {self.student_name}")
            self.age_label.config(text=f"Age: {self.age}")
            self.id_label.config(text=f"Student ID: {self.student_id}")
            self.email_label.config(text=f"Email: {self.email}")
            self.phone_label.config(text=f"Phone Number: {self.number}")
            self.result_label.config(text="Student Found!", fg="green")
        else:
            self.result_label.config(text="Student Not Found!", fg="red")
            self.name_label.config(text="")
            self.age_label.config(text="")
            self.id_label.config(text="")
            self.email_label.config(text="")
            self.phone_label.config(text="")