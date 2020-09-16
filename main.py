import random
from graphics import *

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
ALL_COLORS = ["red", "green", "blue", "yellow", "orange", "pink", "purple"]
NUMBER_OF_BALLS = 10

class Ball:
    def __init__(self, win):
        self.graphic = Circle(
            Point(
                WINDOW_WIDTH * random.random(),
                WINDOW_HEIGHT * random.random()
            ),
            10
        )
        self.graphic.setFill(random.choice(ALL_COLORS))
        self.graphic.draw(win)
        self.velocity = Point(random.randint(-6, 6), random.randint(-6, 6))

def main():
    # Set up window
    win = GraphWin("Ball Test", WINDOW_WIDTH, WINDOW_HEIGHT)

    # Create lots of balls
    balls = []
    for i in range(NUMBER_OF_BALLS):
        balls.append(Ball(win))

    isRunning = True

    while isRunning:
        for ball in balls:
            # Update ball positions
            ball.graphic.move(ball.velocity.getX(), ball.velocity.getY())

            # Bounce off walls if necessary
            ballX = ball.graphic.getCenter().getX()
            if ballX < 0 or ballX > win.getWidth():
                ball.velocity.x = -ball.velocity.x

            ballY = ball.graphic.getCenter().getY()
            if ballY < 0 or ballY > win.getHeight():
                ball.velocity.y = -ball.velocity.y

        # Check if we should exit
        if win.checkKey() == "Escape":
            isRunning = False

        # Sleep for a bit so we're not running as fast as possible
        time.sleep(1/60)

    win.close()

if __name__ == "__main__":
    main()
