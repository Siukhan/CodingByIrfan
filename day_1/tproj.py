# Day 1 - TURTLE PROJECT

import turtle

# Create Screen
screen = turtle.Screen()

# Screen Title
screen.title("Turtle Program")

# Screen Background color
screen.bgcolor("skyblue")

# Create a turtle objest
pen = turtle.Turtle()

# Change Pen Size, Shape and Color
pen.speed(2)
pen.pensize(3)
pen.shape("turtle")
pen.pencolor("red")

# Move turtle to the center of the screen
pen.penup()
pen.setpos(1, 1)
pen.pendown()

# Draw Triangle
for _ in range(3):
    pen.forward(150)
    pen.right(120)

# Draw Square
for _ in range(4):
    pen.forward(150)
    pen.right(90)

# Draw Pentagon
for _ in range(5):
    pen.forward(150)
    pen.right(72)

# Draw Hexagon
for _ in range(6):
    pen.forward(150)
    pen.right(60)

# Hide turtle
pen.hideturtle()    

# Exit
screen.exitonclick()