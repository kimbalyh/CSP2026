# 125_Shall_we_play_a_game.py

#-----import statements-----
import turtle as trtl
import random as rand
# LATER - import leaderboard as lb 

#-----game configuration----
# TODO: set up variables & parallel lists, determine shapes and sizes
fruit_shape = ["circle", "square", "triangle"]
fruit_color = ["red", "yellow", "blue"]

S = 1
M = 3
L = 5

fruit_size = [S, M, L]

# TODO: LATER -  add score, point values, leaderboard

#-----initialize turtle-----
# TODO: add fruits (turtle), start w/ 3, assign shapes [circle, square, triangle] to size variables, make random 
fruits = trtl.Turtle()
wn = trtl.Screen()

# TODO: LATER - add probability of which fruit appears more often

#-----game functions--------
# TODO: add function that makes random fruit appear at top of screen (rand), LATER - add probability of which fruit appears more offten
def random_fruit():
    fruits.hideturtle()
    fruits.shape(rand.choice(fruit_shape))
    fruits.fillcolor(rand.choice(fruit_color))
    fruits.shapesize(rand.choice(fruit_size))
    fruits.penup()
    fruits.goto(0, 250)
    fruits.showturtle()

# TODO: function for if user presses specific key, then move fruit back and forth (onclick), if user presses specific key, then fruit drops (onclick)
def move_fruit():
    # A or D key moves fruit left or right
    while True:
        wn.onkeypress(fruits.back, "a")
        wn.onkeypress(fruits.forward, "d")

# def drop_fruit():
    # Spacebar or return key drops fruit down

# TODO: add function that when fruits touch, check if fruits same, if true, merge fruits (pop), then new one appears at exact location [indexing stuff]
# TODO: LATER - add function? if fruit touch line at top, game over (break)
# TODO: LATER - add function? start game/try again button


#-----events----------------\
random_fruit()

# TODO: if user presses specific key, then move fruit back and forth (onclick), if user presses specific key, then fruit drops (onclick)

# TODO: make fruit drop, & stop when it reaches bottom of screen or touch another fruit

# TODO: screen & mainloop setup
wn.setup(width= 500, height= 800)
wn.mainloop()