import turtle
t = turtle.Pen()
turtle.bgcolor("black") 
colors=["green","blue","red","purple"]

for x in range(200):
	t.pencolor(colors[x%4])
	t.circle(x)
	t.left(91)
