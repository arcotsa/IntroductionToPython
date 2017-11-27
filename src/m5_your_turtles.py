"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Satya Arcot.
"""
########################################################################
# DONEs: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg
########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
window = rg.TurtleWindow()

green_turtle = rg.SimpleTurtle('turtle')
green_turtle.pen = rg.Pen('green', 15)
green_turtle.speed = 12
radius = 150
for k in range(30):
    green_turtle.draw_circle(radius)

    green_turtle.pen_up()
    green_turtle.right(90)
    green_turtle.forward(7)
    green_turtle.pen_down()

    radius = radius - 10

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 7)
red_turtle.speed = 12
size = 200
for k in range(15):
    red_turtle.draw_square(size)

    red_turtle.pen_up()
    red_turtle.left(90)
    red_turtle.forward(10)
    red_turtle.pen_down()

    size = size - 20
