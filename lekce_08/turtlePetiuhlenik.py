import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.speed(1)

for i in range(5):
    t.forward(100)
    t.right(72)

t.screen.mainloop()
