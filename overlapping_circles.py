import turtle

loadWindow=turtle.Screen()
turtle.colormode(255)

turtle.speed(2)
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)

    turtle.left(i)
    b=i
    if b>51:
        b=51

    turtle.color(i, 2*i, 5*b)

turtle.exitonclick()
