# 131 project
#-----import statements-----
import turtle as trtl
# import playsound3 as ps3

#-----game configuration----
wn = trtl.Screen()
wn.setup(width= 1600, height= 1000)
# wn.title("")

albums = ["chinese_album", "classical_album", "english_album"]
messages = ["Wo ai ni", "U are jazzy", "You rock!"]
songs = []
wn.tracer(0)

target_x = 850
target_record_player = -500

#-----turtle initialization----
wood_bg_img = "CSP2026/131/wood_bg.gif" 
wn.addshape(wood_bg_img)
wood_bg = trtl.Turtle(shape=wood_bg_img)

old_bg_img = "CSP2026/131/old_bg.gif" 
wn.addshape(old_bg_img)
old_bg = trtl.Turtle(shape=old_bg_img)
old_bg.hideturtle()

chinese_vinyl_img = "CSP2026/131/vinyl.gif" 
wn.addshape(chinese_vinyl_img)
chinese_vinyl = trtl.Turtle(shape=chinese_vinyl_img)
chinese_vinyl.speed(0)
chinese_vinyl.penup()
chinese_vinyl.goto(-450, -150)

classical_vinyl_img = "CSP2026/131/vinyl.gif"
wn.addshape(classical_vinyl_img)
classical_vinyl = trtl.Turtle(shape=classical_vinyl_img)
classical_vinyl.speed(0)
classical_vinyl.penup()
classical_vinyl.goto(0, -150)

english_vinyl_img = "CSP2026/131/vinyl.gif"
wn.addshape(english_vinyl_img)
english_vinyl = trtl.Turtle(shape=english_vinyl_img)
english_vinyl.speed(0)
english_vinyl.penup()
english_vinyl.goto(450, -150)

vinyls = [chinese_vinyl, classical_vinyl, english_vinyl]

record_player_img = "CSP2026/131/record_player.gif" 
wn.addshape(record_player_img)
record_player = trtl.Turtle(shape=record_player_img)
record_player.speed(0)
record_player.penup()
record_player.goto(-450, -50)
record_player.hideturtle()

# TODO: Albums = Reorder them (1,2,3) on screen + add black outline 
chinese_album_img = "CSP2026/131/chinese_album.gif" # TODO: resize albums to make them uniform
wn.addshape(chinese_album_img)
chinese_album = trtl.Turtle(shape=chinese_album_img)
chinese_album.speed(0)
chinese_album.penup()
chinese_album.goto(-450, -150)

classical_album_img = "CSP2026/131/classical_album.gif"
wn.addshape(classical_album_img)
classical_album = trtl.Turtle(shape=classical_album_img)
classical_album.speed(0)
classical_album.penup()
classical_album.goto(0, -150)

english_album_img = "CSP2026/131/english_album.gif"
wn.addshape(english_album_img)
english_album = trtl.Turtle(shape=english_album_img)
english_album.speed(0)
english_album.penup()
english_album.goto(450, -150)

wn.tracer(1)

#-----game functions--------
def album_clicked(x, y):
  global animation_started
  for i in range(len(albums)):
    if albums[i] == "chinese_album":
      if -625 <= x <= -275 and -375 <= y <= 25:
        print("Chinese Album clicked") # TODO: turn it into on screen text later
        wn.onclick(None)
        vinyl_animation(i)

    elif albums[i] == "classical_album":
      if -175 <= x <= 175 and -375 <= y <= 25:
        print("Classical Album clicked")
        wn.onclick(None)
        vinyl_animation(i)

    elif albums[i] == "english_album":
      if 275 <= x <= 625 and -325 <= y <= 25: 
        print("English Album clicked")
        wn.onclick(None)
        vinyl_animation(i)

def vinyl_animation(i):
  selected_vinyl = vinyls[i]

  for vinyl in vinyls:
    vinyl.hideturtle()
  selected_vinyl.showturtle()
  selected_vinyl.speed(4)
  selected_vinyl.setheading(90)
  selected_vinyl.goto(selected_vinyl.xcor(), 240)
  selected_vinyl.setheading(0)

  while selected_vinyl.xcor() <= target_x:
    selected_vinyl.forward(25)

  change_screen()

  selected_vinyl.hideturtle()
  selected_vinyl.goto(-850, 240)
  selected_vinyl.showturtle()
  selected_vinyl.setheading(0)

  while selected_vinyl.xcor() < target_record_player:
    selected_vinyl.forward(25)
  selected_vinyl.setheading(270)

  for vinyl in range(12):
    selected_vinyl.forward(25)
  selected_vinyl.hideturtle()

  # play_music()
  # wn.ontimer(english_vinyl.hideturtle, 1500)
  
def change_screen():
    wn.tracer(0)

    chinese_album.hideturtle()
    classical_album.hideturtle()
    english_album.hideturtle()
    old_bg.showturtle()
    record_player.showturtle()
    
    wn.tracer(1)

'''
def display_message():
  box = trtl.Turtle()
  box.hideturtle()
  box.pensize(100)
  box.speed(2)
  box.pencolor("ivory")
  box.penup()
  box.goto(-350, 75)
  box.pendown()
  box.forward(800)

  messanger = trtl.Turtle()
  messanger.hideturtle()
  messanger.textcolor("darkred")
  #selection()

def selection():
  if chinese vinyl touch record player:
    chinese song plays (index 0)
    chinese message displays (index 0)
  elif classical vinyl touch record player:
    classical song plays (index 1 or index + 1?)
    classical message displays  (index 1?)
  elif english vinyl touch record player:
    english song plays (index 2)
    english message displays (index 2) - display_message() fct    
                                 
# def play_song():

'''

#-----events----------------\
wn.onclick(album_clicked)

wn.mainloop()

