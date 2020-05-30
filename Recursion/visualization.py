import turtle

tutle = turtle.Turtle()
win = turtle.Screen()

def draw(tutle, line):
	if line > 0:
		tutle.forward(line)
		tutle.right(90)
		draw(tutle, line-5)
draw(tutle, 200)
win.exitonclick()