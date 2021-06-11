import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape('turtle')


def draw_shapes(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)

# for side in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shapes(side)
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

def random_walk():
    directions = [0, 90, 180, 270]
    tim.pensize(15)
    tim.speed(0)
    for i in range(100):
        tim.color(random_colors())
        tim.forward(30)
        tim.setheading(random.choice(directions))

#random_walk()

def draw_spidograph(size_of_gap):
    tim.speed(0)
    for i in range(int(360/ size_of_gap)):
        tim.color(random_colors())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spidograph(5)




screen = t.Screen()
screen.exitonclick()