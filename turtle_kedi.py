import turtle as t

t.pensize(2)
t.speed("fast")
t.bgcolor("light blue")
t.penup()

def dortgen(horizontal, vertical, color):
    t.color(color)
    t.pendown()
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

#bacaklar
for i in range(4):
    t.goto(i*40,-40)
    dortgen(15,100,"black")

#gövde
t.goto(-10,30)
dortgen(150,80,"black")

#kafa
t.goto(120,80)
dortgen(50,50,"black")

t.done()
