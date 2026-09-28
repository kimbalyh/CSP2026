import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# make many circles at (0,0) to replicate the curves of sauce
sauce = turtle.Turtle()
for pizza in range(8):
    sauce.circle(100)
    sauce.penup()
    sauce.goto(0,0)
    sauce.pendown()
    sauce.right(45)

'''
# pizza sauce ========================================================================
# Define coordinates for a custom shape 
custom_polygon = ((0, 11), (2, 10), (5, 10), (7, 7), 
                  (10, 5), (10, 2), (11, 0), (10, -2), (10, -5), (7, -7), 
                  (5, -10), (2, -10), (0, -11), (-2, -10), 
                  (-5, -10), (-7, -7), (-10 ,-5), (-10, -2), (-11, 0), (-10, 2),
                  (-10, 5), (-7, 7), (-5, 10), (-2, 10), (0, 11))

# Register the new custom shape and name it
wn.register_shape("pizza_cheese", custom_polygon)

# Create your turtle and apply the shape
cheese = turtle.Turtle()
# cheese.shapesize(15)
cheese.shape("pizza_cheese")
cheese.color("black")
cheese.fillcolor("white")

# Move it around to test
cheese.forward(100)
cheese.right(90)
cheese.forward(100)
# pizza sauce ========================================================================
'''

# Keep the window open
wn.mainloop()