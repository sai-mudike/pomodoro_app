from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark=""
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    global check_mark
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text=f"00:00")
    reps=0
    check_mark=""
    title_label.config(text="Timer")
    tick_label.config(text=check_mark)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_bk_sec=SHORT_BREAK_MIN*60
    lng_bk_sec=LONG_BREAK_MIN*60
    reps+=1

    if reps%8==0:
        title_label.config(text="Break",fg=RED)
        count_down(lng_bk_sec)
        
    elif reps%2==0:
        title_label.config(text="Break",fg=PINK)
        count_down(short_bk_sec)
    else:
        title_label.config(text="Work",fg=GREEN)
        count_down(work_sec)
        
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global check_mark
    global timer
    count_min=math.floor(count/60)
    count_sec=count%60 
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        timer =window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps%2 ==0:
            check_mark+="✔"
            tick_label.config(text=check_mark)
# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"),)
canvas.grid(row=1,column=1)



title_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,30,"bold"),bg=YELLOW)
title_label.grid(row=0,column=1)

start_btn=Button(text="Start",highlightthickness=0,command=start_timer)
reset_btn=Button(text="Reset",highlightthickness=0,command=reset)

start_btn.grid(row=2,column=0)
reset_btn.grid(row=2,column=2)

tick_label=Label( fg=GREEN,font=(FONT_NAME,15,"bold"),bg=YELLOW)
tick_label.grid(row=3,column=1)







window.mainloop()