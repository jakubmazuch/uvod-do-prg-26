import turtle

n = int(input("Zadej kolikaúhleník chceš: "))

if n > 2:
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("red")
    t.speed(100)

    for i in range(n):
        t.forward(300/n)
        t.right(360/n)

    t.screen.mainloop()
