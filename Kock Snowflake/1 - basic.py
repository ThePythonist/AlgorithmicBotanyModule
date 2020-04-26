#Draw a koch snowflake

from turtle import *

#Recursively draw sides of the snowflake
def draw_side(length, numLayers):
    if numLayers == 1:
        forward(length)
    else:
        draw_side(length/3, numLayers-1)
        left(60)
        draw_side(length/3, numLayers-1)
        right(120)
        draw_side(length/3, numLayers-1)
        left(60)
        draw_side(length/3, numLayers-1)

#Snowflake will have side length 300 and will be 5 layers deep
sideLength = 300
numLayers = 5

#Set move the turtle such that the snowflake is centred
#Moving to the bottom left vertex
penup()
setx(-sideLength/2) #Half the side length left of centre
sety(-sideLength * 3**0.5/4) # sqrt(3)/4 of the length below centre
pendown()

#Set turtle speed
speed(10)

#Draw left edge
left(60)
draw_side(sideLength, numLayers)

#Draw right edge
right(120)
draw_side(sideLength, numLayers)

#Draw bottom edge
right(120)
draw_side(sideLength, numLayers)

#Make sure screen stays open once drawing is finished
getscreen()._root.mainloop()