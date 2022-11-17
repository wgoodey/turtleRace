import turtle
from random import randint, shuffle
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
WIDTH = 800
HEIGHT = 400
finish_line = (WIDTH / 2) - 25
start_line = (-WIDTH / 2) + 20


def get_user_bet(color_list):
    """Prompts the user to pick the color of turtle they want to bet on. Returns the user's bet."""
    while True:
        user_bet = screen.textinput("Make your bet", f"Which turtle do you think will win?"
                                                     f"\n({', '.join(colors)})").lower()
        if user_bet in color_list:
            return user_bet


def create_turtles():
    """Creates a dictionary of turtles and returns it."""
    turtle_list = {}
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtle.penup()
        turtle_list[color] = turtle
    return turtle_list


def arrange_turtles(starting_line):
    """Arranges the turtles at the starting_line."""
    gap = 60
    i = 0
    for color in colors:
        turtles[color].goto(starting_line, 150 - (i * gap))
        i += 1


def check_winner(finishing_line):
    """Returns the name of a turtle if it has crossed the finishing_line."""
    for color in turtles:
        x, y = turtles[color].position()
        if x >= finishing_line:
            return color
    return "none"


def move_turtles(finishing_line):
    """Moves all the turtles a random distance and if a turtle has crossed the finish line, its name is returned."""
    shuffle(colors)
    winner = check_winner(finishing_line)
    for color in colors:
        # limit movement to finish line
        distance = randint(0, 10)
        x, _ = turtles[color].position()
        if x + distance > finishing_line:
            distance = finishing_line - x
        turtles[color].forward(distance)

        # check if a turtle has crossed the finishing_line
        if winner == "none":
            winner = check_winner(finishing_line)

    return winner


screen = Screen()
screen.setup(WIDTH, HEIGHT)
turtles = create_turtles()
arrange_turtles(start_line)
bet = get_user_bet(colors)

leader = check_winner(finish_line)
while leader == "none":
    leader = move_turtles(finish_line)

if leader == bet:
    result = f"You won! The {leader} turtle crossed the finish line first."
else:
    result = f"Sorry you lost. The {leader} turtle crossed the finish line first."

turtle.hideturtle()
turtle.write(result)

screen.exitonclick()
