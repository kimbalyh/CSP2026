# 131 project
#-----import statements-----
import turtle as trtl

#-----game configuration----
wn = trtl.Screen()
wn.setup(width= 1600, height= 1000)
# wn.title("")

albums = ["chinese_album", "classical_album"]
wn.tracer(0)

target_x = 850  

#-----turtle initialization----

classical_vinyl_img = "CSP2026/131/vinyl.gif"
wn.addshape(classical_vinyl_img)
classical_vinyl = trtl.Turtle(shape=classical_vinyl_img)
classical_vinyl.speed(0)
classical_vinyl.penup()
classical_vinyl.shapesize(5)
classical_vinyl.goto(0, -150)

chinese_vinyl_img = "CSP2026/131/vinyl.gif" 
wn.addshape(chinese_vinyl_img)
chinese_vinyl = trtl.Turtle(shape=chinese_vinyl_img)
chinese_vinyl.speed(0)
chinese_vinyl.penup()
chinese_vinyl.shapesize(5)
chinese_vinyl.goto(-450, -150)

# TODO: Albums = Reorder them (1,2,3) on screen + add black outline 
chinese_album_img = "CSP2026/131/chinese_album.gif" # TODO: resize albums to make them uniform
wn.addshape(chinese_album_img)
chinese_album = trtl.Turtle(shape=chinese_album_img)
chinese_album.speed(0)
chinese_album.penup()
chinese_album.shapesize(5)
chinese_album.goto(-450, -150)

classical_album_img = "CSP2026/131/classical_album.gif"
wn.addshape(classical_album_img)
classical_album = trtl.Turtle(shape=classical_album_img)
classical_album.speed(0)
classical_album.penup()
classical_album.shapesize(5)
classical_album.goto(0, -150)

# song 3 = trtl.Turtle()

wn.tracer(1)

#-----game functions--------
def album_clicked(x, y):
  for i in range(len(albums)):
    if albums[i] == "chinese_album":
      if -550 <= x <= -350 and -250 <= y <= 100: # TODO: change the coordinates to match the album's position on the screen
        print("Chinese Album clicked")
        vinyl_animation()
    elif albums[i] == "classical_album":
      if -300 <= x <= 300 and -450 <= y <= 300: # TODO: change the coordinates to match the album's position on the screen
        print("Classical Album clicked")

def vinyl_animation():
  chinese_vinyl.speed(2)
  chinese_vinyl.setheading(90)
  chinese_vinyl.goto(-450, 200)
  chinese_vinyl.setheading(0)
  while chinese_vinyl.xcor() <= target_x:
    chinese_vinyl.forward(25)  


#-----events----------------\
wn.onclick(album_clicked)

wn.mainloop()

