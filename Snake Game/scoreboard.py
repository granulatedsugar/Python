from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


# Score board class
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    # Display Score
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Game Over!
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # Add score + 1
    def add_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
