from tkinter import *

class AddStudent:
    def __init__(self, students_list, screen_input):
        self.students_list = students_list
        self.screen_input = screen_input
        self.entries = {}

    def add_student_gui(self, screen_input):
        self.title_label = Label(screen_input, text="Add a Student", font=("Century Gothic", 18), fg="black", bg="#dadada", pady=20)
        self.title_label.pack()
        # Frames
        form_frame = Frame(screen_input, bg="#dadada")
        form_frame.pack(pady=10)
        # entry ng user
        labels = ["Name", "Age", "Student ID", "Email", "Phone"]
        for i, label_text in enumerate(labels):
            label = Label(form_frame, text=f"{label_text}:", font=("Century Gothic", 12), anchor="e", width=15, bg="#dadada", fg="black")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            entry = Entry(form_frame, font=("Century Gothic", 12), width=25)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label_text] = entry 

        # Submit Button
        self.submit_button = Button(screen_input, text="Add Student", font=("Century Gothic", 12), bg="black", fg="white", command=self.save_student)
        self.submit_button.pack(pady=10)
        self.status_label = Label(screen_input, text="", font=("Century Gothic", 12), fg="black", bg="#dadada")
        self.status_label.pack()

    def save_student(self):
        # kunin yung mga nilagay ni user
        name = self.entries["Name"].get().strip()
        age = self.entries["Age"].get().strip()
        student_id = self.entries["Student ID"].get().strip()
        email = self.entries["Email"].get().strip()
        phone = self.entries["Phone"].get().strip()

        #if walang laman, katulad don sa website error
        if not all([name, age, student_id, email, phone]):
            self.status_label.config(text="Error: All fields must be filled!", fg="red")
            return

        # Add sa students_list
        new_student = [name, age, student_id, email, phone]
        self.students_list.append(new_student)

        # Save sa file
        with open("students.txt", "a+") as file:
            for x in new_student:
                file.write(f"{x}, ")
            file.write("\n")
            file.close()
        print("Student added to the list")
        self.status_label.config(text="Student added successfully!", fg="green")

        # Clear mga nilagay ni user
        for entry in self.entries.values():
            entry.delete(0, END)