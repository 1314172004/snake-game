from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",20,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as high_score:
            self.high_score=int(high_score.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score_board()
    def score_board(self):

        self.goto(-120,220)
        self.write(f"Score:{self.score}",False,ALIGNMENT,FONT)
        self.goto(120,220)
        self.write(f"High Score:{self.high_score}", False, ALIGNMENT, FONT)
    def game_over(self):
        self.clear()
        self.high_score_increment()
        self.score_board()
        self.score = 0

    def score_increment(self):
        self.score+=1
        self.clear()
        self.score_board()
    def high_score_increment(self):

        if self.score>self.high_score:
            with open("data.txt",mode="w") as file:
                self.high_score=int(file.write(f"{self.score}"))