from graphics import *

def main():
    win = GraphWin("Ball Test", 500, 500)
    isRunning = True
    while isRunning:
        ball = Circle(Point(100, 100), 10)
        ball.setFill("red")
        ball.draw(win)
        if win.checkKey() == "Escape":
            isRunning = False
    win.close()

if __name__ == "__main__":
    main()
