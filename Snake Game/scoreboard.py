from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


# Score board class
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./scores.txt") as file:
             self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    # Display Score
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # Tracking high score
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./scores.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # Game Over!
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # Add score + 1
    def add_score(self):
        self.score += 1
        self.update_scoreboard()
