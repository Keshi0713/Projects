from tkinter import *

class ShowAllStudents:
    def __init__(self, students_list, screen_input):
        self.students_list = students_list
        self.screen_input= screen_input

    def show_all_students_gui(self, screen_input):
        self.show_title = Label(screen_input, text="All Students", font=("Century Gothic", 18), pady=20)
        self.show_title.pack()


        canvas = Canvas(screen_input)
        scrollbar = Scrollbar(screen_input, orient="vertical", command=canvas.yview)
        canvas.config(yscrollcommand=scrollbar.set)
        

        content_frame = Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


        header_frame = Frame(content_frame)
        header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        name_header = Label(header_frame, text="Name", font=("Century Gothic", 14), width=12, anchor="w", padx=10, fg="black", bg="#dadada")
        name_header.grid(row=0, column=0, padx=4, pady=5)
        
        age_header = Label(header_frame, text="Age", font=("Century Gothic", 14), width=10, anchor="w", padx=10, fg="black", bg="#dadada")
        age_header.grid(row=0, column=1, padx=5, pady=5)
        
        id_header = Label(header_frame, text="Student ID", font=("Century Gothic", 14), width=12, anchor="w", padx=10, fg="black", bg="#dadada")
        id_header.grid(row=0, column=2, padx=5, pady=5)
        
        email_header = Label(header_frame, text="Email", font=("Century Gothic", 14), width=23, anchor="w", padx=10, fg="black", bg="#dadada")
        email_header.grid(row=0, column=3, padx=5, pady=5)
        
        phone_header = Label(header_frame, text="Phone", font=("Century Gothic", 14), width=12, anchor="w", padx=10, fg="black", bg="#dadada")
        phone_header.grid(row=0, column=4, padx=5, pady=5)

        row = 1
        for student in self.students_list:
            student_frame = Frame(content_frame)
            student_frame.grid(row=row, column=0, padx=10, pady=5, sticky="w")
            
            name_label = Label(student_frame, text=student[0], font=("Century Gothic", 12), width=14, anchor="w", padx=10, fg="black", bg="#dadada")
            name_label.grid(row=row, column=1, padx=5, pady=5)

            age_label = Label(student_frame, text=student[1], font=("Century Gothic", 12), width=12, anchor="w", padx=10, fg="black", bg="#dadada")
            age_label.grid(row=row, column=2, padx=7, pady=5)

            id_label = Label(student_frame, text=student[2], font=("Century Gothic", 12), width=15, anchor="w", padx=10, fg="black", bg="#dadada")
            id_label.grid(row=row, column=3, padx=7, pady=5)

            email_label = Label(student_frame, text=student[3], font=("Century Gothic", 12), width=27, anchor="w", padx=10, fg="black", bg="#dadada")
            email_label.grid(row=row, column=4, padx=7, pady=5)

            phone_label = Label(student_frame, text=student[4], font=("Century Gothic", 12), width=12, anchor="w", padx=10, fg="black", bg="#dadada")
            phone_label.grid(row=row, column=5, padx=7, pady=5)

            row += 1


        content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))