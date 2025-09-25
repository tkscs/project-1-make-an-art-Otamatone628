import turtle

x = 120

turtle.up()
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
    turtle.forward(10)
    turtle.right(x)
    turtle.down()

for j in range(6) :
        turtle.forward(250)
        turtle.left(60)
        turtle.forward(40)
        turtle.backward(40)
        turtle.right(x)
turtle.up()
turtle.left(x)
turtle.forward(10)
turtle.right(x)
turtle.down()

hexagon(260)
hexagon(270)
hexagon(280)
hexagon(290)

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
    turtle.forward(5)
    turtle.up()
    turtle.forward(45)
    turtle.down()

fufd()
fufd()

turtle.exitonclick()