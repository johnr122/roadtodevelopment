import turtle 

def draw_square(hehe):
	for i in range(1,5):
		hehe.forward(100)
		hehe.right(90)

def pabilog_na_square():	
	window = turtle.Screen()
	window.bgcolor("green")
	pat = turtle.Turtle()
	pat.shape("turtle")
	pat.color("purple")
	pat.speed(2)
	for i in range(1,37):
		draw_square(pat)
		pat.right(10)

	window.exitonclick()

pabilog_na_square()