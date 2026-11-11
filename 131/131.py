# 131 project
#-----import statements-----
import turtle as trtl

#-----game configuration----
wn = trtl.Screen()
wn.setup(width= 1600, height= 1000)
# wn.title("")

albums = ["chinese_album", "classical_album"]


#-----turtle initialization----

# TODO: Albums = Reorder them (1,2,3) on screen + add black outline 
chinese_album_img = "CSP2026/131/chinese_album.gif"
wn.addshape(chinese_album_img)
chinese_album = trtl.Turtle(shape=chinese_album_img)
chinese_album.speed(0)
chinese_album.hideturtle()
chinese_album.penup()
chinese_album.shapesize(5)
chinese_album.goto(-450, 0)
chinese_album.showturtle() # TODO: wn.update to show the turtle after it is moved to the correct position

classical_album_img = "CSP2026/131/classical_album.gif"
wn.addshape(classical_album_img)
classical_album = trtl.Turtle(shape=classical_album_img)
classical_album.shapesize(5)

# song 3 = trtl.Turtle()



#-----game functions--------
def album_clicked(x, y):
  for i in range(len(albums)):
    if albums[i] == "chinese_album":
      if -550 <= x <= -350 and -100 <= y <= 100: # TODO: change the coordinates to match the album's position on the screen
        print("Chinese Album clicked")
    elif albums[i] == "classical_album":
      if -300 <= x <= 300 and -300 <= y <= 300: # TODO: change the coordinates to match the album's position on the screen
        print("Classical Album clicked")

#-----events----------------\
wn.onclick(album_clicked)

wn.mainloop()

