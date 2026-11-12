# 131 project
#-----import statements-----
import turtle as trtl

#-----game configuration----
wn = trtl.Screen()
wn.setup(width= 1600, height= 1000)
# wn.title("")

albums = ["chinese_album", "classical_album", "english_album"]
wn.tracer(0)

target_x = 850  

#-----turtle initialization----

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
        chinese_vinyl_animation()
        
    elif albums[i] == "classical_album":
      if -175 <= x <= 175 and -375 <= y <= 25:
        print("Classical Album clicked")
        wn.onclick(None)
        classical_vinyl_animation()

    elif albums[i] == "english_album":
      if 275 <= x <= 625 and -325 <= y <= 25: 
        print("English Album clicked")
        wn.onclick(None)
        english_vinyl_animation()

def chinese_vinyl_animation():
  chinese_vinyl.speed(2)
  chinese_vinyl.setheading(90)
  chinese_vinyl.goto(-450, 200)
  chinese_vinyl.setheading(0)
  while chinese_vinyl.xcor() <= target_x:
    chinese_vinyl.forward(25)

def classical_vinyl_animation():
  classical_vinyl.speed(2)
  classical_vinyl.setheading(90)
  classical_vinyl.goto(0, 200)
  classical_vinyl.setheading(0)
  while classical_vinyl.xcor() <= target_x:
    classical_vinyl.forward(25)

def english_vinyl_animation():
  english_vinyl.speed(2)
  english_vinyl.setheading(90)
  english_vinyl.goto(450, 200)
  english_vinyl.setheading(0)
  while english_vinyl.xcor() <= target_x:
    english_vinyl.forward(25)

#-----events----------------\
wn.onclick(album_clicked)

wn.mainloop()

