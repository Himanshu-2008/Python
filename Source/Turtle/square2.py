import turtle 
t = turtle.Pen()
colors =["red","yellow","blue","green", "purple"]
for x in range (300):
	t.pencolor(colors[x%5])
	t.forward(x)
	t.left(300) 
input()
