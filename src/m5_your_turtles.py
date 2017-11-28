"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Kayleigh Doyle.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
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
import rosegraphics as rg

window = rg.TurtleWindow()

terry = rg.SimpleTurtle('turtle')
terry.pen_up()
terry.left(180)
terry.forward(50)
terry.pen_down()
terry.pen = rg.Pen('dark green',10)
terry.right(90)
terry.forward(100)
terry.backward(50)
terry.right(30)
terry.forward(60)
terry.backward(60)
terry.right(120)
terry.forward(60)

laurel = rg.SimpleTurtle()
laurel.speed = 20
laurel.pen_up()
laurel.left(180)
laurel.forward(150)
laurel.pen_down()


for k in range(15):
    laurel.pen = rg.Pen('red', 3)
    laurel.draw_circle(5+k)
    laurel.forward(6+k)

karen = rg.SimpleTurtle()
karen.speed = 20
karen.pen_up()
karen.left(140)
karen.forward(150)
karen.pen_down()


for k in range(15):
    karen.pen = rg.Pen('orange', 3)
    karen.draw_circle(5+k)
    karen.forward(6+k)

steve = rg.SimpleTurtle()
steve.speed = 20
steve.pen_up()
steve.left(90)
steve.forward(150)
steve.pen_down()

for k in range(15):
    steve.pen = rg.Pen('yellow', 3)
    steve.draw_circle(5+k)
    steve.forward(6+k)

hugo = rg.SimpleTurtle()
hugo.speed = 20
hugo.pen_up()
hugo.left(30)
hugo.forward(150)
hugo.pen_down()

for k in range(15):
    hugo.pen = rg.Pen('blue',3)
    hugo.draw_circle(5+k)
    hugo.forward(6+k)

marvin = rg.SimpleTurtle()
marvin.speed = 20
marvin.pen_up()
marvin.forward(150)
marvin.pen_down()

for k in range(15):
    marvin.pen = rg.Pen('purple',3)
    marvin.draw_circle(5+k)
    marvin.forward(6+k)

mildred = rg.SimpleTurtle() 
mildred.speed = 20
mildred.pen_up()
mildred.left(180)
mildred.forward(100)
mildred.left(90)
mildred.forward(40)
mildred.left(90)
mildred.pen_down()

for k in range(30):
    mildred.pen = rg.Pen('black',3)
    mildred.draw_circle(5)
    mildred.forward(8)
