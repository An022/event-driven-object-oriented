"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

It's not a difficult game but a hard homework.(hahaha)

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'orange'
        self.paddle.color = 'orange'
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_offset)
        self.paddle_width = paddle_width
        self.paddle_height_at_offset = self.window_height - paddle_offset
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.ball_radius = BALL_RADIUS
        self.window.add(self.ball, x=(self.window_width-ball_radius)/2, y=(self.window_height-ball_radius)/2)
        self.corner_y = self.ball.y + self.ball_radius*2
        self.corner_x = self.ball.x + self.ball_radius*2

        self.brick = GRect(brick_width, brick_height)
        self.brick.filled = True
        self.brick_cols = BRICK_COLS
        self.brick_rows = BRICK_ROWS
        self.brick_offset = BRICK_OFFSET
        self.brick_height = BRICK_HEIGHT
        self.brick_width = BRICK_WIDTH
        self.brick_spacing = BRICK_SPACING
        self.embed_bricks()

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED

        self.ball_velocity()
        self.ball_react()
        self.ball_check()

        self.count_bricks = self.brick_rows * self.brick_cols
        self.win()

    def embed_bricks(self):
        x_axis = 0
        y_axis = self.brick_offset
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                self.brick = GRect(self.brick_width, self.brick_height)
                self.brick.filled = True
                if j % 2 == 1:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                else:
                    self.brick.fill_color = 'navy'
                    self.brick.color = 'navy'
                self.window.add(self.brick, x=x_axis, y=y_axis)
                y_axis += self.brick_height + self.brick_spacing
            self.brick = GRect(self.brick_width, self.brick_height)
            self.brick.filled = True
            x_axis += self.brick_width + self.brick_spacing
            y_axis = self.brick_offset
            self.window.add(self.brick, x=x_axis, y=y_axis)

    def ball_velocity(self):
        self.__dx = random.randint(0, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = random.randint(MAX_X_SPEED, INITIAL_Y_SPEED)
        if random.random() > 0.5:
            self.__dy = -self.__dy

    def move_ball(self):
        self.ball.move(self.__dx, self.__dy)

    def move_ball_random(self):
        self.__dx = random.randint(0, MAX_X_SPEED)
        self.__dy = random.randint(MAX_X_SPEED, INITIAL_Y_SPEED)

    def prepare_ball(self):
        self.ball = GOval(self.ball_radius, self.ball_radius)
        self.ball.filled = True
        self.ball_radius = BALL_RADIUS
        self.window.add(self.ball, x=(self.window_width - self.ball_radius) / 2,
                        y=(self.window_height - self.ball_radius) / 2)

    def handle_wall_collisions(self):
        if self.ball.x <= 0 or self.ball.x >= self.window_width - self.ball_radius:
            self.__dx = - self.__dx
        if self.ball.y <= 0 or self.ball.y >= self.window_height - self.ball_radius:
            self.__dy = -self.__dy

    def get_velocity_x(self):
        return self.__dx

    def get_velocity_y(self):
        return self.__dy

    def ball_react(self):
        self.__dy = -self.__dy

    def ball_check(self):
        maybe_brick_i = self.window.get_object_at(self.ball.x, self.ball.y)
        if maybe_brick_i is not None:
            self.ball_react()
            if maybe_brick_i is not self.paddle:
                self.window.remove(maybe_brick_i)
                self.count_bricks -= 1
        else:
            maybe_brick_ii = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2)
            if maybe_brick_ii is not None:
                self.ball_react()
                if maybe_brick_ii is not self.paddle:
                    self.window.remove(maybe_brick_ii)
                    self.count_bricks -= 1
            else:
                maybe_brick_iii = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
                if maybe_brick_iii is not None:
                    self.ball_react()
                    if maybe_brick_iii is not self.paddle:
                        self.window.remove(maybe_brick_iii)
                        self.count_bricks -= 1
                else:
                    maybe_brick_iv = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y + self.ball_radius * 2)
                    if maybe_brick_iv is not None:
                        self.ball_react()
                        if maybe_brick_iv is not self.paddle:
                            self.window.remove(maybe_brick_iv)
                            self.count_bricks -= 1

    def win(self):
        if self.count_bricks <= 0:
            return True
        else:
            return False
