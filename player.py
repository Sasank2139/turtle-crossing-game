from turtle import Turtle

forward_distance = 10
starting_position = (0, -280)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(starting_position)
        self.setheading(90)

    def move(self):
        self.forward(forward_distance)