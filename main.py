from graphics import *

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

def main():
    # Set up window
    win = GraphWin("Ball Test", WINDOW_WIDTH, WINDOW_HEIGHT)

    # Create a ball
    ball = Circle(Point(200, 100), 10)
    ball.setFill("red")
    ball.draw(win)
    ballVelocity = Point(4, 6)

    isRunning = True

    while isRunning:
        # Update ball position
        ball.move(ballVelocity.getX(), ballVelocity.getY())

        # Bounce off walls if necessary
        ballX = ball.getCenter().getX()
        if ballX < 0 or ballX > win.getWidth():
            ballVelocity.x = -ballVelocity.x

        ballY = ball.getCenter().getY()
        if ballY < 0 or ballY > win.getHeight():
            ballVelocity.y = -ballVelocity.y

        # Check if we should exit
        if win.checkKey() == "Escape":
            isRunning = False

        # Sleep for a bit so we're not running as fast as possible
        time.sleep(1/60)

    win.close()

if __name__ == "__main__":
    main()
