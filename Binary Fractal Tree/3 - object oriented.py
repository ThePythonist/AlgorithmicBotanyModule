#Draw a binary fractal tree

from turtle import *
from random import uniform

#Set turtle position to the centre of the bottom edge of the screen
penup()
sety(-window_height()/2)
pendown()

#This list will keep track of the state of the turtle at each iteration
stack = []

#Instances of this class will contain the turtle's current state
class TurtleState:
    def __init__(self):
        self.x = xcor()
        self.y = ycor()
        self.h = heading()
    
    def activate(self):
        penup()
        setx(self.x)
        sety(self.y)
        seth(self.h)
        pendown()

#This function will push the current turtle state to the stack
def push_state():
    stack.append(TurtleState())

#This function will pop the turtle state from the stack
def pop_state():
    stack.pop().activate()

#Uniformly distributed number up to a proportion of variance away from x e.g. variance = 0.1 means x +- 10%
def randomize(x, variance):
    return x * uniform(1-variance, 1+variance)

#This class contains the data about how the branches vary as you get deeper into the tree
class VarianceData:
    def __init__(self, lengthMultiplier, childAngle, lengthVariance, angleVariance):
        self.lengthMultiplier = lengthMultiplier
        self.childAngle = childAngle
        self.lengthVariance = lengthVariance
        self.angleVariance = angleVariance

#This class will contain the data of a branch, and a link to all of its children.
#Note that the tree itself will also be an instance of this class
class Branch:
    def __init__(self, length, angle, variance):
        self.length = length
        self.angle = angle #Angle relative to parent branch
        self.variance = variance
        self.children = []
    
    def grow(self, numLayers):
        if numLayers > 1:
            #Iterate over the angles of the children to create
            for childAngle in [self.variance.childAngle, -self.variance.childAngle]:
                newLength = randomize(self.length * self.variance.lengthMultiplier, self.variance.lengthVariance)
                print(childAngle)
                newAngle = randomize(childAngle, self.variance.angleVariance)
                child = Branch(newLength, newAngle, self.variance)
                child.grow(numLayers-1)
                self.children.append(child)
    
    def draw(self):
        left(self.angle)
        forward(self.length)
        for child in self.children:
            push_state()
            child.draw()
            pop_state()

#Create a VarianceData object with a length multiplier of 0.5 and deviation angle of 45 degrees, length variance of 0.5, angle variance of 0.5
variance = VarianceData(0.5, 45, 0.5, 0.5)

#Create a tree with a trunk length of 300 at 90 degrees to the horizontal
tree = Branch(300, 90, variance)

#Grow the tree 5 layers deep
tree.grow(5)

#Draw the tree
tree.draw()

#Make sure screen stays open once drawing is finished
getscreen()._root.mainloop()