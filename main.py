
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *

PINK = "##e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
POSX_IMG = 100
POSY_IMG = 112

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

lbl_title = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
lbl_title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(POSX_IMG, POSY_IMG, image=tomato_img)

canvas.create_text(POSX_IMG, POSY_IMG + 18, text='00:00', fill='white', font=(FONT_NAME, 28, 'bold'))
# canvas.create_text(100, 300, text='✔', fill=GREEN, font=(FONT_NAME, 18, 'bold'))
canvas.grid(row=1, column=1)

btn_start = Button(text='Start', font=(FONT_NAME, 14, 'bold'), highlightthickness=0)
btn_start.grid(row=2, column=0)

btn_reset = Button(text='Reset', font=(FONT_NAME, 14, 'bold'), highlightthickness=0)
btn_reset.grid(row=2, column=2)

lbl_check = Label(text='✔', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18, 'bold'))
lbl_check.grid(row=3, column=1)

window.mainloop()
