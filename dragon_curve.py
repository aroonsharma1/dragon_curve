"""This program produces a dragon curve fractal based on the user's prompted number of iterations. 
   See http://en.wikipedia.org/wiki/Dragon_curve and https://www.youtube.com/watch?v=wCyC-K_PnRY
   for the math details. At a high level, the curve is defined by the directions Left, Right, Up, 
   and Down, which are denoted by a list of characters L, R, U, and D respectively. To create the curve, 
   think of your pen on a piece of paper and your pen drawing a line in the direction specified by the
   current item in the list. For example, L U means to draw a line left and then a line up."""
 
import turtle

"""functions"""

"""creates a new list that is the reverse of the input list called curve"""
def reverse_curve(curve):
    reversed_curve = []
    for i in range(0, len(curve)):
        reversed_curve.append(curve[len(curve) - i - 1])
    return reversed_curve
    
"""transforms a list according to the following:
        L --> U
        R --> D
        U --> R
        D --> L """
def transform_curve(curve):
    transformed_curve = []
    for item in curve:
        if item == "L":
            transformed_curve.append("U")
        elif item == "R":
            transformed_curve.append("D")
        elif item == "U":
            transformed_curve.append("R")
        elif item == "D":
            transformed_curve.append("L")
    return transformed_curve

"""performs one round of reverse_curve and one round of transform_curve
   per iteration, which the user decides"""
def dragon_curve(curve, number_of_iterations):
    for i in range(number_of_iterations):
        curve += transform_curve(reverse_curve(curve))
    return curve
    
"""draws the dragon curve using turtle grpahics"""
def draw_curve(curve, linewidth):
    turtle.title("Dragon Curve")
    turtle.hideturtle()
    turtle.setup(width = 0.8, height = 0.8)
    turtle.speed("fastest")
    for item in curve:
        if item == "R":
            turtle.setheading(0)
        elif item == "U":
            turtle.setheading(90)
        elif item == "L":
            turtle.setheading(180)
        elif item == "D":
            turtle.setheading(270)
        else:
            print "ERROR: Invalid direction %s detected! Only use the directions U, D, L, and R for Up, Down, Left, and Right respectively" % item
            quit()
        turtle.forward(linewidth)
    turtle.exitonclick()
        
"""main program starts here"""
curve = ["L", "U"]
number_of_iterations = int(raw_input("Enter in the number of iterations: ")) #will throw an error if what is entered is not an integer
number_of_lines = 2**(number_of_iterations+1)

"""determine the width of the line to draw with"""
if number_of_iterations <= 8:
    linewidth = 10
elif number_of_iterations <= 11:
    linewidth = 5
else:
    linewidth = 2
       
"""compute the dragon curve and draw it"""
d_curve = dragon_curve(curve, number_of_iterations)
draw_curve(d_curve, linewidth)