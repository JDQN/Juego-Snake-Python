from re import A
from turtle import Turtle


#Estas son las constantes 
ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 #Esto es un atributo en opp
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()
        

    def update_score(self):
        self.write("The Score is: {}".format(self.score), align=(ALIGN), font=(FONT))


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over end", align=(ALIGN), font=(FONT))

  