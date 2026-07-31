from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        next_y = self.ycor() - 20
        self.goto(self.xcor(), next_y)