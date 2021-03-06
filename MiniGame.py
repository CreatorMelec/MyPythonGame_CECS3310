from graphics import *
import random 

def exitGame(win, finalScore):

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
        score = Text(Point(192.0,190.0),"Your total score was: " + str(finalScore))
        score.draw(win)
        win.getMouse()
        score.undraw()
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

def introGame(win):

    intro = Text(Point(192.0,190.0),"Welcome to Remember the Shape")
    intro.draw(win)
    cont = Text(Point(192.0, 210.0),"Click to Continue")
    cont.setSize(8)
    cont.setStyle("bold")
    cont.draw(win)
    win.getMouse()
    intro.undraw()
    cont.undraw()

    intro2 = Text(Point(192.0,190.0),"The Rules are simple:")
    intro2.draw(win)
    win.getMouse()
    intro2.undraw()

    intro3 = Text(Point(205.0,190.0),"Remember the Shape inside the square to win")
    intro3.draw(win)
    win.getMouse()
    intro3.undraw()

    intro4 = Text(Point(192.0,190.0),"Answers can be: square, circle, triangle, star")
    intro4.draw(win)
    win.getMouse()
    intro4.undraw()

    intro5 = Text(Point(205.0,190.0),"GOOD LUCK OUT THERE!")
    intro5.setSize(20)
    intro5.setStyle("bold")
    intro5.draw(win)
    win.getMouse()
    intro5.undraw()


def plays(win, totalScore):

    keepPlay = True
    finalScore = 0
    while keepPlay:

        PresentingSpace = Rectangle(Point(64.0,363.0),Point(357.0,50.0))
        PresentingSpace.draw(win)


        firstLine = Line(Point(64.0,210.0),Point(357.0,210.0))
        firstLine.draw(win)
        secondLine = Line(Point(210.0,50.0),Point(210.0,363.0))
        secondLine.draw(win)

   
        num1 = Text(Point(70.0,63.0),"1")
        num1.draw(win)
        num2 = Text(Point(347.0,62.0),"2")
        num2.draw(win)
        num3 = Text(Point(72.0,221.0),"3")
        num3.draw(win)
        num4 = Text(Point(349.0,222.0),"4")
        num4.draw(win)


        numberChoosen = draw(win)
        PresentingSpace.undraw()
        firstLine.undraw()
        secondLine.undraw()

        
        num1.undraw()
        num2.undraw()
        num3.undraw()
        num4.undraw()

        win.getMouse()

        squareNum = random.randint(1,4)
        guess = Text(Point(192.0,190.0),"What was the shape in square: " + str(squareNum))
        guess.draw(win)
        win.getMouse()
        guess.undraw()
        userInput = Entry(Point(192.0,190.0),8)
        userInput.setText("")
        userInput.draw(win)
        win.getMouse()
        answer = userInput.getText()
        win.getMouse()
        userInput.undraw()

        
        getTotal = shapes(numberChoosen,answer,win, squareNum, totalScore)
        question = Text(Point(192.0,190.0),"Do you want to keep playing?")
        question.draw(win)
        question1 = Text(Point(192.0, 210.0), "Press enter to continue or click to exit")
        question1.draw(win)
        win.getMouse()
        question.undraw()
        question1.undraw()
        finalScore = finalScore + getTotal

        exitGame(win, finalScore)
        

        


