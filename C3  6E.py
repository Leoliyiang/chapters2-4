res1=input("How many sides do the polygon have?")
res2=input("What is the length of each side?")
N=int(res1)
S=int(res2)
import turtle
wn= turtle.Screen()

lo=turtle.Turtle()
for i in range(N):
    lo.forward(S)
    lo.left(360/N)
wn.mainloop()