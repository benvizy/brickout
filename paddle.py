from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.pu()
        self.goto(position)

    # Paddle Functions
    def go_right(self):
        new_xcor = self.xcor() + 20
        self.goto(new_xcor, self.ycor())

    def go_left(self):
        new_xcor = self.xcor() - 20
        self.goto(new_xcor, self.ycor())
