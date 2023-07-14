import time
from turtle import Screen, Turtle
from field import Field
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=1025, height=620)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.update()
screen.listen()
line = Field()
right_paddle = Paddle("right")
left_paddle = Paddle("left")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
ball = Ball()
left_score = Score("left")
right_score = Score("right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    left_paddle.move_paddle()
    ball.move()
    if left_paddle.segments[0].ycor() == 280:
        for segment in left_paddle.segments:
            segment.setheading(270)
        left_paddle.down()
    if left_paddle.segments[3].ycor() == -280:
        for segment in left_paddle.segments:
            segment.setheading(90)
        left_paddle.up()
    right_paddle.move_paddle()
    if right_paddle.segments[0].ycor() == 280:
        for segment in right_paddle.segments:
            segment.setheading(270)
        right_paddle.down()
    if right_paddle.segments[3].ycor() == -280:
        for segment in right_paddle.segments:
            segment.setheading(90)
        right_paddle.up()
    if ball.ycor() > 290:
        ball.wall_collision_up()
    if ball.ycor() < -290:
        ball.wall_collision_down()
    for segment in left_paddle.segments:
        if ball.distance(segment) < 20:
            ball.left_paddle_collision()
    for segment in right_paddle.segments:
        if ball.distance(segment) < 20:
            ball.right_paddle_collision()
    if ball.xcor() > 510:
        left_score.add_point()
        time.sleep(1)
        ball.reset()
    if ball.xcor() < -510:
        right_score.add_point()
        time.sleep(1)
        ball.reset()
    if right_score.score > 10 or left_score.score > 10:
        game_is_on = False

screen.exitonclick()
