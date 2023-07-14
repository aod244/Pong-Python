from turtle import Turtle


class Paddle:

    def __init__(self, left_right):
        self.paddle_size = 4
        self.segments = []
        self.direction = ""
        self.create_paddle(left_right)
        self.head = self.segments[0]

    def create_paddle(self, left_right):
        self.direction = left_right
        cord_y = 40
        cord_x = 0
        if self.direction == "right":
            cord_x = 490
        elif self.direction == "left":
            cord_x = -490

        for _ in range(self.paddle_size):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(x=cord_x, y=cord_y)
            segment.setheading(90)
            self.segments.append(segment)
            cord_y -= 20

    def move_paddle(self):

        for segment in self.segments:
            segment.forward(20)

    def up(self):
        for segment in self.segments:
            segment.setheading(90)

    def down(self):
        for segment in self.segments:
            segment.setheading(270)
