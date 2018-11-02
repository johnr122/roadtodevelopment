import turtle

def draw_diamond(hihi):
    for i in range(1,3):
        hihi.forward(50)
        hihi.right(40)
        hihi.forward(50)
        hihi.right(140)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("blue")
    pat = turtle.Turtle()
    pat.shape("turtle")
    pat.color("green")
    pat.speed(2)
    for i in range(1,37):
        draw_diamond(pat)
        pat.right(10)
    pat.right(90)
    pat.forward(200)

    window.exitonclick()

draw_flower()
