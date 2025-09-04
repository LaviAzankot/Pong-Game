from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.sety(new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.sety(new_y)





