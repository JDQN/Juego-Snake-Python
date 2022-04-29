from turtle import Screen
from snake import Snake #de esta manera importamos la clase que creamos llamada Snake
from food import Food #de esta manera importamos la clase que creamos llamada Food
from scoreboard import Score_board #de esta manera importamos la clase que creamos llamada Score_board

import time 


#Crear el esenario
screen = Screen() #Con esto intanciamos el objeto screen o creamos el objeto screen
screen.setup(width=600, height=600) #Con esto le damos un tamaño al escenario
screen.bgcolor("black") #Con esto le damos un color al escenario
screen.title("Programate Snake") #Con esto le damos un titulo al escenario

screen.tracer(0) #Con esto desactivamos el refresco de pantalla


#Creamos - la instancia de los objetos serpiente y comida
snake = Snake() #Con esto creamos la instancia de la clase Snake
food = Food() #Con esto creamos la instancia del objeto Food
score_board = Score_board() #Con esto creamos la instancia del objeto Score_board


#movimiento de la serpiente
screen.listen() #Con esto activamos el movimiento de la serpiente
screen.onkey(snake.up, "Up") #Con esto le damos una tecla para que se mueva hacia arriba
screen.onkey(snake.down, "Down") #Con esto le damos una tecla para que se mueva hacia abajo
screen.onkey(snake.left, "Left") #Con esto le damos una tecla para que se mueva hacia la izquierda
screen.onkey(snake.right, "Right") #Con esto le damos una tecla para que se mueva hacia la derecha



game_is_on = True #Con esto creamos una variable booleana para saber si el juego esta en marcha o no

while game_is_on:
    screen.update() #Con esto refrescamos la pantalla y quitamos la nimacion del movimiento de la serpiente
    time.sleep(0.2) #Con esto le damos un tiempo de espera
    snake.move() #Con esto llamamos al metodo move de la clase Snake

    if snake.head.distance(food) < 15: #Con esto verificamos si la serpiente esta cerca de la comida
        food.refresh() #Con esto refrescamos la comida
        score_board.increase_score() #Con esto aumentamos el puntaje
        snake.extend() #Con esto aumentamos la longitud de la serpiente


    #Aqui detectamos la colision de la serpiente con el cuerpo
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over() #aqui pasamos el mensaje de game over que traemos de la clase scoreboard.py
    

    #codigo de coliision de la serpiente con el cuerpo
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

    time.sleep(0.05) #Con esto le damos un tiempo de espera
    

#final
screen.exitonclick() #Con esto hacemos la ventana solo se cierre cuando le de click
