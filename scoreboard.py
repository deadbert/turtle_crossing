from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.level_count = 1
        self.hideturtle()
        self.goto(-280, 260)
        self.write(f"Level: {self.level_count}", font=FONT)

    def level_up(self):
        self.clear()
        self.level_count += 1
        self.write(f"Level: {self.level_count}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align='center')
