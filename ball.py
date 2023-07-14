from turtle import Turtle
import random


HEADING = [45, 135, 225, 315]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(x=0, y=random.randint(-260, 260))
        self.speed("fastest")
        self.color("white")
        self.shape("circle")
        self.setheading(random.choice(HEADING))
        self.move()

    def move(self):
        self.forward(20)

    def wall_collision_up(self):
        if self.heading() == 45:
            self.setheading(315)
            self.move()
        elif self.heading() == 135:
            self.setheading(225)
            self.move()

    def wall_collision_down(self):
        if self.heading() == 225:
            self.setheading(135)
            self.move()
        elif self.heading() == 315:
            self.setheading(45)
            self.move()

    def left_paddle_collision(self):
        if self.heading() == 135:
            self.setheading(45)
            self.move()
        elif self.heading() == 225:
            self.setheading(315)
            self.move()

    def right_paddle_collision(self):
        if self.heading() == 45:
            self.setheading(135)
            self.move()
        elif self.heading() == 315:
            self.setheading(225)
            self.move()

    def reset(self):
        self.setposition(x=0, y=random.randint(-260, 260))
        self.setheading(random.choice(HEADING))
        self.move()
