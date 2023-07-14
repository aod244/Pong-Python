from turtle import Turtle


class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.shape("square")
        self.pensize(2)
        self.penup()
        self.setheading(90)
        self.setposition(0, -290)
        self.pendown()
        for _ in range(28):
            self.forward(20)
            self.penup()
            self.forward(10)
            self.pendown()
