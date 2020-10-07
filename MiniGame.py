from graphics import *
from MiniGameClassEd import RememberTheShape
import random 

def main():

    win = GraphWin("Remember The Shape", 420, 420, autoflush=False)
    game = RememberTheShape()
    game.introGame(win)
    game.playGame(win) 
    

main()