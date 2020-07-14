import turtle
t=turtle.Pen()
colors = ["red","blue","green","yellow","pink","purple","gray","black","violet"]
for x in range(100):
	t.pencolor(colors[x%8])
	t.circle(x)
	t.left(91)

input()
