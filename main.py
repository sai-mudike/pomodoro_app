from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK="✔"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image)
canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"),)
canvas.grid(row=1,column=1)

title_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,30,"bold"),bg=YELLOW)
title_label.grid(row=0,column=1)

start_btn=Button(text="Start")
reset_btn=Button(text="Reset")

start_btn.grid(row=2,column=0)
reset_btn.grid(row=2,column=2)

tick_label=Label(text=CHECK_MARK,fg=GREEN,font=(FONT_NAME,15,"bold"))
tick_label.grid(row=3,column=1)







window.mainloop()