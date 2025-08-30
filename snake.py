from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        for i in range(3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.setx(snake.xcor() - (i * 20))
            self.all_snakes.append(snake)
    def extent(self):
        snake=Turtle("square")
        snake.color("white")
        snake.penup()
        x=self.all_snakes[-1].xcor()-20
        y=self.all_snakes[-1].ycor()
        snake.goto(x,y)
        self.all_snakes.append(snake)

    def movement(self):
        for seg_num in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[seg_num - 1].xcor()
            new_y = self.all_snakes[seg_num - 1].ycor()
            self.all_snakes[seg_num].goto(new_x, new_y)
        self.all_snakes[0].forward(MOVE_DISTANCE)

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
    def reset(self):
        for seg in self.all_snakes:
            seg.goto(1010,1001)
        self.all_snakes.clear()
        self.create_snake()
        self.head=self.all_snakes[0]

