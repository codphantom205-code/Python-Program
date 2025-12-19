from tkinter import *
from time import strftime
root = Tk()
root.title("Clock")
lbl = Label(root, font=('Century', 50))
lbl.pack()
def update():
    current_time = strftime('%H:%M:%S')
    current_date = strftime('%d-%m-%Y')
    lbl.config(text=f"{current_time}\n{current_date}")
    lbl.after(1000, update)
update()
root.mainloop()


# import turtle
# import time
# from datetime import datetime
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("Day, Date and Time")
# pen = turtle.Turtle()
# pen.hideturtle()
# pen.color("cyan")
# pen.penup()
# pen.goto(0, 0)

# while True:
#     pen.clear()
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     current_date = now.strftime("%d-%m-%Y")
#     current_day = now.strftime("%A")
#     pen.write(f"Day   : {current_day}\nDate  : {current_date}\nTime  : {current_time}",
#         align="center", font=("Arial", 20, "bold"))
#     time.sleep(1)