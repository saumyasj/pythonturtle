import turtle

loadWindow=turtle.Screen()
turtle.colormode(255)

turtle.speed(0)
sides=5

def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)

for i in range(100):
    shape(5*i, sides)


    turtle.left(i)
    b=i
    if b>51:
        b=51

    turtle.color(i, 2*i, 5*b)

turtle.exitonclick()
