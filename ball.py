from turtle import Turtle

MOVE_X = 3
MOVE_Y = 3
MOVE_SPEED = 0.1


class Ball(Turtle):
    # Create ball at position (0,0)
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset()

    # Move at a constant amount of 3
    def move(self):
        new_x = self.xcor() + MOVE_X
        new_y = self.ycor() + MOVE_Y
        self.goto(new_x, new_y)

    def reset(self):
        global MOVE_SPEED
        self.goto(0, 0)
        MOVE_SPEED = 0.1
        self.bounce_x()

    # collision with top wall then we want the ball to bounce back
    def bounce_y(self):
        global MOVE_Y, MOVE_SPEED
        MOVE_Y *= -1  # reverse the direction of the ball
        MOVE_SPEED *= 0.9

    # collision with right paddle then bounce ball to left
    def bounce_x(self):
        global MOVE_X
        MOVE_X *= -1  # reverse the direction of the ball
