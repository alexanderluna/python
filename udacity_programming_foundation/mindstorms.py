import turtle

def draw_square(custom_turtle):
    for i in range(1,5):
        custom_turtle.forward(100)
        custom_turtle.right(90)

def draw_art():
    # setup turtle
    window = turtle.Screen()
    window.bgcolor("black")

    alex = turtle.Turtle()
    alex.pencolor("green")

    # draw to the Screen
    for i in range(1,100):
        draw_square(alex)
        alex.right(5)

    window.exitonclick

draw_art()
