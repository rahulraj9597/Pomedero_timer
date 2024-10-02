from tkinter import *
import math
from openpyxl.styles.colors import BLACK
from pygments.styles.rainbow_dash import GREEN

YELLOW = '#f7f5dd'
BLUE = '#322ad1'
RED = '#d12a56'
reps = 0
timer = None


window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=100,bg='#f7f5dd')

canvas = Canvas(width=360,height=360,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(180,180,image=tomato_image)
canvas_text = canvas.create_text(180,200,text='00:00',fill='white',font=('Courier',35,'bold'),)
canvas.grid(column=1,row=1)

#set timer
def set_timer():
    global reps
    reps+=1
    if reps%2!=0:
        countdown(25*60)
        timer_label.config(text='WORK')
    elif reps%2==0:
        countdown(5*60)
        timer_label.config(text='BREAK')
    elif reps%8==0:
        countdown(20*60)
        timer_label.config(text='LONG-BREAK')

def resetfunction():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text,text = '00:00')
    timer_label.config(text='TIMER')
    check_mark.config(text='')

#testing
def countdown(count):
    count_mins = math.floor(count/60)
    count_secs = count%60
    if count_secs == 0:
        count_secs = '00'
    elif count_secs < 10:
        a = str(count_secs)
        count_secs = '0' + a
    canvas.itemconfig(canvas_text,text = f"{count_mins}:{count_secs}")
    if count > 0:
        print(count)
        global timer
        timer = window.after(1000,countdown,count - 1)
    else:
        set_timer()
        marks = ''
        work_session = math.floor(reps/2)
        for i in range(work_session):
            marks+='✔'
        check_mark.config(text=marks)


# counting = countdown(90)

#label
timer_label = Label(text='TIMER',font=('Courier',50,'bold'),bg=YELLOW,fg=GREEN)
timer_label.grid(column=1,row=0)

check_mark = Label(fg=GREEN,font=('Courier',10,'bold'),bg=YELLOW,highlightthickness=0)
check_mark.grid(column=1,row=3)
#button
starting = Button(text='START',highlightthickness=0,command=set_timer)
starting.grid(column=0,row=2)

reset = Button(text='RESET',highlightthickness=0,command=resetfunction)
reset.grid(column=2,row=2)



window.mainloop()
