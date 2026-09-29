import turtle

# set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# make pizza dough
dough = turtle.Turtle()
dough.speed(0)
dough.fillcolor("burlywood2")
dough.penup()
dough.goto(0,-225)
dough.pendown()
dough.begin_fill()
dough.circle(225)
dough.end_fill()
dough.hideturtle()

# ask user for type of sauce
sauce = turtle.Turtle()
sauce.speed(0)
sauce_type = input("Alfredo or Tomato sauce? ")

# forces user to input correcct input
while sauce_type != "Alfredo" and sauce_type != "Tomato":
    print("Invalid choice. Please enter Alfredo or Tomato.")
    sauce_type = input("What type of sauce? ")

# sets sauce color based on user input
if sauce_type == "Alfredo":
    sauce.pencolor("white")
    sauce.fillcolor("white")
else:
    sauce.pencolor("darkred")
    sauce.fillcolor("darkred")

# make many circles at (0,0) to replicate the curves of sauce
for pizza in range(8):
    sauce.begin_fill()
    sauce.circle(100)
    sauce.goto(0,0)
    sauce.right(45)
    sauce.end_fill()

# define coordinates for a custom shape (cheese)
custom_polygon = ((0, 11), (2, 10), (5, 10), (7, 7), 
                  (10, 5), (10, 2), (11, 0), (10, -2), (10, -5), (7, -7), 
                  (5, -10), (2, -10), (0, -11), (-2, -10), 
                  (-5, -10), (-7, -7), (-10 ,-5), (-10, -2), (-11, 0), (-10, 2),
                  (-10, 5), (-7, 7), (-5, 10), (-2, 10), (0, 11))

# Register the new custom shape and name it
wn.register_shape("pizza_cheese", custom_polygon)

# create turtle and apply the shape
cheese = turtle.Turtle()
cheese.shape("pizza_cheese")
cheese.fillcolor("cornsilk1")

# put cheese on pizza
cheese.shapesize(16.5)
cheese.stamp()

#pepperoni

# keep the window open
wn.mainloop()