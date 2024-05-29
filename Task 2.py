import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Indian Flag")
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Create a turtle object
flag_turtle = turtle.Turtle()
flag_turtle.speed(3)  # Adjust the speed as necessary

# Function to draw a rectangle
def draw_rectangle(color, width, height):
    flag_turtle.begin_fill()
    flag_turtle.color(color)
    for _ in range(2):
        flag_turtle.forward(width)
        flag_turtle.right(90)
        flag_turtle.forward(height)
        flag_turtle.right(90)
    flag_turtle.end_fill()

# Position the turtle at the starting point
flag_turtle.penup()
flag_turtle.goto(-150, 100)
flag_turtle.pendown()

# Draw the saffron stripe
draw_rectangle("orange", 300, 60)

# Move to the starting position for the white stripe
flag_turtle.penup()
flag_turtle.goto(-150, 40)
flag_turtle.pendown()

# Draw the white stripe
draw_rectangle("white", 300, 60)

# Move to the starting position for the green stripe
flag_turtle.penup()
flag_turtle.goto(-150, -20)
flag_turtle.pendown()

# Draw the green stripe
draw_rectangle("green", 300, 60)

# Draw the Ashoka Chakra
flag_turtle.penup()
flag_turtle.goto(0, 10)
flag_turtle.pendown()
flag_turtle.color("navy")
flag_turtle.circle(15)  # Draw the outer circle of the Ashoka Chakra

# Draw the 24 spokes of the Ashoka Chakra
flag_turtle.penup()
flag_turtle.goto(0, 10)
flag_turtle.pendown()
flag_turtle.setheading(90)  # Point the turtle upward

for _ in range(24):
    flag_turtle.forward(20)
    flag_turtle.backward(20)
    flag_turtle.right(15)

# Hide the turtle and display the window
flag_turtle.hideturtle()
turtle.done()
