import turtle #brings the module in
import time #allows to work with time in Python
from turtle import * #brings object from the module (turtle)
from random import * #all the definitions from random become part of the current name space

speed(0) #set the turtle speed to the highest
#setup the background colour
screen = turtle.Screen()
screen.bgcolor("#FF8364") #making the background colour to be #FF8364

#move to starting point
turtle.up() #raising the turtle (pen) from the drawing surface
turtle.goto(-640,300) #moving the turtle to the specified x and y position
turtle.down() #lowering the turtle (pen) from the drawing surface

#title box of the project
turtle.pencolor("black") #changing the pen colour of turtle to the specified colour
turtle.pensize(3) #making the size of the pen becomes thicker than normal
turtle.forward(1280) 
turtle.left(90)   #rotate the turtle to the left by 90 degrees
turtle.forward(60)
turtle.left(90)
turtle.forward(1280)    #moving turtle forward to 1280 steps (pixels) in the current direction
turtle.left(90)
turtle.forward(60)

#letters C starting point
turtle.up()
turtle.goto(-250,345)
turtle.down()

#letters C on title
turtle.pencolor("black")
turtle.pensize(3)
turtle.left(90)
turtle.forward(30)
turtle.left(180)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)

#letters O starting point
turtle.up()
turtle.goto(-210,315)
turtle.down()

#letters O on title
turtle.fillcolor("skyblue") #changing the fill colour of turtle to skyblue
turtle.begin_fill() #enclosing a set of turtles command that will draw a filled shape using black colour
for i in range(2): #asking the turtle to move 2 times (steps) in order to create a square shape
    turtle.forward(30)  #with the specified direction and angle
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
turtle.end_fill()

#letters U starting point
turtle.up()
turtle.goto(-170,345)
turtle.down()

#letters U on title
turtle.right(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)

#letters N starting point
turtle.up()
turtle.goto(-130,315) #moving the turtle to the specified x and y position
turtle.down()

#letters N on title
turtle.forward(30)
turtle.right(90)  #rotate the turtle to the right by 90 degrees
turtle.forward(5)
turtle.right(60)
turtle.forward(33)
turtle.left(60)
turtle.forward(5)
turtle.left(90)
turtle.forward(30)

#letters T starting point
turtle.up()
turtle.goto(-80,315)
turtle.down()

#letters T on title
turtle.forward(30)
turtle.right(90)
turtle.forward(15)
turtle.right(180)
turtle.forward(30)

#letters R starting point
turtle.up()
turtle.goto(-40,345)
turtle.down()

#letters R on title
turtle.fillcolor("lightgreen") #changing the fill colour of turtle to lightgreen
turtle.begin_fill()
for i in range(2): #asking the turtle to move 2 times (steps) in order to create a square shape 
    turtle.forward(20) #with the specified direction and angle
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
turtle.end_fill() 
turtle.left(90)
turtle.forward(20)
turtle.right(60)
turtle.forward(20)
turtle.left(180)
turtle.forward(20)
turtle.right(120)  #rotate the turtle to the right by 120 degrees
turtle.forward(10)

#letters Y starting point
turtle.up()
turtle.goto(-23,315)
turtle.down()

#letters Y on title
turtle.right(180)
turtle.forward(15)
turtle.left(30)
turtle.forward(20)
turtle.right(180)
turtle.forward(20)
turtle.left(120)
turtle.forward(20)
turtle.left(30)

#letters F starting point
turtle.up()
turtle.goto(10,315)
turtle.down()

#letters F on title
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(180)
turtle.forward(20)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(20)

#letters L starting point
turtle.up()
turtle.goto(60,315)
turtle.down()

#letters L on title
turtle.right(180)
turtle.forward(20)
turtle.right(90)
turtle.forward(30)

#letters A starting point
turtle.up()
turtle.goto(80,330)
turtle.down()

