from turtle import Turtle

CLEAR = (0,0,0,0)
COLORS = ['coral', 'SteelBlue2', 'MediumOrchid3', 'snow', 'RosyBrown2', 'PeachPuff3', 'tan2']

class Brick(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.is_bouncy = True

class BrickWall:

    def __init__(self):
        self.bricks = []

    def make_wall(self):
        brick_y = 225
        for color in COLORS:
            if COLORS.index(color) % 2 == 0:
                brick_x = -380
                range_end = 11
            else:
                brick_x = -420
                range_end = 13
            for n in range(0, range_end):
                position = (brick_x, brick_y)
                color = color
                self.add_brick(color, position)
                brick_x += 75
            brick_y -= 25

    def add_brick(self, color, position):
        new_brick = Brick()
        new_brick.color(color)
        new_brick.pu()
        new_brick.goto(position)
        self.bricks.append(new_brick)

    def delete_brick(self, brick):
        self.bricks[brick].hideturtle()
        self.bricks[brick].is_bouncy = False





