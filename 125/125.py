# 125_Shall_we_play_a_game.py

#-----import statements-----
import turtle as trtl
import random as rand
# LATER - import leaderboard as lb 

#-----game configuration----
wn = trtl.Screen()
wn.listen()
wn.setup(width= 600, height= 800)
wn.title("Fruit Merge Game")

# TODO: set up variables & parallel lists, determine shapes and sizes
fruit_shape = ["circle", "square", "triangle"]
fruit_color = ["red", "yellow", "blue"]

S = 1.5
M = 2.5
L = 3

fruit_size = [S, S, S, S, S, M, M, M, M, L]
xcor = 0
ycor = 230

# TODO: LATER -  add score, point values, leaderboard

#-----initialize turtle-----
# TODO: add fruits (turtle), start w/ 3, assign shapes [circle, square, triangle] to size variables, make random 
fruits = trtl.Turtle()

#-----game functions--------
# TODO: add function that makes random fruit appear at top of screen (rand)
def random_fruit():
    fruits.hideturtle()
    fruits.shape(rand.choice(fruit_shape))
    fruits.fillcolor(rand.choice(fruit_color))
    fruits.shapesize(rand.choice(fruit_size))
    fruits.penup()
    fruits.goto(xcor, ycor)
    fruits.showturtle()

# TODO: function for if user presses specific key, then move fruit back and forth (onclick), if user presses specific key, then fruit drops (onclick)
def move_right():
    # If press D key, move right, set boundaries
    if fruits.xcor() < 200:
        fruits.goto(fruits.xcor() + 20, fruits.ycor())
    wn.onkeypress(move_right, "d")

def move_left():
     # If press A key, move left, set boundaries
    if fruits.xcor() > -200:
        fruits.goto(fruits.xcor() - 20, fruits.ycor())
    wn.onkeypress(move_left, "a")

def drop_fruit():
    # Spacebar or return key drops fruit down
    wn.onkeypress(None, "d")
    wn.onkeypress(None, "a")
    while fruits.ycor() > -250:
       fruits.goto(fruits.xcor(), fruits.ycor() - 30)
    random_fruit()
    wn.onkeypress(move_right, "d")
    wn.onkeypress(move_left, "a")

# TODO: add function that when fruits touch (hitbox), check if fruits same, if true, merge fruits (pop), then new one appears at exact location [indexing stuff]


# TODO: LATER - add function? if fruit touch line at top, game over (break)
    

# TODO: LATER - add function? start game/try again button

#-----events----------------\
# random fruit generated
random_fruit()

# fruit controls 
wn.onkeypress(move_right, "d")
wn.onkeypress(move_left, "a")
wn.onkeypress(drop_fruit, "space")

# new random fruit appears

# TODO: make fruit drop, & stop when it reaches bottom of screen or touch another fruit

wn.mainloop()
# add classes?