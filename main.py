from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Create the screen
screen = Screen()
screen.tracer(0)  # turn off animation
r_paddle = Paddle((350, 0))  # The right position is a tuple
l_paddle = Paddle((-350, 0))  # The left position is a tuple
ball = Ball()
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # if ball has reach the top wall then we need to bounce it back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # if ball has touch the right paddle then we need to bounce it back
    if (
        # right paddle
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        # left paddle
        or ball.distance(l_paddle) < 50
        and ball.ycor() > -320
    ):
        ball.bounce_x()

    # if ball has touch the right or left wall then reset position to (0,0)
    if ball.xcor() > 380:  # right wall

        # left paddle wins and score 1 pt
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:  # left wall

        # right paddle wins and score 1 pt
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
