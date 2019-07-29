
import turtle
import random

turtle.tracer(1,0)

s_x = 800
s_y = 500
turtle.setup(s_x, s_y)

turtle.penup()

square_size = 20
start_length = 6
time_step = 100

pos_list = [ ]
stamp_list= [ ]
food_pos = [ ]
food_stamps = [ ]

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

def new_stamp():
    snake_pos = snake.pos()
    pos_list.append(snake_pos)
    stamps= snake.stamp()
    stamp_list.append(stamps)

for body in range(6):
    x_pos = snake.pos() [0]
    y_pos = snake.pos() [1]

    x_pos+=square_size

    snake.goto(x_pos, y_pos)

    new_stamp()

def remove_tail():
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

snake.direction = "Up"
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
def up():
    snake.direction = "Up"
    print("You pressed the up key!")
turtle.onkeypress(up, "Up")

def down():
    snake.direction = "Down"
    print("You pressed the down key!")
turtle.onkeypress(down, "Down")

def right():
    snake.direction = "Right"
    print("You pressed the right key!")
turtle.onkeypress(right, "Right")

def left():
    snake.direction = "Left"
    print("You pressed the left key!")
turtle.onkeypress(left, "Left")

turtle.listen()

turtle.register_shape("trash.gif")

food = turtle.clone()
food.shape("trash.gif")

food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos :
    food.goto(this_food_pos)
    food_stmp = food.stamp()
    food_stamps.append(food_stmp)
    food.hideturtle()
    
def make_food():
    min_x = -int(s_x/2/square_size)+1
    max_x = int(s_x/2/square_size)-1
    min_y = -int(s_y/2/square_size)+1
    max_y = int(s_y/2/square_size)-1


    food_x = random.randint (min_x, max_x) *square_size
    food_y = random.randint(min_y, max_y) *square_size
    food.goto(food_x, food_y)
    food_ran_pos = (food_x, food_y)
    food_pos.append(food_ran_pos)
    food.stamp()
    food_stamps.append(food_ran_pos)

#ejfvhoihfeoividfghjkgdsasdfhjkdsasdfhjkjgfdsasdgjkjgfdsasdgjklkgfdsasdfhjkjgfsasdg
    
    
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos [0]
    y_pos = my_pos [1]

    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + square_size)
    elif snake.direction == "Down":
        snake.goto(x_pos, y_pos - square_size)
    elif snake.direction == "Right":
        snake.goto(x_pos + square_size, y_pos)
    elif snake.direction == "Left":
        snake.goto(x_pos - square_size, y_pos)
        
    new_stamp()

    if snake.pos() in food_pos:
        food_index = food_pos.index(snake.pos())
        food.clearstamp(food_stamps [food_index])
        food_pos.pop(food_index)
        food_stamps.pop(food_index)
        print("You have eaten the food!")

    if len(food_stamps) <= 6 :
        make_food() 

        

    remove_tail()

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("Game Over!")
        quit()

    if new_x_pos <= LEFT_EDGE:
        print("Game Over!")
        quit()

    if new_y_pos >= UP_EDGE:
        print("Game Over!")
        quit()

    if new_y_pos <= DOWN_EDGE:
        print("Game Over!")
        quit()

    

    turtle.ontimer(move_snake, time_step)

    
move_snake()












turtle.mainloop()

    
