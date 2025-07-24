from turtle import Turtle, Screen
from paddle import Paddle

from ball import Ball
import time
from scoreboard import Scoreboard


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("PONG GAME")
tim=Turtle()
tim.color("white")
tim.hideturtle()
tim.penup()
tim.goto(0,0)
ball=Ball()
scoreboard=Scoreboard()
screen.tracer(0)


screen.update()
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")
game_is_on=True
while game_is_on:
    time.sleep(0.05)
    ball.move()
    screen.update()
    #detecting with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
        #detect collsion with paddle

    if ball.distance(r_paddle.tim) <50 and ball.xcor()>320:
        ball.bounce_x()

    if ball.distance(l_paddle.tim) <50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>380 :
        scoreboard.increase_l_score()
        ball.goto(0,0)
        ball.x_move *= -1

        ball.move()
    if ball.xcor()<-380:
        scoreboard.increase_r_score()
        ball.goto(0, 0)
        ball.x_move *= -1
        ball.move()

    if scoreboard.r_score > 10:
        game_is_on = False
        winner = "Player A"
        tim.write(f"Winner: {winner}", align="center", font=("Arial", 20, "normal"))

    elif scoreboard.l_score > 10:
        game_is_on = False
        winner = "Player B"
        tim.write(f"Winner: {winner}", align="center", font=("Arial", 20, "normal"))

screen.exitonclick()