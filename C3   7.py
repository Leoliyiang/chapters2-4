import turtle
wn = turtle.Screen()
total=0
lo = turtle.Turtle()
for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
     lo.forward(100)
     lo.left(i)
     total=total+i
     if total//360>1:
         total=total%(360*(total//360-1))
     print(total)
     
     
     
     
     
wn.mainloop()
     