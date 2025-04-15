from turtle import *

tracer(0)
left(90)
screensize(5000, 5000)
size = 18

pendown()

for i in range(4):
    fd(16*size)
    lt(90)
    fd(20*size)
    lt(90)

penup()

fd(4*size)
lt(90)
fd(8*size)
rt(180)

pendown()

for i in range(3):
    fd(35*size)
    lt(90)
    fd(6*size)
    lt(90)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*size, y*size)
        dot(4, 'blue')

input()
done()

'''
Answer: 130
'''