#letters A on title
turtle.fillcolor("lightpink") #changing the fill colour of turtle to lightpink
turtle.begin_fill()
for i in range(3): #asking the turtle to move 3 times (steps) in order to create a triangle shape
    turtle.forward(15)  #with the specified direction and angle
    turtle.left(120)
    turtle.forward(15)
turtle.end_fill()

#letters G starting point
turtle.up()
turtle.goto(105,330)
turtle.down()

#letters G on title
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)

#letters S starting point
turtle.up()
turtle.goto(130,315)
turtle.down()

#letters S on title
turtle.forward(20)
turtle.left(90)
turtle.forward(15)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(20)

#Indonesia Flag starting point
turtle.up()
turtle.goto(-600,215)
turtle.down()

#Indonesia Flag (Red)
turtle.fillcolor("red") #changing the fill colour of turtle to red
turtle.begin_fill()
turtle.right(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(80)
turtle.end_fill()

#Indonesia Flag (White)
turtle.fillcolor("white") #changing the fill colour of turtle to white
turtle.begin_fill()
turtle.forward(80)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()

#Octagon patterns starting point
turtle.up()
turtle.goto(-300,130)
turtle.down()

#Octagon Patterns
turtle.pencolor("maroon") #changing the pen colour of turtle to maroon
turtle.pensize(5)

for i in range(8):  #eight octagon shapes will be created with the specified angle
    turtle.left(45)
    for i in range(8):  #asking the turtle to move 8 times (steps) in order to create an octagon shape
        turtle.forward(20)  #with the specified direction and angle
        turtle.left(45)
        
#Japan flag starting point
turtle.up()
turtle.goto(-200,215)
turtle.down()

#Japan flag (white)
turtle.pencolor("black")  #changing the pen colour of turtle to black
turtle.pensize(3)
turtle.fillcolor("white") #changing the fill colour of turtle to white
turtle.begin_fill()
turtle.left(90)
turtle.forward(160)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(160)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(160)
turtle.end_fill()

#Japan flag starting point (red circle)
turtle.up()
turtle.goto(-135,138)
turtle.down()

#Japan flag (red circle)
turtle.fillcolor("red") #changing the fill colour of turtle to red
turtle.begin_fill()
turtle.circle(35) #draw a circle with 35 radius
turtle.end_fill()

#Octagon patterns starting point
turtle.up()
turtle.goto(100,130)
turtle.down()

#Octagon Patterns
turtle.pencolor("maroon") #changing the pen colour of turtle to maroon
turtle.pensize(5) 

for i in range(8):
    turtle.left(45)
    for i in range(8):
        turtle.forward(20)
        turtle.left(45)

#Pakistan flag starting point
turtle.up()
turtle.goto(200,55)
turtle.down()

#Pakistan flag (Dark green rectangle)
turtle.pencolor("black") #changing the pen colour of turtle to black
turtle.pensize(3)
turtle.fillcolor("#01411C") #changing the fill colour of turtle to #01411C
turtle.begin_fill()
for i in range (2): #asking the turtle to move 2 times (steps) in order to create a rectangle shape
    turtle.left(90) #with the specified direction and angle
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(160)
turtle.end_fill()

#Pakistan flag (White rectangle)
turtle.fillcolor("white") #changing the fill colour of turtle to white
turtle.begin_fill()
for i in range (2): #asking the turtle to move 2 times (steps) in order to create a rectangle shape
    turtle.left(90) #with the specified direction and angle
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(160)
turtle.end_fill()

#Pakistan flag (moon shape) starting point
turtle.up()
turtle.goto(290,130)

#Pakistan flag (moon shape)
turtle.fillcolor("white") #changing the fill colour of turtle to white
turtle.begin_fill()
turtle.circle(40) #draw a circle with 40 radius
turtle.end_fill()


turtle.goto(310,140)
turtle.fillcolor("#01411C") #changing the fill colour of turtle to #01411C
turtle.begin_fill()
turtle.circle(35)
turtle.end_fill()

#Pakistan flag (star shape) starting point
turtle.goto(350,180)

#Pakistan flag (star shape)
turtle.fillcolor("white") #changing the fill colour of turtle to white
turtle.begin_fill()
for i in range(5): #asking the turtle to move 5 times (steps) in order to create a star shape
    turtle.forward(30) #with the specified direction and angle
    turtle.left(144)
turtle.end_fill()

#Arrows
turtle.goto(440,130)
turtle.pencolor("maroon") #changing the pen colour of turtle to maroon
turtle.down()
turtle.pensize(3)

turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(80)
turtle.right(90)

turtle.fillcolor("yellow") #changing the fill colour of turtle to yellow
turtle.begin_fill()
for i in range(3): #asking the turtle to move 3 times (steps) in order to create a triangle shape
    turtle.forward(10)  #with the specified direction and angle
    turtle.left(120)
    turtle.forward(5)
turtle.end_fill()

#Olympic Logo starting point
turtle.up()
turtle.goto(540,-15)
turtle.down()

#Making Olympic Game Logo
#Black Ring
turtle.pencolor("Black") #changing the pen colour of turtle to black
turtle.pensize(4)
turtle.circle(20) #draw a circle with 20 radius

#Blue Ring
turtle.up()
turtle.goto(500,10)
turtle.down()

turtle.pencolor("Blue") #changing the pen colour of turtle to blue
turtle.circle(20)

#Red Ring
turtle.up()
turtle.goto(580,-40)
turtle.down()

turtle.pencolor("Red") #changing the pen colour of turtle to red
turtle.circle(20)

#Yellow Ring
turtle.up()
turtle.goto(510,-18)
turtle.down()

turtle.pencolor("Yellow") #changing the pen colour of turtle to yellow
turtle.circle(20)

#Green Ring
turtle.up()
turtle.goto(550,-45)
turtle.down()

turtle.pencolor("Green") #changing the pen colour of turtle to green
turtle.circle(20)

#Texts
turtle.pencolor("Black") #changing the pen colour of turtle to black
turtle.up()
turtle.goto(490,-140)
turtle.down()

turtle.write("TURTLE", font=("Apple Chancery",15,"underline")) #placing a text "TURTLE" with the specified type of font, size, and characteristics

turtle.up()
turtle.goto(460,-190)
turtle.down()

turtle.write("RACE", font=("Apple Chancery",35,"italic", "bold")) #placing a text "RACE" with the specified type of font, size, and characteristics

turtle.up()
turtle.goto(452,-220)
turtle.down()

turtle.write("OLYMPIC", font=("Apple Chancery",25, "bold")) #placing a text "OLYMPIC" with the specified type of font, size, and characteristics

turtle.up()
turtle.goto(490,-245)
turtle.down()

turtle.write("GAMES", font=("Apple Chancery",15,"underline")) #placing a text "GAMES" with the specified type of font, size, and characteristics

#Arrows
turtle.up()
turtle.goto(530,-265)
turtle.pencolor("maroon") 
turtle.down()
turtle.pensize(3)

turtle.left(90)
turtle.forward(45)
turtle.right(90)
turtle.forward(40)
turtle.right(90)

turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(3):  #asking the turtle to move 3 times (steps) in order to create a triangle shape
    turtle.forward(10) #with the specified direction and angle
    turtle.left(120)
    turtle.forward(5)
turtle.end_fill()

#Indonesia Text
turtle.pencolor("Black")
turtle.up()
turtle.goto(-530,30)
turtle.down()

turtle.write("INDONESIA", font=("Apple Chancery",10,"bold")) #placing a text "INDONESIA" with the specified type of font, size, and characteristics

#Japan Text
turtle.pencolor("Black")
turtle.up()
turtle.goto(-115,30)
turtle.down()

turtle.write("JAPAN", font=("Apple Chancery",10,"bold")) #placing a text "JAPAN" with the specified type of font, size, and characteristics

#Pakistan Text
turtle.pencolor("Black")
turtle.up()
turtle.goto(270,30)
turtle.down()

turtle.write("PAKISTAN", font=("Apple Chancery",10,"bold")) #placing a text "PAKISTAN" with the specified type of font, size, and characteristics

#Finish Line
turtle.up()
turtle.goto(-600,-300)
turtle.down()

turtle.right(90)
def draw_square(color): #define a draw_square function with colour applied
    turtle.color(color) #give a colour of the turtle (pen colour)
    for i in range(0,4):  #asking the turtle to move 4 times (steps) in order to create a square shape  
        turtle.fd(30)     #with the specified direction and angle
        turtle.lt(90)
    turtle.fd(40)

draw_square("lightblue") #draw the square with light blue pen colour
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")
draw_square("lightblue")

turtle.up()
turtle.goto(-600,-270)
turtle.down()

turtle.forward(1000)
turtle.right(90)
turtle.forward(30)

#Finish Line Text
turtle.pencolor("black") #turn the pen colour to be black again
turtle.up()
turtle.goto(-150,-340)
turtle.down()
turtle.write("FINISH LINE", font=("Apple Chancery",20,"bold", "italic"))    #placing a text "FINISH LINE with the specified type of font, size, and characteristics

#Square Spiral 1
turtle.pencolor("maroon")   #changing the pen colour of turtle to maroon
turtle.pensize(2)
turtle.up()
turtle.goto(-300,-90)
turtle.down()

for i in range (140):  #asking the turtle to move 140 times (steps) in order to create a square spiral shape
    turtle.forward(i) #turtle will move forward by 140 pixels (steps)
    turtle.left(91) #turtle will turn left by 91 degrees to make the shape spiral

#Square Spiral 2
turtle.up()
turtle.goto(100,-90)
turtle.down()

for i in range(140):
   turtle.forward(i)
   turtle.left(91)
    
#Indonesia Turtle-Red
ind_turtle=Turtle() #creating the first turtle for Indonesia country
ind_turtle.color("Red") #fill the Indonesian turtle colour to red
ind_turtle.shape("turtle")  #change the shape of ind_turtle to "Turtle" shape
ind_turtle.shapesize(1.5)   #change the size of turtle to be a bit bigger
ind_turtle.penup()
ind_turtle.goto(-500,10)
ind_turtle.right(90)
ind_turtle.pendown()

#Japan Turtle-White
jpn_turtle=Turtle() #creating the second turtle for Japan country
jpn_turtle.color("White")   #fill the Japanese turtle colour to white
jpn_turtle.shape("turtle")  #change the shape of jpn_turtle to "Turtle" shape
jpn_turtle.shapesize(1.5)   #change the size of turtle to be a bit bigger
jpn_turtle.penup()
jpn_turtle.goto(-100,10)
jpn_turtle.right(90)
jpn_turtle.pendown()

#Pakistan Turtle-Green
pkt_turtle=Turtle() #creating the third turtle for Pakistan country
pkt_turtle.color("#01411C") #fill the Pakistan turtle colour to #01411C
pkt_turtle.shape("turtle")  #change the shape of jpn_turtle to "Turtle" shape
pkt_turtle.shapesize(1.5)   #change the size of turtle to be a bit bigger
pkt_turtle.penup()
pkt_turtle.goto(300,10)
pkt_turtle.right(90)
pkt_turtle.pendown()

#Pause for one second before racing
time.sleep(1)

#Move the Turtles
for i in range(107):   #turtles will be running 107 times to reach the finish line (whoever crosses finish line first, they are the winner)
    ind_turtle.forward(randint(1,5))
    jpn_turtle.forward(randint(1,5)) #the three turtles will be running 
    pkt_turtle.forward(randint(1,5)) #between 1-5 pixels of distance randomly

turtle.hideturtle() #making the turtle invisible
turtle.exitonclick() #turtle will be terminated or closed or exit when its clicked





