from turtle import Turtle


#Crear el cuerpo de la serpiente
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)] #Con esto creamos una lista con las posiciones de la serpiente

#Aqui creamos las constantes
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        #esto es un atributo
        self.segments = [] #Con esto creamos una lista vacia para guardar los segmentos de la serpiente
        #este es el mehtodo para crear la serpiuente
        self.create_snake()
        self.head = self.segments[0] #defino el atriubutocon self.head



    def create_snake(self):
        for position in STARTING_POSITIONS: #Con esto recorremos la lista
            self.add_segment(position) #Con esto agregamos segmentos a la lista

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("yellow")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)
    
    
    def extend(self):
        self.add_segment(self.segments[-1].position())


    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1): #Con esto recorremos la lista de segmentos de la serpiente
            new_x = self.segments[seg_num - 1].xcor()#con esto le dcimos que coja el seg_num y restele 1
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)#Con esto le damos una posicion al segmento actual

        self.head.forward(20)
        #self.head.left(90)

    #estos son los methodos con los que se mueve la serpiente y los invoco en el archivo main.py
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)





