import turtle

turtle.color('white')
turtle.speed(100)
for i in range(300):
    turtle.circle(i * 1.5)
    turtle.left(4)
    turtle.bgcolor('blue')
    if i>200:
        turtle.color('black')


turtle.hideturtle()
turtle.done()