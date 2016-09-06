import turtle

def draw_square():

    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()

    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    bob = turtle.Turtle()
    bob.color("white")
    bob.speed("5")

    i = 0
    count = 20
    
    while (i <= count):

        if (i % 2 == 0):
            brad.forward(100)
            brad.right(90)
            bob.circle(10000)
            bob.forward(10)

        else:
            brad.forward(100)
            brad.left(90)
            bob.circle(50)
            bob.forward(10)
                        

        i = i + 1
      
    window.exitonclick()


draw_square()
