# 125_Shall_we_play_a_game.py

#-----import statements-----
import turtle as trtl
import random as rand
# LATER - import leaderboard as lb 

#-----game configuration----
wn = trtl.Screen()
wn.setup(width= 500, height= 700)
wn.title("Fruit Merge Game")

box = trtl.Turtle()
box.hideturtle()
box.speed(0)
box.pensize(3)
box.penup()
box.goto(-200, 200)
box.pendown()
box.goto(-200, -300)
box.goto(200, -300)
box.goto(200, 200)

top_line = 200
line = trtl.Turtle()
line.hideturtle()
line.speed(0)
line.penup()
line.goto(-200, top_line)
line.pendown()
line.pensize(3)
line.color("red")
line.goto(200, top_line)
line.penup()

fruit_shape = ["circle", "circle", "circle", "circle"]
fruit_color = ["blue", "purple", "red", "yellow"] # add ~4 more fruits that aren't randomized at the top, must be merged to get
fruit_size = [1.5, 2, 3, 3.5]

xcor = 0
ycor = 250

fruits = []
current_fruit = None

# TODO: LATER -  add score, point values, leaderboard

#-----game functions--------

def random_fruit():
    global current_fruit

    current_fruit = trtl.Turtle()
    current_fruit.hideturtle()

    fruit_index = rand.randint(0,3)
    current_fruit.fruit_index = fruit_index

    current_fruit.shape(fruit_shape[fruit_index])
    current_fruit.fillcolor(fruit_color[fruit_index])
    current_fruit.shapesize(fruit_size[fruit_index])

    current_fruit.penup()
    current_fruit.goto(xcor, ycor)
    current_fruit.showturtle()
    fruits.append(current_fruit)

def move_right():
    if current_fruit.xcor() < 150:
        current_fruit.goto(current_fruit.xcor() + 20, current_fruit.ycor())

def move_left():
    if current_fruit.xcor() > -150:
        current_fruit.goto(current_fruit.xcor() - 20, current_fruit.ycor())

def drop_fruit():
    wn.onkeypress(None, "d")
    wn.onkeypress(None, "a")
    current_fruit.speed(0)

    while current_fruit.ycor() > -250:
       current_fruit.goto(current_fruit.xcor(), current_fruit.ycor() - 10)
       hit_fruit = check_collision()
       if hit_fruit != None:
           if current_fruit.fruit_index == hit_fruit.fruit_index and current_fruit.fruit_index < 3:
               merge_fruits(hit_fruit)
           else: 
                break

    if check_game_over():
      return   
    random_fruit()
    wn.onkeypress(move_right, "d")
    wn.onkeypress(move_left, "a")

def check_collision():
    for fruit in fruits:
        if fruit != current_fruit:
            if current_fruit.distance(fruit) < 40: # fix hitbox for diff shapes sigh
                return fruit
    return None

def merge_fruits(fruit):
    global current_fruit
    if current_fruit.fruit_index == fruit.fruit_index and current_fruit.fruit_index < 3:
        new_index = current_fruit.fruit_index + 1

        x = fruit.xcor()
        y = fruit.ycor()

        current_fruit.hideturtle()
        fruit.hideturtle()
 
        fruits.pop(fruits.index(current_fruit))
        fruits.pop(fruits.index(fruit))

        new_fruit = trtl.Turtle()
        new_fruit.penup()
        new_fruit.speed(0)
        new_fruit.goto(x, y)
        new_fruit.shape(fruit_shape[new_index])
        new_fruit.fillcolor(fruit_color[new_index])
        new_fruit.shapesize(fruit_size[new_index])
        new_fruit.fruit_index = new_index

        fruits.append(new_fruit)
        current_fruit = new_fruit

# TODO: add function? if fruit touch line at top, game over
def check_game_over():
    for fruit in fruits:
        if fruit.ycor() >= top_line:
            wn.clear()
            wn.title("Game Over")
            game_over = trtl.Turtle()
            game_over.hideturtle()
            game_over.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
            return True
    return False

# TODO: LATER - add function? start game/try again button

#-----events----------------\
random_fruit()

wn.onkeypress(move_right, "d")
wn.onkeypress(move_left, "a")
wn.onkeypress(drop_fruit, "space")

wn.listen()
wn.mainloop()