import turtle as t

def dortgen (horizontal,vertical,color):
    t.pendown()
    t.pensize(2)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed("fast")
t.bgcolor("light blue")

#ayaklar
t.goto(-100,-150)
dortgen(50,20,"purple")
t.goto(-30,-150)
dortgen(50,20,"purple")
#bacaklar
t.goto(-25,-50)
dortgen(15,100,"yellow")
t.goto(-55,-50)
dortgen(-15,100,"yellow")
#gövde
t.goto(-90,100)
dortgen(100,150,"red")
#sol kol
t.goto(-150,70)
dortgen(60,15,"yellow")
t.goto(-150,110)
dortgen(15,40,"yellow")
#sağ kol
t.goto(10,70)
dortgen(60,15,"yellow")
t.goto(55,110)
dortgen(15,40,"yellow")
#boyun
t.goto(-50,120)
dortgen(15,20,"seashell")
#kafa
t.goto(-85,170)
dortgen(80,50,"orange")
#gözler
t.goto(-60,160)
dortgen(30,10,"white")
t.goto(-55,155)
dortgen(5,5,"black")
t.goto(-40,155)
dortgen(5,5,"black")
#ağız
t.goto(-65,135)
dortgen(40,5,"red")
#eller
t.goto(-155,130)
dortgen(25,25,"green")
t.goto(-147,130)
dortgen(10,15,t.bgcolor())
t.goto(50,130)
dortgen(25,25,"green")
t.goto(58,130)
dortgen(10,15,t.bgcolor())

t.hideturtle()
t.done()