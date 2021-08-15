import turtle

t = turtle.Turtle()

t.pensize(10)
t.shapesize(1.2)
t.penup()
t.goto(-200,-200)
t.pendown()
t.speed(100)

#tuong nha
t.begin_fill()
t.fillcolor("Yellow")
for i in range(2):
    t.fd(200)
    t.left(90)
    t.fd(250)
    t.left(90)
t.end_fill()
#mai nha
t.begin_fill()

t.left(90)
t.fd(250)
t.right(40)
t.fd(150)
t.right(99)
t.fd(150)


#cua so
t.penup()
t.goto(-135,-80)
t.right(-50)
t.pendown()
t.begin_fill()
t.fillcolor("Blue")
for i in range(4):
    t.fd(60)
    t.left(90)
t.end_fill()
#cua chinh
t.penup()
t.goto(-200,-200)
t.pendown()
t.fd(60)
t.begin_fill()
t.fillcolor("red")
for i in range(2):
    t.fd(60)
    t.left(90)
    t.fd(99)
    t.left(90)
t.end_fill()
#cai cay

t.penup()
t.goto(200,-200)
t.pendown()
t.begin_fill()
t.fillcolor("Brown")
for i in range(2):
    t.fd(50)
    t.left(90)
    t.fd(260)
    t.left(90)
t.end_fill()
t.left(90)
t.fd(200)
t.right(90)
t.fd(25)
t.begin_fill()
t.fillcolor("green")
t.circle(90)
t.end_fill()

#ong mat troi
t.penup()
t.goto(250,250)
t.begin_fill()
t.fillcolor("orange")
t.circle(50)
t.end_fill()




turtle.done()