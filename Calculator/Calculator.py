from tkinter import *
from functools import partial
win = Tk()
row_num, col_num = 2, 0
res = Label(win, width=20, text="0", fg="white", bg="#222831", font=("Times", "20", "bold"))
res.grid(row=0, column=0, columnspan=4)
btn_txt = ["x^a", "|÷|", "%", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "÷", "*", "0", ".", "="]
def funct(value):
    txt = res.cget("text")
    if value == "C": res.config(text="0")
    elif value == "=":
        try:
            expression = txt.replace("÷", "/").replace("x^a", "**").replace("|÷|", "//")
            res.config(text=str(eval(expression)))
        except:
            res.config(text="Error")
    else:
        res.config(text=txt + value if txt != "0" else value)
for txt in btn_txt:
    Button(win, text=txt, width=5, height=3, fg="white", bg="#76ABAE", font=("Times", "13", "bold"),
           command=partial(funct, txt)).grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
    if col_num == 4: col_num, row_num = 0, row_num + 1
win.title("Python Calculator")
win.geometry("325x450+700+200")
win.config(bg="#EEEEEE")
win.mainloop()