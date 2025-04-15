from turtle import *

tracer(0)
left(90)
screensize(5000, 5000)
size = 18

pendown()

forward(25*size)
right(45)
forward(50*size)

penup()

backward(50*size)
right(45)
forward(15*size)
left(90)
forward(30*size)

pendown()

right(180)
forward(60*size)
backward(5*size)
right(90)
forward(31*size)

penup()

for x in range(-50, 50):
    for y in range(-60, 60):
        setpos(x*size, y*size)
        dot(4, 'blue')

input()
done()

'''
Ответ: 536
'''