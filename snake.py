
import turtle
import random

turtle.tracer(1,0)
turtle.bgcolor("black")

color_list = ["red","orange", "yellow", "green", "blue", "indigo", "violet"]

def color_change():
    for color in color_list:
        turtle.color(color)


    time_step = 100
    turtle.ontimer(color_change, time_step)

color_change()

s_x = 600
s_y = 570
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

border = turtle.clone()
border.penup()
border.goto(-300,280)
border.pendown()
border.goto(300,280)
border.goto(300,-280)
border.goto(-300,-280)
border.goto(-300,280)


style = ('Courier', 60, 'italic')
turtle.write('Snake Game!', font=style, align='center')



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

turtle.register_shape("zach-normal.gif")
turtle.register_shape("golden-apple.gif")

poison = turtle.clone()
poison.shape("zach-normal.gif")

gapple = turtle.clone()
gapple.shape("golden-apple.gif")

gapple_pos = []
gapple_stamps = []

poison_pos = []
poison_stamps = []


for this_gapple_pos in gapple_pos:
    gapple.goto(this_gapple_pos)
    gapple_stmp = gapple.stamp()
    gapple_stamps.append(gapple_stmp)
    gapple.hideturtle()

def make_gapple():
    min_x = -int(s_x/2/square_size)+1
    max_x = int(s_x/2/square_size)-1
    min_y = -int(s_y/2/square_size)+1
    max_y = int(s_y/2/square_size)-1


    gapple_x = random.randint (min_x, max_x) *square_size
    gapple_y = random.randint(min_y, max_y) *square_size
    gapple.goto(gapple_x, gapple_y)
    gapple_ran_pos = (gapple_x, gapple_y)
    gapple_pos.append(gapple_ran_pos)
    random_gapple_stamp = gapple.stamp()
    gapple_stamps.append(random_gapple_stamp)



for this_poison_pos in poison_pos:
    poison.goto(this_poison_pos)
    poison_stmp = poison.stamp()
    poison_stamps.append(poison_stmp)
    poison.hideturtle()

def make_poison():
    min_x = -int(s_x/2/square_size)+1
    max_x = int(s_x/2/square_size)-1
    min_y = -int(s_y/2/square_size)+1
    max_y = int(s_y/2/square_size)-1


    poison_x = random.randint (min_x, max_x) *square_size
    poison_y = random.randint(min_y, max_y) *square_size
    poison.goto(poison_x, poison_y)
    poison_ran_pos = (poison_x, poison_y)
    poison_pos.append(poison_ran_pos)
    random_poison_stamp = poison.stamp()
    poison_stamps.append(random_poison_stamp)

food = turtle.clone()
food.shape("zach-normal.gif")

food_pos = []
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
    random_stamp = food.stamp()
    food_stamps.append(random_stamp)


#ejfvhoihfeoividfghjkgdsasdfhjkdsasdfhjkjgfdsasdgjkjgfdsasdgjklkgfdsasdfhjkjgfs
    
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos [0]
    y_pos = my_pos [1]

    for i in range(len (pos_list)):
        for j in range(len (pos_list)):
            if pos_list [i] == pos_list [j] and i !=j:
                print ("You ate your self!")
                quit()

    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + square_size)
    elif snake.direction == "Down":
        snake.goto(x_pos, y_pos - square_size)
    elif snake.direction == "Right":
        snake.goto(x_pos + square_size, y_pos)
    elif snake.direction == "Left":
        snake.goto(x_pos - square_size, y_pos)


    if snake.pos() in food_pos:
        food_index = food_pos.index(snake.pos())
        food.clearstamp(food_stamps [food_index])
        #food.clearstamps()
        food_pos.pop(food_index)
        food_stamps.pop(food_index)
        print("You have eaten the food!")

    new_stamp()
    if snake.pos() in poison_pos:
        poison_index = poison_pos.index(snake.pos())
        poison.clearstamp(poison_stamps [poison_index])
        #food.clearstamps()
        poison_pos.pop(poison_index)
        poison_stamps.pop(poison_index)
        print("You have eaten the poison!")


    if snake.pos() in gapple_pos:
        gapple_index = gapple_pos.index(snake.pos())
        gapple.clearstamp(gapple_stamps [gapple_index])
        #food.clearstamps()
        gapple_pos.pop(gapple_index)
        gapple_stamps.pop(gapple_index)
        print("You have eaten the Golden Apple!")
    

        #x_pos+=square_size


        #new_stamp()


    if len(poison_stamps) <= 0 :
        remove_tail()
        make_poison()

    for i in range(5):
        if i == 4:
            if len(gapple_stamps)<=0:
                make_gapple()
                make_gapple()
                make_gapple()

    if len(food_stamps) <= 1 :
        make_food() 

    else:
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



    
##    if new_pos in pos_list:
##        print(pos_list)
##        print(new_pos)
##        print(food_pos)
##        quit()



    
    turtle.ontimer(move_snake, time_step)

    
move_snake()













turtle.mainloop()

    
