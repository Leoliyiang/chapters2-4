import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
lo = turtle.Turtle()
lo.shape("turtle")
lo.color("blue")
lo.stamp()
angle=0
for i in range(12):
    angle=angle+30
    lo.right(angle)
    lo.penup()
    lo.forward(200)
    lo.pendown()
    lo.forward(20)
    lo.penup()
    lo.forward(12)
    lo.stamp()
    lo.home()


wn.mainloop()
 # This is new
#size = 20
#for i in range(30):
#   lo.stamp()             # Leave an impression on the canvas
#   size = size + 3          # Increase the size on every iteration
#   lo.forward(size)       # Move tess along
#   lo.right(24)           #  ...  and turn her




