from tkinter import *
from functools import partial
from login import MainLogin
from search_student import infosearch
from show_all_students import ShowAllStudents
from add_student import AddStudent

win = Tk()
win.geometry(f"1280x800+{(win.winfo_screenwidth()-1280)//2}+{(win.winfo_screenheight()-800)//2}")
students_list = []

def read_file():
    with open("students.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            student1 = line.strip().split(", ")
            students_list.append(student1)
    print("Student Data added to the list")
    print(students_list)

#mga happenings pag pinindot ang buttons
def content1_button():  # info ng logged in user
    cont2_div.pack_forget()
    cont3_div.pack_forget()
    cont4_div.pack_forget()
    cont1_div.pack(side="right", fill="both", expand=True)
    login.myinfo_gui(cont1_div)
    login.update_myinfo()

def content2_button():  # search ng student
    cont1_div.pack_forget()
    cont3_div.pack_forget()
    cont4_div.pack_forget()
    cont2_div.pack(side="right", fill="both", expand=True)
    info.search_gui(cont2_div)

def content3_button():  # show all student info
    cont1_div.pack_forget()
    cont2_div.pack_forget()
    cont4_div.pack_forget()
    cont3_div.pack(side="right", fill="both", expand=True)
    show.show_all_students_gui(cont3_div)

def content4_button():  # add student
    cont1_div.pack_forget()
    cont2_div.pack_forget()
    cont3_div.pack_forget()
    cont4_div.pack(side="right", fill="both", expand=True)
    add_student.add_student_gui(cont4_div)

def destroyer():
    win.destroy()

def show_login_screen():
    main_div.pack_forget()
    login.login_gui(win)

read_file()
# Main and Menu Sections
main_div = Frame(win, bg="white")
menu_div = Frame(main_div, bg="#78909C")
btn_txt = ["1. Student Information", "2. Search Student", "3. Show All Students", "4. Add Student"]
func = [content1_button, content2_button, content3_button, content4_button]
btns = []
login = MainLogin(students_list, main_div, menu_div, destroyer)
info = infosearch(students_list, main_div)
show = ShowAllStudents(students_list, main_div)
add_student = AddStudent(students_list, main_div)
# login screen
login.login_gui(win)

# Menu Logo
menulogo = Label(menu_div, anchor="w", bg="#78909C", text=" |||      Menu", width=21, font=("Century Gothic", 14), padx=10, pady=5)
menulogo.grid(row=0, column=0)

# Buttons sa Menu
for i in range(len(btn_txt)):
    btns.append(Button(menu_div, anchor="w", bg="#FFFFFF", text=btn_txt[i], width=21, font=("Century Gothic bold", 14), padx=10, pady=10))
    btns[i].grid(row=i+1, column=0)
    btns[i].config(command=func[i])

# Exit Button
exit_button = Button(menu_div, width=21, text="5. Exit Program", anchor="w", command=show_login_screen, bg="#FFFFFF", font=("Century Gothic", 14), padx=10, pady=10)
exit_button.grid(row=len(btn_txt) + 1, column=0)

# Content Frames
cont1_div = Frame(main_div, bg="#dadada")
cont1_div.pack(side="right", fill="both", expand=True)
login.myinfo_gui(cont1_div)
cont2_div = Frame(main_div, bg="#dadada")
cont3_div = Frame(main_div, bg="#dadada")
cont4_div = Frame(main_div, bg="#dadada")

# Run the main loop
win.mainloop()