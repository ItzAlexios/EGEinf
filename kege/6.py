from turtle import *

tracer(0)
left(90)
screensize(5000, 5000)
size = 50
pendown()

right(90)

for i in range(7):
    rt(45)
    fd(11*size)
    rt(45)

penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x*size, y*size)
        dot(6, 'darkblue')

input()
done()