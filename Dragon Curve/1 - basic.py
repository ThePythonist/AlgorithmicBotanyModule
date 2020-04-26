#Draw a dragon curve

from turtle import *

#Recursively draw sides of the curve
#Since the line segments alternate between bending left and right, we need a parameter to tell us which to do
def draw_side(length, numLayers, leftFirst=False):
    if numLayers == 1:
        forward(length)
    else:
        #Ternary operator - very handy
        dir1 = left if leftFirst else right
        dir2 = right if leftFirst else left

        #Split the line segment recursively into two
        dir1(45)
        draw_side(length / (2 ** 0.5), numLayers-1, False)
        dir2(90)
        draw_side(length / (2 ** 0.5), numLayers-1, True)
        dir1(45)

#Curve will have initial side length 300 and will be 10 layers deep
sideLength = 300
numLayers = 10

#Set move the turtle such that the snowflake is centred
#Moving to the bottom left vertex
penup()
setx(-sideLength/2)
pendown()

#Draw the curve
draw_side(sideLength, numLayers)

#Make sure screen stays open once drawing is finished
getscreen()._root.mainloop()