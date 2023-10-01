from turtle import *
import colorsys

bgcolor('black')
width(2)
h = 0.0

for i in range(180):
    speed(100)
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    forward(i * 3)
    right(121)
    h += 0.005
done()
