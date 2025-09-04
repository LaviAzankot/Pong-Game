from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 80, "normal")
POSITIONS = [(-100, 200), (100, 200)]


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(POSITIONS[0])
        self.write(self.left_score, align=ALIGN, font=FONT)
        self.goto(POSITIONS[1])
        self.write(self.right_score, align=ALIGN, font=FONT)

    def increase_left_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.right_score > self.left_score:
            # Winner = right user(350, 0)
            x_position = 200
        else:
            # Winner = left user(-350, 0)
            x_position = -200

        self.goto(x_position, 100)
        self.write("WIN", align=ALIGN, font=("Courier", 50, "normal"))

