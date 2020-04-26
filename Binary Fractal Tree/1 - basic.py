#Draw a binary fractal tree

from turtle import *

#Set turtle position to the centre of the bottom edge of the screen
penup()
sety(-window_height()/2)
pendown()
left(90)

#This list will keep track of the state of the turtle at each iteration
stack = []

#This function will push the coordinates of the turtle and the direction it is facing to the stack
def push_state():
    x = xcor()
    y = ycor()
    h = heading()
    stack.append([x, y, h])

#This function will pop the coordinates of the turtle and the direction it is facing from the stack
def pop_state():
    penup()
    x, y, h = stack.pop()
    setx(x)
    sety(y)
    seth(h)
    pendown()

#This is a recursive function which will draw the tree
def draw_tree(numLayers, length, lengthMultiplier, angle):
    #Draw the line
    forward(length)
    
    #Check whether this branch should have children
    if numLayers > 1:
        #Draw left child
        push_state()
        left(angle)
        draw_tree(numLayers - 1, length * lengthMultiplier, lengthMultiplier, angle)
        pop_state()

        #Draw right child
        push_state()
        right(angle)
        draw_tree(numLayers - 1, length * lengthMultiplier, lengthMultiplier, angle)
        pop_state()
    
#Draw a tree with 5 layers, initial branch length of 200, length multiplier of 0.7 and deviation angle of 45 degrees
draw_tree(5, 200, 0.7, 45)

#Make sure screen stays open once drawing is finished
getscreen()._root.mainloop()