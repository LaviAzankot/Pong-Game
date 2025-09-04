from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "cyan", "blue", "indigo", "violet", "purple", "magenta", ""]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.index = -1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        # Change color
        self.index += 1
        color = COLORS[self.index % 10]
        self.color(color)

        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()






