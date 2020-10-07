from graphics import *
from MiniGameClassEd import RememberTheShape
import random 

def main():

    win = GraphWin("Remember The Shape", 420, 420, autoflush=False)
    finalScore = 0
    game = RememberTheShape()
    game.introGame(win)

    keepPlay = True
    while keepPlay:
        
        game.playGame(win) 
        enterKey = win.checkKey()
        if enterKey == 'Return':
            keepPlay = True
            text1 = Text(Point(192.0,190.0),"Next Round")
            text1.draw(win)
            win.getMouse()
            text1.undraw()

        elif win.getMouse():
            keepPlay = False
            goodbye = Text(Point(192.0,190.0),"Thank you for playing! :D")
            goodbye.setSize(20)
            goodbye.setStyle("bold")
            goodbye.draw(win)
            win.getMouse()
            goodbye.undraw()
            finalScore = game.getFinalScore(win)
            getName = Text(Point(192.0,190.0),"Please enter your name for records")
            getName.draw(win)
            win.getMouse()
            getName.undraw()
            userName = Entry(Point(192.0, 190.0), 10)
            userName.setText("")
            userName.draw(win)
            win.getMouse()
            userName = userName.getText()
    

            records = open("Rankings.txt", "w")
            records.write(userName)
            records.write(" ")
            records.write(str(finalScore))
            records.close()
            win.close()
    

main()