from turtle import *
color('red','yellow')
begin_fill()
while True:
	forward(200)
	left(175)
	if abs(pos())<0.5:
		break

end_fill()
done()