def draw(win):

    choosenNum = random.randint(1,7)

    if choosenNum == 1:
        first = Rectangle(Point(85.0, 180.0),Point(195.0, 70.0))
        first.setFill("red")
        first.draw(win)
        second = Circle(Point(285.0,125.0),55)
        second.setFill("blue")
        second.draw(win)
        third = Polygon(Point(85.0, 340.0),Point(185.0,340.0),Point(134.0, 240.0))
        third.setFill("yellow")
        third.draw(win)
        fourth = Polygon(Point(220.0, 280.0),Point(330.0,340.0),Point(290.0, 240.0),Point(230.0,340.0),Point(350.0,280.0))
        fourth.setOutline("green")
        fourth.setFill("green")
        fourth.draw(win)
            

    if choosenNum == 2:
        first = Rectangle(Point(85.0, 180.0),Point(195.0, 70.0))
        first.setFill("pink")
        first.draw(win)
        second = Circle(Point(285.0,290.0),55)
        second.setFill("green")
        second.draw(win)
        third = Polygon(Point(85.0, 340.0),Point(185.0,340.0),Point(134.0, 240.0))
        third.setFill("red")
        third.draw(win)
        fourth = Polygon(Point(220.0, 120.0),Point(330.0,180.0),Point(290.0, 80.0),Point(230.0,180.0),Point(350.0,120.0))
        fourth.setOutline("blue")
        fourth.setFill("blue")
        fourth.draw(win)

    if(choosenNum == 3):
        first = Rectangle(Point(85.0, 340.0),Point(195.0, 240.0))
        first.setFill("yellow")
        first.draw(win)
        second = Circle(Point(285.0,125.0),55)
        second.setFill("blue")
        second.draw(win)
        third = Polygon(Point(85.0, 180.0),Point(185.0,180.0),Point(134.0, 80.0))
        third.setFill("red")
        third.draw(win)
        fourth = Polygon(Point(220.0, 280.0),Point(330.0,340.0),Point(290.0, 240.0),Point(230.0,340.0),Point(350.0,280.0))
        fourth.setOutline("green")
        fourth.setFill("green")
        fourth.draw(win)

    if choosenNum == 4:
        first = Rectangle(Point(230.0, 180.0),Point(330.0, 70.0))
        first.setFill("brown")
        first.draw(win)
        second = Circle(Point(135.0,125.0),55)
        second.setFill("gray")
        second.draw(win)
        third = Polygon(Point(85.0, 340.0),Point(185.0,340.0),Point(134.0, 240.0))
        third.setFill("cyan")
        third.draw(win)
        fourth = Polygon(Point(220.0, 280.0),Point(330.0,340.0),Point(290.0, 240.0),Point(230.0,340.0),Point(350.0,280.0))
        fourth.setOutline("green")
        fourth.setFill("green")
        fourth.draw(win)

    if choosenNum == 5:
        first = Rectangle(Point(230.0, 340.0),Point(330.0, 240.0))
        first.setFill("cyan")
        first.draw(win)
        second = Circle(Point(135.0,125.0),55)
        second.setFill("purple")
        second.draw(win)
        third = Polygon(Point(230.0, 180.0),Point(330.0,180.0),Point(280.0, 80.0))
        third.setFill("blue")
        third.draw(win)
        fourth = Polygon(Point(75.0, 280.0),Point(185.0,340.0),Point(145.0, 240.0),Point(85.0,340.0),Point(205.0,280.0))
        fourth.setOutline("green")
        fourth.setFill("green")
        fourth.draw(win) 
    
    if choosenNum == 6:
        first = Rectangle(Point(230.0, 180.0),Point(330.0, 70.0))
        first.setFill("green")
        first.draw(win)
        second = Circle(Point(135.0,285.0),55)
        second.setFill("purple")
        second.draw(win)
        third = Polygon(Point(230.0, 340.0),Point(330.0,340.0),Point(280.0, 240.0))
        third.setFill("red")
        third.draw(win)
        fourth = Polygon(Point(75.0, 120.0),Point(185.0,180.0),Point(145.0, 80.0),Point(85.0,180.0),Point(205.0,120.0))
        fourth.setOutline("blue")
        fourth.setFill("blue")
        fourth.draw(win)
    
    if choosenNum == 7:
        first = Rectangle(Point(230.0, 340.0),Point(330.0, 240.0))
        first.setFill("green")
        first.draw(win)
        second = Circle(Point(135.0,285.0),55)
        second.setFill("red")
        second.draw(win)
        third = Polygon(Point(230.0, 180.0),Point(330.0,180.0),Point(280.0, 80.0))
        third.setFill("blue")
        third.draw(win)
        fourth = Polygon(Point(75.0, 120.0),Point(185.0,180.0),Point(145.0, 80.0),Point(85.0,180.0),Point(205.0,120.0))
        fourth.setOutline("yellow")
        fourth.setFill("yellow")
        fourth.draw(win)
    

    for i in range(2):
        update(1)
        first.undraw()
        second.undraw()
        third.undraw()
        fourth.undraw()
        
    
    return choosenNum
    


