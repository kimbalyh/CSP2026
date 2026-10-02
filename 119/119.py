import turtle as trtl

# set up the screen
wn = trtl.Screen()
wn.bgcolor("white")

# ask user what size of pizza
dough_size = trtl.textinput("What size pizza?","Small, Medium, or Large: ")
dough_size = dough_size.lower()

# force user to put in valid input
while dough_size not in ["small", "medium", "large"]:
    dough_size = trtl.textinput("Invalid choice", "Small, Medium, or Large: ")

# dough size in numbers
if dough_size == "small":
    circle_size = 20
elif dough_size == "medium":
    circle_size = 25
elif dough_size == "large":
    circle_size = 30

# create pizza dough
dough = trtl.Turtle()
dough.fillcolor("burlywood2")
dough.shape("circle")
dough.shapesize(circle_size)
dough.stamp()
dough.hideturtle()
sauce = trtl.Turtle()
sauce.speed(0)

# ask user for sauce type
sauce_type = trtl.textinput("What kind of suace?", "Alfredo or Tomato:")
sauce_type = sauce_type.lower()

# forces user to input correcct input
while sauce_type not in ["alfredo", "tomato"]:
   # print("Invalid choice. Please enter Alfredo or Tomato.")
    sauce_type = trtl.textinput("Invalid Choice", "Alfredo or Tomato:")

# sets sauce color based on user input
if sauce_type == "alfredo":
    sauce.pencolor("white")
    sauce.fillcolor("white")
else:
    sauce.pencolor("darkred")
    sauce.fillcolor("darkred")

# make many circles at (0,0) to replicate the curves of sauce
for pizza in range(8):
    sauce.begin_fill()
    sauce.circle(circle_size * 4.3)
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

# create turtle and put cheese on pizza (fix)
cheese = trtl.Turtle()
cheese.shape("pizza_cheese")
cheese.pencolor("cornsilk4")
cheese.fillcolor("cornsilk1")
cheese.shapesize(circle_size/1.3) #fix this line, appears, doesn't change size

# ask user to pick toppings
toppings = trtl.textinput("What toppings?", "Pepperoni, mushroom, both, or none: ").lower() 
toppings = toppings.lower() 

while toppings not in ["pepperoni", "mushroom", "both", "none"]:
    toppings = trtl.textinput("Invalid Choice", "Please enter pepperoni, mushroom, both, or none.")

# mushroom topping
custom_polygon = ((-1,11), (2,11), (6,10), (8,8), (9,6), (9,4), (8,2), (6,1), (4,1), (3,2), 
                  (2,1), (3,4), (4,6), (5,6), (6,5), (5,6), (4,6), (3,4), (2,1),
                  (3,-4), (3,-6), (2,-7), (-1,-7), (-2,-6), (-2,-4),
                  (-1,1), (-2,4), (-3,6), (-4,6), (-5,5), (-4,6), (-3,6), (-2,4), (-1,1),
                  (-2,2), (-3,1), (-5,1), (-7,2), (-8,4), (-8,6), (-7,8), (-5,10), (-1,11))

# Register the new custom shape and name it
wn.register_shape("pizza_mushroom", custom_polygon)

# create turtle and apply the shape
shroom = trtl.Turtle()
shroom.pensize(10)
shroom.pencolor("black")
shroom.fillcolor("tan")
shroom.shape("pizza_mushroom")
shroom.shapesize(circle_size / 6)

pepperoni = trtl.Turtle()
pepperoni.fillcolor("brown")
pepperoni.shape("circle")
pepperoni.shapesize(circle_size / 8)

# keep the window open
wn.mainloop()