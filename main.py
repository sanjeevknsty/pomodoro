from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps =1
start_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global  reps

    window.after_cancel(start_timer)
    canvas.itemconfig(edit_text,text="00:00")
    title_text.config(text="TIMER")
    checkmark_label.config(text="")
    reps =1


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():

    global reps

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60
    if reps == 8:
        title_text.config(text="BREAK",fg=RED)
        count_down(long_break_sec)
        reps = 0

    elif reps % 2 == 0:
        title_text.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
        reps += 1

    else:
        title_text.config(text="WORK", fg=GREEN)
        count_down(work_sec)
        reps += 1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count /60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(edit_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global start_timer
        start_timer = window.after(10,count_down,count-1)
    else:
        global reps
        check_mark = ""
        print(reps)
        for _ in range(math.floor(reps / 2)):
            check_mark +="✔"
        checkmark_label.config(text=check_mark)
        timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50,pady=50,bg=YELLOW)

title_text = Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,"30","bold"))
title_text.grid(column=1,row=0)


canvas = Canvas(width=200,height=220,bg=YELLOW,highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100,110,image=photo_image)
edit_text = canvas.create_text(102,130,text="00:00",font=(FONT_NAME,"20","bold"),fill="white")
canvas.grid(column=1,row=1)



start_button = Button(text="Start",highlightthickness=0,command=timer)
start_button.grid(column=0,row=3)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=3,row=3)



checkmark_label = Label(fg=GREEN,bg=YELLOW,font=("10"))
checkmark_label.grid(column=1,row=4)




window.mainloop()



