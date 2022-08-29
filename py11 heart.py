d1={"Pen":"an object that a hand can hold to write something on paper","Man":"a male human being","Woman":
    "a female human being","Mutable":"that can be changed","Immutable":"that cannot be changed"}
print("Enter a word to know its meaning")
word=input()
b=word.capitalize()
print(b,"=",d1[b])
import time


import turtle
t=turtle.Turtle()
t.color("red")
t.begin_fill()
t.fillcolor("red")
t.left(40)        #its 40 degree left from x axis or 0 degree
t.forward(180)
t.circle(90,200)

t.right(120)        #or t.setheading(120)
t.circle(90,200)   #instead of 200 ,360 will make a full circle and -90 will be in clockwise direction
t.forward(180)
t.end_fill()
time.sleep(3)

