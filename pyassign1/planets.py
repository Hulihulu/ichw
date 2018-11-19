#!/usr/bin/env python3

"""planets.py: Simulating Simulating the revolution of 
               the six major planets in the solar system.

__author__ = "Huruihua"
__pkuid__  = "1800011843"
__email__  = "1800011843@pku.edu.cn"
"""

import math

import turtle
wn = turtle.Screen()
wn.bgcolor("black")

"""Define pen one by one
"""
pen=[]
pen_count = 8
for i in range(pen_count):
    pen.append(turtle.Turtle()) 
    
"""draw the Sun 
"""
pen[1].shape("circle")
pen[1].shapesize(3)
pen[1].color("red")
pen[1].penup()

"""draw the Mercury
"""
pen[2].goto(80,0)
pen[2].color("bisque")
pen[2].speed(2)
pen[2].shape("circle")

"""draw the Venus
"""
pen[3].goto(110,0)
pen[3].color("goldenrod")
pen[3].speed(3)
pen[3].shape("circle")
    
"""draw the Earth
"""
pen[4].goto(150,0)
pen[4].color("lightseagreen")
pen[4].speed(4)
pen[4].shape("circle")

"""draw the Mars
"""
pen[5].goto(190,0)
pen[5].color("firebrick")
pen[5].speed(5)
pen[5].shape("circle")

"""draw the Saturn
"""
pen[6].goto(260,0)
pen[6].color("peru")
pen[6].shape("circle")
pen[6].speed(6)
pen[6].shapesize(2)

"""draw the Jupiter
"""
pen[7].goto(350,0)
pen[7].color("chocolate")
pen[7].shape("circle")
pen[7].speed(7)
pen[7].shapesize(2.5)

def main():
    """main module
    """   
    for x in range(1000):
        pen[2].goto(80*math.cos(0.1*x),75*math.sin(0.1*x))
        pen[3].goto(110*math.cos(0.08*x),100*math.sin(0.08*x))
        pen[4].goto(150*math.cos(0.06*x),130*math.sin(0.06*x))
        pen[5].goto(190*math.cos(0.03*x),160*math.sin(0.03*x))
        pen[6].goto(260*math.cos(0.01*x),210*math.sin(0.01*x))
        pen[7].goto(350*math.cos(0.005*x),280*math.sin(0.005*x))

if __name__ == '__main__':
    main()
