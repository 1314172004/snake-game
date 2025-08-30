from turtle import Screen
import time
import snake
import food
from score_board import ScoreBoard

screen=Screen()
screen.tracer(0)
screen.setup(600, 500)
screen.bgcolor("black")
screen.title("Snake Game")

snake=snake.Snake()
foodi=food.Food()
score=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
snake_head=snake.head
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.movement()
    if snake.all_snakes[0].distance(foodi) < 15:
        foodi.refresh()
        score.score_increment()
        snake.extent()
    if snake_head.xcor()>295 or snake_head.xcor()<-295 or snake_head.ycor()<-245 or snake_head.ycor()>245:
        score.game_over()
        snake.reset()

    for each_snake in snake.all_snakes[1:]:
        if snake_head.distance(each_snake)<10:
            score.game_over()
            snake.reset()


screen.exitonclick()





