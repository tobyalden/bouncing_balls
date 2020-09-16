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

    # Create a second ball
    ball2 = Circle(Point(100, 200), 10)
    ball2.setFill("green")
    ball2.draw(win)
    ball2Velocity = Point(5, 3)

    isRunning = True

    while isRunning:
        # Update ball positions
        ball.move(ballVelocity.getX(), ballVelocity.getY())
        ball2.move(ball2Velocity.getX(), ball2Velocity.getY())

        # Bounce off walls if necessary
        ballX = ball.getCenter().getX()
        if ballX < 0 or ballX > win.getWidth():
            ballVelocity.x = -ballVelocity.x

        ballY = ball.getCenter().getY()
        if ballY < 0 or ballY > win.getHeight():
            ballVelocity.y = -ballVelocity.y

        ball2X = ball2.getCenter().getX()
        if ball2X < 0 or ball2X > win.getWidth():
            ball2Velocity.x = -ball2Velocity.x

        ball2Y = ball2.getCenter().getY()
        if ball2Y < 0 or ball2Y > win.getHeight():
            ball2Velocity.y = -ball2Velocity.y

        # Check if we should exit
        if win.checkKey() == "Escape":
            isRunning = False

        # Sleep for a bit so we're not running as fast as possible
        time.sleep(1/60)

    win.close()

if __name__ == "__main__":
    main()
