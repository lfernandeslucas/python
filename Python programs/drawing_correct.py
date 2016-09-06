import turtle

def draw_square(some_turtle):

    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):

    for i in range (1,5):
        some_turtle.circle(50)

def move_right(some_turtle):

    for i in range (1,5):
        some_turtle.right(5)

def draw_art():

    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    tom = turtle.Turtle()


    for i in range(1,4):
        
        draw_square(brad)
        move_right(brad)


    window.exitonclick()


draw_art()

