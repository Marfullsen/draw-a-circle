#!/usr/bin/env python
#-*- coding: utf-8 -*-

import draw_a_circle

def test_circle():
    draw_a_circle.draw_circle(50,50,5,(255,100,255))
    draw_a_circle.img.show()

def test_circles():
    draw_a_circle.draw_circle(50,50,5,(255,100,255))
    draw_a_circle.draw_circle(150,150,5,(0,100,255))
    draw_a_circle.draw_circle(50,0,5,(255,0,50))
    draw_a_circle.draw_circle(0,50,5,(92,231,193))
    draw_a_circle.img.show()

if __name__ == "__main__":
      test_circle()
      test_circles()
