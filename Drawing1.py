#monChefDoeuvreDautomne
#This program draws a person is walking the dog
#
#Suhua Qin
#NourhanSaleh
#10/30/2015

import turtle as t

#draw the square head
t.fillcolor("black")
t.begin_fill()
def draw_square(side,color):
    for i in range(4):
        t.pencolor(color)
        t.forward(side)
        t.left(90)

draw_square(100,'black')   #call it
t.end_fill()

# Move the pen
t.penup()
t.left(180)
t.forward(35)
t.left(180)
t.pendown()

#draw a rectangle
t.pencolor('violet')
def draw_rectangle(l,w):
    for i in range(2):
        t.forward(l)
        t.right(90)
        t.forward(w)
        t.right(90)
        
draw_rectangle(180,115) # call it
t.left(90)

#draw the left arm
t.pencolor('brown')
def arm_drawing():
    t.left(150)
    t.forward(130)
    t.right(50)
    t.circle(20,220)
    t.left(10)
    t.forward(100)
arm_drawing()

#move the pen to right arm
t.penup()
t.right(60)
t.forward(175)
t.pendown()

#draw the right arm
t.right(50)
t.forward(100)
t.right(30)
t.circle(22,270)
t.right(60)
t.forward(125)

#move the pen to draw waist
def left_turn(x,y):
    t.penup()
    t.left(x)
    t.forward(y)
left_turn(140,100)

t.right(90)
t.forward(150)
t.left(90)
t.pendown()

#draw waist
t.pencolor('red')
t.circle(60,180)

#move pen for drawing legs
def right_turn(a,b,c):
    t.penup()
    t.right(a)
    t.forward(b)
    t.right(c)
right_turn(180,30,90)

t.forward(15)
t.left(90)
t.forward(5)
t.pendown()

#draw leg
t.pencolor('pink')
draw_rectangle(200,90)

#move to feet position
t.penup()
t.forward(200)
t.pendown()

#draw feet
t.pencolor('orange')
def draw_feet():
    t.circle(20)
    t.penup()
    t.right(90)
    t.forward(90)
    t.left(90)
    t.pendown()
    t.circle(20)#front foot
draw_feet()

#move to right hand 
t.penup()
t.left(133)
t.forward(300)
t.pendown()

#draw leash
t.pencolor("green")
draw_rectangle(15,250)



#draw dog
right_turn(100,200,50)
t.left(120)
t.forward(50)
t.right(30)
t.forward(20)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
draw_square(50,'blue')
t.end_fill()
    #change angle for body
t.right(60)
t.forward(70)
t.right(100)
draw_rectangle(150,60)
    #legs
t.forward(20)
t.left(90)
t.forward(20)
draw_feet()

#move to ball position
t.penup()
t.left(90)
t.forward(230)
t.pendown()

# ball
def ball(color2):
    for i in range(6):
        t.pencolor(color2)
        t.forward(30)
        t.left(60)

ball('violet')
#pen-move to another dog head
def pen_move(f):
    t.penup()
    t.forward(f)
    t.left(90)
    t.forward(20)
    t.pendown()
pen_move(100)
pen_move(100)

#another dog
draw_square(50,'violet')  

#pen-move to body
t.penup()
t.left(90)
t.forward(50)
t.left(90)
t.forward(140)
t.left(90)
t.right(180)
t.pendown()

#another dog
draw_rectangle(60,140)

#pen_move to feet position
t.penup()
t.forward(60)
t.right(90)
t.pendown()

#legs
t.forward(20)
t.left(90)
t.forward(20)
draw_feet()

#move pen to draw triangles
t.penup()
t.right(180)
t.forward(150)
t.pendown()
#triangle def :
def triangle():
    for i in range(3):
        t.forward(30)
        t.left(120)
        
for i in range(4):
    pen_move(140)
    triangle()










