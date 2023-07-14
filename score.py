from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 40, "normal")


class Score(Turtle):
    def __init__(self, left_right):
        super().__init__()
        x_cord = 0
        if left_right == "right":
            x_cord = 50
        if left_right == "left":
            x_cord = -50
        self.score = 0
        self.penup()
        self.setposition(x=x_cord, y=255)
        self.hideturtle()
        self.color("white")
        self.write(f"{self.score}", align=ALIGMENT, font=FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align=ALIGMENT, font=FONT)
