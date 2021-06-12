from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=800, height=600)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Red, Orange, Yellow, Green, Blue, Purple.\n Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-130, -80, -30, 20, 70 , 120]
#print(user_input)
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-380, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
    
if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()