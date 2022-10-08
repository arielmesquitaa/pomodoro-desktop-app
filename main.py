
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *

PINK = "##e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
POSX_IMG = 100
POSY_IMG = 112
reps = 0
check = 0

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps, check
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in (0, 2, 4, 6):
        count_down(work_sec)
        reps += 1
        check += 1
        lbl_check.configure(text='✔'*check)
    elif reps == 7:
        count_down(long_break_sec)
        reps = 0
    elif reps in (1, 3, 5, 7):
        count_down(short_break_sec)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global btn_start
    if btn_start['state'] == 'normal':
        btn_start.configure(state=DISABLED)
    mins, secs = divmod(count, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    canvas.itemconfig(timer_txt, text=timer)
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        btn_start.configure(state=NORMAL)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

lbl_title = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
lbl_title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(POSX_IMG, POSY_IMG, image=tomato_img)

timer_txt = canvas.create_text(POSX_IMG, POSY_IMG + 18, text='00:00', fill='white', font=(FONT_NAME, 28, 'bold'))
canvas.grid(row=1, column=1)

btn_start = Button(text='Start', command=start_timer, font=(FONT_NAME, 14, 'bold'), highlightthickness=0)
btn_start.grid(row=2, column=0)

btn_reset = Button(text='Reset', font=(FONT_NAME, 14, 'bold'), highlightthickness=0)
btn_reset.grid(row=2, column=2)

lbl_check = Label(text='✔'*check, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18, 'bold'))
lbl_check.grid(row=3, column=1)

window.mainloop()
