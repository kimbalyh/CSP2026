# 125_Shall_we_play_a_game.py

#-----import statements-----
import turtle as trtl
import random as rand
# LATER - import leaderboard as lb 

#-----game configuration----
wn = trtl.Screen()
wn.setup(width= 600, height= 800)
wn.title("Fruit Merge Game")

fruit_shape = ["circle", "circle", "circle", "circle"]
fruit_color = ["blue", "purple", "red", "yellow"]
fruit_size = [1.5, 2, 3, 3.75]

xcor = 0
ycor = 230

fruits = []
current_fruit = None

# TODO: LATER -  add score, point values, leaderboard

#-----game functions--------
# create random fruit
def random_fruit():
    global current_fruit

    current_fruit = trtl.Turtle()
    current_fruit.hideturtle()

    fruit_index = rand.randint(0,3)
    current_fruit.fruit_size = fruit_size[fruit_index]

    current_fruit.shape(fruit_shape[fruit_index])
    current_fruit.fillcolor(fruit_color[fruit_index])
    current_fruit.shapesize(fruit_size[fruit_index])

    current_fruit.penup()
    current_fruit.goto(xcor, ycor)
    current_fruit.showturtle()
    fruits.append(current_fruit)

def move_right():
    if current_fruit.xcor() < 200:
        current_fruit.goto(current_fruit.xcor() + 20, current_fruit.ycor())

def move_left():
    if current_fruit.xcor() > -200:
        current_fruit.goto(current_fruit.xcor() - 20, current_fruit.ycor())

def drop_fruit():
    wn.onkeypress(None, "d")
    wn.onkeypress(None, "a")
    while current_fruit.ycor() > -250:
       current_fruit.speed(0)
       current_fruit.goto(current_fruit.xcor(), current_fruit.ycor() - 10)
       if check_collision() != None:
            break
    random_fruit()
    wn.onkeypress(move_right, "d")
    wn.onkeypress(move_left, "a")

# TODO: COLLISION - checks if fruits touch, if yes, stop falling, need to make the hitbox more accurate for different shape sizes
def check_collision():
    for fruit in fruits:
        if fruit != current_fruit:
            if current_fruit.distance(fruit) < 50:
                return fruits
    return None

# TODO: add function to merge alike fruits 

# TODO: LATER - add function? if fruit touch line at top, game over (break)

# TODO: LATER - add function? start game/try again button

#-----events----------------\
# random fruit generated
random_fruit()

# fruit controls 
wn.onkeypress(move_right, "d")
wn.onkeypress(move_left, "a")
wn.onkeypress(drop_fruit, "space")

wn.listen()
wn.mainloop()