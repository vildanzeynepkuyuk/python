import turtle as t

ILKX = -100
ILKY = 50

t.color("blue")
t.shape("arrow")
t.bgcolor("red")
t.pensize(3)
t.pencolor("yellow")

t.penup()
t.goto(ILKX, ILKY)
t.pendown()

#evin ana hatları
for index in range(4):
    t.forward(200)
    t.right(90)

# çatısı
t.left(45)
t.forward(140)
t.right(89)
t.forward(141)

# sol pencere
t.penup()
t.goto(ILKX+30, ILKY-30)
t.pendown()
t.setheading(0)
for index in range(4):
    t.forward(40)
    t.right(90)

# sağ pencere
t.penup()
t.goto(ILKX+130, ILKY-30)
t.pendown()
t.setheading(0)
for index in range(4):
    t.forward(40)
    t.right(90)

#kapı
t.penup()
t.goto(ILKX+70, ILKY-110)
t.pendown()
t.setheading(0)
for index in range(2):
    t.forward(56)
    t.right(90)
    t.forward(90)
    t.right(90)

t.hideturtle()
t.done()