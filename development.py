import turtle

x = 120
y = 10


turtle.up()
turtle.goto(0,0)
turtle.left(x)
turtle.forward(250)
turtle.right(x)
turtle.down()

def spiral(radius) :
     turtle.circle(radius, extent=90)

def hexagon(size) :
# draws a hexagon
    for i in range(6) :
        turtle.forward(size)
        turtle.right(360/6)
    turtle.up()
    turtle.left(x)
    turtle.forward(y)
    turtle.right(x)
    turtle.down()

for j in range(6) :
        turtle.forward(250)
        turtle.left(y*6)
        turtle.forward(y*4)
        turtle.backward(y*4)
        turtle.right(x)
turtle.up()
turtle.left(x)
turtle.forward(y)
turtle.right(x)
turtle.down()

a = turtle.position()
hexagon(260)
b = turtle.position()
hexagon(270)
c = turtle.position()
hexagon(280)
d = turtle.position()
hexagon(290)
e = turtle.position()

turtle.right(60)
turtle.up()
turtle.forward(350)
turtle.down()


turtle.left(200)

turtle.circle(-25, extent=120)
spiral(-50)
spiral(-75)
spiral(-125)

turtle.forward(13)
turtle.circle(15, extent=135)
turtle.circle(8, extent=160)
turtle.forward(300)

turtle.circle(-10, extent=210)
turtle.forward(150)
turtle.circle(90, extent=105)
turtle.left(25)
turtle.circle(60, extent=120)
turtle.circle(45, extent=120)

for k in range (40, 0, -5) :
    spiral(k)


turtle.left(90)
turtle.up()
turtle.forward(200)
turtle.left(90)
turtle.forward(30)
turtle.down()

def fufd ():
    turtle.dot()
    # turtle.forward(5)
    turtle.up()
    turtle.forward(45)
    turtle.down()

fufd()
fufd()

turtle.up()
turtle.goto(e)
turtle.down()

turtle.right(25)
turtle.forward(30)

turtle.exitonclick()