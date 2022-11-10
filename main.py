# Turtle funcions to build a cake
# By Jeremery M Jett

import turtle
turtle.color("blue")

def cake(width, height):
    triangle(height)
    down(90, 5)
    back(width / 2 - height / 2)
    for z in range(3):
        rectangle(width, height)
        down(90, height + 5)

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

def down(angle,len):
    turtle.penup()
    turtle.right(angle)
    turtle.forward(len)
    turtle.left(angle)
    turtle.pendown()

def triangle(size):
#repeat 3 times
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)

def rectangle(width, height):
    for j in range(0, 4):
        if j % 2 ==0:
                turtle.forward(width)
                turtle.right(90)
        else:
                turtle.forward(height)
                turtle.right(90)

# cake(200, 10)

cake(200, 30)


