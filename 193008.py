import turtle


t = turtle.Turtle()
t.shape("turtle")

t.left(90)

t.penup()
t.backward(150)

t.pendown()
t.forward(400)

def dfs(height, level, child, angle):

    if level == 0:
        return

    t.left(angle / 2)
    for c in range(child):
        t.forward(height)
        dfs(height * 0.6, level - 1, child, angle)
        t.backward(height)

        if c != child - 1:
            t.right(angle / (child - 1))

    t.left(angle / 2)


t.speed(100)

dfs(40, 3, 5, 270)

turtle.done()