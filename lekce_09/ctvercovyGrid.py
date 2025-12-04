import turtle


def ctverec(velikost):
    for _ in range(4):
        turtle.forward(velikost)
        turtle.right(90)


def grid(velikost, pocet):
    for y in range(pocet):
        turtle.pendown()
        for x in range(pocet):
            ctverec(velikost)
            turtle.forward(velikost)
        turtle.penup()
        turtle.backward(pocet * velikost)
        turtle.right(90)
        turtle.forward(velikost)
        turtle.left(90)


turtle.shape("turtle")
turtle.speed(200)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()

grid(30, 10)

turtle.done()