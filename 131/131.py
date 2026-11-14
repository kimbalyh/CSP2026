# 131 project
#-----import statements-----
import turtle as trtl
import playsound3 as ps3

#-----game configuration----
wn = trtl.Screen()
wn.setup(width= 1600, height= 1000)
# wn.title("")

albums = ["chinese_album", "classical_album", "english_album"]

messages = [
  "Some feelings never grow old. May \n this melody bring back fond memories \n and remind you of how loved you are.", 
  "May this melody bring warmth to your \n heart and comfort in your soul. Wishing \n you a peaceful and wonderful day!",
  "The world is full of little wonders. \n May you always find something beautiful \n to smile about. You are appreciated!" ]

songs = ["CSP2026/131/chinese_song.mp3", "CSP2026/131/classical_song.mp3", "CSP2026/131/english_song.mp3"]
current_song = None

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

'''
stop_button_img = "CSP2026/131/stop_button_img.gif" #finish making image in canva
wn.addshape(stop_button_img)
stop_button = trtl.Turtle(shape=record_player_img)
stop_button.speed(0)
stop_button.penup()
stop_button.goto(150, -50)
stop_button.hideturtle()
'''

chinese_album_img = "CSP2026/131/chinese_album.gif" #make album covers same aesthetic 
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

  ps3.playsound("CSP2026/131/select_effect.mp3")
 # want to put pop here
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

  ps3.playsound("CSP2026/131/click_effect.mp3", block=False)
  play_music(i)
  # wait a few secs before displaying a message
  display_message(i)
  
def change_screen():
    wn.tracer(0)

    chinese_album.hideturtle()
    classical_album.hideturtle()
    english_album.hideturtle()
    old_bg.showturtle()
    record_player.showturtle()
    # stop_button.showturtle()
    
    wn.tracer(1)

def display_message(i):
  box = trtl.Turtle()
  box.hideturtle()
  box.pensize(200)
  box.pencolor("beige")
  box.penup()
  box.goto(-40, 75)
  box.pendown()
  box.speed(2)
  box.forward(550)

# have music note draw turtle
# wait a few secs before drawing
#make letters index one by one
  message = trtl.Turtle()
  message.hideturtle()
  message.speed(0)
  message.penup()
  message.goto(-77, 15)
  message.pencolor("black")
  message.write(messages[i], font=("Times New Roman", 28, "bold"))
  
def play_music(i):
  global current_song

  if current_song != None:
    current_song.stop()
  current_song = ps3.playsound(songs[i], block=False)

'''
def change_song_clicked(x,y):
  if # <= x <= # and # <= y <= #: 
    ps3.playsound("CSP2026/131/select_effect.mp3")
    change_song()

def change_song():
  global current_song

  if current_song != None:
    current_song.stop()
    current_song = None

  old_bg.hideturtle()
  record_player.hideturtle()

  chinese_album.showturtle()
  classical_album.showturtle()
  english_album.showturtle()
  chinese_vinyl.showturtle()
  classical_vinyl.showturtle()
  english_vinyl.showturtle()

  wn.onclick(album_clicked)
'''
#-----events----------------\
wn.onclick(album_clicked)

wn.mainloop()

