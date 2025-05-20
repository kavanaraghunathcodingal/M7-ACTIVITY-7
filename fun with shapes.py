import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set the background color to black

# Create a turtle
t = turtle.Turtle()
t.speed(3)  # Set turtle drawing speed

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to draw a circle
def draw_circle(radius):
    t.circle(radius)

# Function to draw an equilateral triangle
def draw_triangle(size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

# Function to draw a regular polygon
def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.right(144)

# Drawing shapes at different positions
shapes = [
    ("Square", draw_square, 100),
    ("Circle", draw_circle, 50),
    ("Triangle", draw_triangle, 100),
    ("Hexagon", draw_polygon, 6, 60),  # Hexagon with 6 sides, each of length 60
    ("Star", draw_star, 100)
]

# Positioning and drawing each shape
for shape in shapes:
    name, draw_func, *params = shape
    t.penup()
    t.goto(-200, 200)  # Move turtle to a new position
    t.pendown()
    t.color("white")  # Set pen color to white
    draw_func(*params)  # Draw the shape
    t.penup()
    t.goto(0, 0)  # Reset position to center
    t.pendown()

# Hide the turtle and finish
t.hideturtle()
turtle.done()
