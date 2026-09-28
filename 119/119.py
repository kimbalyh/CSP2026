import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# make pizza dough
dough = turtle.Turtle()
dough.fillcolor("burlywood2")
dough.speed(0)
dough.penup()
dough.goto(0,-225)
dough.pendown()
dough.begin_fill()
dough.circle(225)
dough.end_fill()
dough.hideturtle()

# ask user for type of sauce (incomplete)
sauce = turtle.Turtle()
sauce.fillcolor("darkred")
sauce.pencolor("darkred")
'''input("What type of sauce? Alfredo or Tomato.")
if input == "Alfredo":
    sauce.fillcolor("white")
else:
    sauce.pencolor("red")'''
sauce.speed(0)

# make many circles at (0,0) to replicate the curves of sauce
for pizza in range(8):
    sauce.begin_fill()
    sauce.circle(100)
    sauce.goto(0,0)
    sauce.right(45)
    sauce.end_fill()

# Define coordinates for a custom shape (cheese)
custom_polygon = ((0, 11), (2, 10), (5, 10), (7, 7), 
                  (10, 5), (10, 2), (11, 0), (10, -2), (10, -5), (7, -7), 
                  (5, -10), (2, -10), (0, -11), (-2, -10), 
                  (-5, -10), (-7, -7), (-10 ,-5), (-10, -2), (-11, 0), (-10, 2),
                  (-10, 5), (-7, 7), (-5, 10), (-2, 10), (0, 11))

# Register the new custom shape and name it
wn.register_shape("pizza_cheese", custom_polygon)

# Create your turtle and apply the shape
cheese = turtle.Turtle()
cheese.shape("pizza_cheese")
cheese.fillcolor("cornsilk1")

# put cheese on pizza
cheese.shapesize(16.5)
cheese.stamp()

# Keep the window open
wn.mainloop()