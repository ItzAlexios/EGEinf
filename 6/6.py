from turtle import *

tracer(0)
left(90)
screensize(5000, 5000)
size = 30

pendown()

for i in range(2):
    forward(24*size)
    right(90)
    forward(10*size)
    right(90)

forward(3*size)
left(90)
forward(13*size)
right(90)

for i in range(2):
    forward(9*size)
    right(90)
    forward(32*size)
    right(90)

penup()

for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*size, y*size)
        dot(6, 'cyan')

input()
done()

'''
A1 = 11; B1 = 25
A2 = 10; B2 = 33

Ответ: 330
'''