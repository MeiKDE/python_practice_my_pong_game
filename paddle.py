from turtle import Turtle


class Paddle(Turtle):
    # Create paddle(s) at a certain position
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        # paddle.position()
        # print(paddle.position())
        self.goto(position)

    # Move paddle up
    def go_up(self):
        # r_paddle original position (350, 0)
        # l_paddle original position (-350, 0)
        # we only want to move y-axis
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Move paddle down
    def go_down(self):
        # r_paddle original position (350, 0)
        # l_paddle original position (-350, 0)
        # we only want to move y-axis
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
