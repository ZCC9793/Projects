"""
Zachary Coelho
Homework 01
"""

import turtle

turtle.pensize(2) #sets up the pen  size to have a size of two

def hex1(): # this def creates the first hexagon in the sequence
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(60)
    turtle.left(60)

def nexthex(): # this is the code that moves the turtle to the next spot to start the next hexagon
    turtle.forward(60)
    turtle.right(60)
    
def drawing(): # this function consolidates some code to draw the first part of the program
    hex1()
    nexthex()
    hex1()
    nexthex()
    hex1()
    nexthex()
    hex1()
    nexthex()
    hex1()
    nexthex()
    hex1()
    nexthex()

def part2(): #code to move the turtle to the next spot to start the second part of the drawing
    turtle.forward(60)



# main function that drives the program, and tells the turtle when to use the commands
def main():
    drawing()
    part2()
    drawing()
    print("Click on the 'X' button in the window titlebar to close the program")

main()
turtle.done()
