"""John Nava
Program #4: Drawing shapes using the turtle module
COSC 1306
Fall 2019
This program implements several functions to draw shapes using the Turtle module. """

import turtle

def setColor (num):
    if num == 1:
        return 'Red'
    elif num == 2:
        return 'Green' 
    elif num == 3:
        return 'Blue'
    else: 
        return 'Yellow'


def drawTriangle (shape,sideLength,lineColor,fillColor):
    shape.clear()
    shape.color(setColor(lineColor),setColor(fillColor))
    shape.begin_fill()
    for i in range(3):
        shape.forward(sideLength)
        shape.left(int(360/3))
    shape.end_fill()
    
def drawSquare (shape,sideLength,lineColor,fillColor):
    shape.clear()
    shape.color(setColor(lineColor),setColor(fillColor))
    shape.begin_fill()
    for i in range(4):
        shape.forward(sideLength)
        shape.left(int(360/4))
    shape.end_fill()

def drawPentagon (shape,sideLength,lineColor,fillColor):
    shape.clear()
    shape.color(setColor(lineColor),setColor(fillColor))
    shape.begin_fill()
    for i in range(5):
        shape.forward(sideLength)
        shape.left(int(360/5))
    shape.end_fill()
    
def drawHexagon (shape,sideLength,lineColor,fillColor):
    shape.clear()
    shape.color(setColor(lineColor),setColor(fillColor))
    shape.begin_fill()
    for i in range(6):
        shape.forward(sideLength)
        shape.left(int(360/6))
    shape.end_fill()
    
def drawOctagon (shape,sideLength,lineColor,fillColor):
    shape.clear()
    shape.color(setColor(lineColor),setColor(fillColor))
    shape.begin_fill()
    for i in range(8):
        shape.forward(sideLength)
        shape.left(int(360/8))
    shape.end_fill()

# Write your drawPolygon function here 
def drawPolygon (shape, Type, sideLength,LColor,fill):
    if shapeType == 3:
        drawTriangle (shape,sideLength,LColor,fill)
    if shapeType == 4:
        drawSquare (shape,sideLength,LColor,fill)
    if shapeType == 5:
        drawHexagon (shape,sideLength,LColor,fill)
    if shapeType == 6:     
        drawOctagon (shape,sideLength,LColor,fill)

shape = turtle.Turtle()
shape.shape('blank')
window = turtle.Screen()
drawTriangle(shape,100,1,3)
drawSquare(shape,100,1,3)
drawPentagon(shape,100,1,3)
drawHexagon(shape,100,1,3)
drawOctagon(shape,100,1,3)
window.exitonclick()
