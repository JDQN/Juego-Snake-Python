from turtle import Turtle

import random #generamos numero aleatorio


#creamos la comida de la serpiente
class Food(Turtle):
    def __init__(self): #de esta manera se define un constructor
        super().__init__() #de esta manera le decimos que herede todo lo de la clase Turtle
        self.shape("circle")
        self.penup()
        self.color(random.choice(["red", "green", "blue", "yellow"]))
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    #creamos un metodo para que la comida aparezca en una posicion aleatoria    
    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)