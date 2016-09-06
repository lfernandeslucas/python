import turtle

def draw_l(some_turtle):

    some_turtle.right(90)
    some_turtle.forward(100)
    some_turtle.left(90)
    some_turtle.forward(80)

def draw_u(some_turtle):

    turtle.position()
    (200.00,50.00)

def draw_name():

    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()

    draw_l(brad)

    brad.setpos(200,0)
    draw_l(brad)

    window.exitonclick()




draw_name()

