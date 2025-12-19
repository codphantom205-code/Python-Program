import turtle
t = turtle.Turtle()
t.speed(1)
n = int(turtle.textinput("Petals", "No of Petals"))
for _ in range(n):
    t.circle(100, 60)
    t.left(120)
    t.circle(100, 60)
    t.left(360 / n)
t.hideturtle()
turtle.done()    