def shapes(numberChoosen,userInput,win, squareNum, totalScore):

    num1 = 1
    num2 = 2
    num3 = 3
    num4 = 4

    if numberChoosen == 1:
        first = "square"
        second = "circle"
        third = "triangle"
        fourth = "star"
       
        if num1 == squareNum:
            if first == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
            
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
     

        elif num2 == squareNum:
            if second == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
               
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
       

        elif num3 == squareNum:
            if third == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
                
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
       

        elif num4 == squareNum:
            if fourth == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
                
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
       

    if numberChoosen == 2:
        first = "square"
        second = "star"
        third = "triangle"
        fourth = "circle"
        if num1 == squareNum:
            if first == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
              
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
        

        elif num2 == squareNum:
            if second == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
                
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
       

        elif num3 == squareNum:
            if third == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
               
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
        

        elif num4 == squareNum:
            if fourth == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
                
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
       

    if numberChoosen == 3:
        first = "triangle"
        second = "circle"
        third = "square"
        fourth = "star"
        if num1 == squareNum:
            if first == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
               
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
      

        elif num2 == squareNum:
            if second == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
               
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
    

        elif num3 == squareNum:
            if third == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
                
               
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
       

        elif num4 == squareNum:
            if fourth == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
                
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
       

    if numberChoosen == 4:
        first = "circle"
        second = "square"
        third = "triangle"
        fourth = "star"
        if num1 == squareNum:
            if first == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
              
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
        

        elif num2 == squareNum:
            if second == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
              
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
            

        elif num3 == squareNum:
            if third == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
                
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
            

        elif num4 == squareNum:
            if fourth == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
              
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()

    if numberChoosen == 5:
        first = "circle"
        second = "triangle"
        third = "star"
        fourth = "square"
        if num1 == squareNum:
            if first == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
              
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
        

        elif num2 == squareNum:
            if second == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
              
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
            

        elif num3 == squareNum:
            if third == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
                
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
            

        elif num4 == squareNum:
            if fourth == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
              
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()


    if numberChoosen == 6:
        first = "star"
        second = "square"
        third = "circle"
        fourth = "triangle"
        if num1 == squareNum:
            if first == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
              
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
        

        elif num2 == squareNum:
            if second == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
              
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
            

        elif num3 == squareNum:
            if third == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
                
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
            

        elif num4 == squareNum:
            if fourth == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
              
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()

    if numberChoosen == 7:
        first = "star"
        second = "triangle"
        third = "circle"
        fourth = "square"
        if num1 == squareNum:
            if first == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
              
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
        

        elif num2 == squareNum:
            if second == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
              
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
            

        elif num3 == squareNum:
            if third == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
                
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
            

        elif num4 == squareNum:
            if fourth == userInput:
                answer = Text(Point(192.0,190.0),"You are Correct!")
                answer.draw(win)
                win.getMouse()
                answer.undraw()
                totalScore = totalScore + 1
              
            else:
                answer = Text(Point(192.0,190.0),"You are Incorrect! :( ")
                answer.draw(win)
                win.getMouse()
                answer.undraw()

    return totalScore
            
        

def main():

    win = GraphWin("Remember The Shape", 420, 420, autoflush=False)
    totalScore = 0

    introGame(win)
    plays(win, totalScore) 
    

main()