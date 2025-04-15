from turtle import *

lt(90)
tracer(0)
screensize(5000, 5000)
size = 100
pendown()

rt(30)

for i in range(3):
    rt(150)
    fd(6*size)
    rt(30)
    fd(12*size)

penup()

for x in range(-25, 35):
    for y in range(-25, 35):
        setpos(x * size, y * size)
        dot(6, "blue")

input()
done()