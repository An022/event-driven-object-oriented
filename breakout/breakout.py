"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

It's not a difficult game but a hard homework.(hahaha)
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmousemoved, onmouseclicked

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts
GAME_START = 1
NUM_CLICKS = 0
graphics = BreakoutGraphics()


def main():
    # graphics = BreakoutGraphics()
    # Add animation loop here!
    onmousemoved(moving_paddle)
    onmouseclicked(moving_ball)


def moving_paddle(e):
    graphics.paddle.x = e.x - graphics.paddle.width/2
    graphics.paddle.y = graphics.window_height - graphics.paddle_offset
    # set the zone that paddle can move.
    if graphics.paddle.x >= graphics.window.width - graphics.paddle.width:
        graphics.paddle.x = graphics.window.width - graphics.paddle.width
    elif graphics.paddle.x < 0:
        graphics.paddle.x = 0
    else:
        pass
    pause(FRAME_RATE)


def moving_ball(e):
    global NUM_LIVES
    global NUM_CLICKS
    NUM_CLICKS += 1
    game_on = NUM_CLICKS == GAME_START
    # start the game
    while game_on and NUM_LIVES > 0:
        # If the ball fall out from the screen bottom, we should discount player's lives one time.
        if graphics.ball.y >= graphics.window_height - graphics.ball_radius:
            NUM_LIVES -= 1
            graphics.window.remove(graphics.ball)
            # If player's lives are more than 0, player can gain one ball and continue the game.
            if NUM_LIVES > 0:
                NUM_CLICKS -= 1
                graphics.prepare_ball()
                graphics.move_ball_random()
                break
            # If player's lives are no more than 0, player can not gain any ball.
            else:
                break
        graphics.move_ball()
        graphics.handle_wall_collisions()
        graphics.ball_check()
        pause(FRAME_RATE)
        if graphics.win() is True:
            break
        if NUM_LIVES == 0:
            break
    # When game is started, any clicks cannot influence the ball and the whole game.
    if game_on is not True and NUM_LIVES > 0:
        NUM_CLICKS -= 1
        graphics.move_ball()
        graphics.handle_wall_collisions()
        graphics.ball_check()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
