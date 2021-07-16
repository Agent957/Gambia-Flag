import turtle

speed = (2.0)

screen = turtle.Screen()
screen.bgcolor('black')

def rectangle():
	for i in range(2):
		turtle.forward(900)
		turtle.right(90)
		turtle.forward(150)
		turtle.right(90)

turtle.penup()
turtle.goto(-400,350)
turtle.pendown()
turtle.color('red')
turtle.begin_fill()
rectangle()
turtle.end_fill()

turtle.penup()
turtle.goto(-400,200)
turtle.pendown()
turtle.color('white')
turtle.begin_fill()
rectangle()
turtle.end_fill()

turtle.penup()
turtle.goto(-400,125)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
rectangle()
turtle.end_fill()

turtle.penup()
turtle.goto(-400,-25)
turtle.pendown()
turtle.color('white')
turtle.begin_fill()
rectangle()
turtle.end_fill()

turtle.penup()
turtle.goto(-400,-125)
turtle.pendown()
turtle.color('green')
turtle.begin_fill()
rectangle()
turtle.end_fill()

turtle.done()