"""  John Nava
     Program #4
     COSC 1306
     Fall 2019
"""
import turtle 
wn =turtle.Screen()

def drawU(Color):
    U = turtle.Turtle()
    U.color(Color)
    U.pensize(10)
    U.backward(10)
    U.forward(20)
    U.backward(10)
    U.right(90) 
    U.forward(80)
    U.left(45)
    U.forward(20)
    U.left(45)
    U.forward(40)
    U.left(45) 
    U.forward(20)
    U.left(45)
    U.forward(80)
    U.right(90)
    U.backward(10)
    U.forward(20)
    U.backward(10)

def drawH(Color):
    wn = turtle.Screen()
    U = turtle.Turtle()
    U.penup()
    U.goto(90,-60)
    U.color(Color)
    U.pensize(10)
    U.pendown() 
    U.backward(10)
    U.forward(20)
    U.backward(10)
    U.right(90)
    U.pendown()
    U.forward(95)
    U.right(90)
    U.backward(10)
    U.forward(20)
    U.backward(10)
    U.left(90)
    U.backward(48)
    U.right(90)
    U.forward(60) #The middle of the "H"
    U.right(90)
    U.forward(48)
    U.right(90)
    U.backward(10)
    U.forward(20)
    U.backward(10)
    U.right(270)
    U.backward(95)
    U.right(90)
    U.backward(10)
    U.forward(20)
    U.backward(10)

Color = input("Enter the color: Enter QUIT to quit: ")
while(Color != "QUIT"):
    IntInput = int(input("Enter your number: "))
    wn.clear()
    if IntInput % 3 == 0:
        drawU(Color)
    
    if IntInput % 5 == 0:
        drawH(Color)

    if IntInput % 3 ==0 and IntInput % 5 == 0:
        drawU(Color)
        drawH(Color)
    Color = input("Enter the color: Enter QUIT to quit: ")

        


