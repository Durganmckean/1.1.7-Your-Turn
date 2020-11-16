#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop()
  t.penup()
  t.pensize(5)
  my_turtles.append(t)
  t.pencolor(new_color)
  t.fillcolor(new_color)


  

# starting position 
startx = 0
starty = 0

direction = 90


# making the shapes
for t in my_turtles:
  t.setheading(direction)
  t.goto(startx,starty)
  t.pendown()
  t.right(45)     
  t.forward(100)
  direction = t.heading()
  startx = t.xcor()
  starty = t.ycor()
  

# changed starting position	
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()