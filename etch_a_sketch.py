from turtle import Turtle, Screen

t = Turtle()


def move_forward(distance = 10):
    t.forward(distance)

def move_backward(distance = 10):
    t.backward(distance)

def turn_left(angle = 10):
    t.left(angle)

def turn_right(angle = 10):
    t.right(angle)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen = Screen()
screen.listen()
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(clear, "space")
screen.mainloop()