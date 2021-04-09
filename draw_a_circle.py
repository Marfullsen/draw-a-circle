#!/usr/bin/env python
#-*- coding: utf-8 -*-
# transcoded from Java to Python3
# Source: https://stackoverflow.com/a/58629898

from PIL import Image
from math import acos, cos, sin

img = Image.new('RGB', (200, 200))

def draw_circle(x:int, y:int, r:int, color:tuple) -> 'new file: ./circle.png':
      PI = 3.1415926535;
      x1, y1 = (0.0, 0.0)

      # calculates the minimun angle between two pixels in a diagonal.
      # you can multiply minAngle by a security factor like 0.9 just to be sure you wont have empty pixels in the circle
      minAngle = acos(1 - 1/r)

      for angle in range(0, 360):
            angle += minAngle
            x1 = r * cos(angle)
            y1 = r * sin(angle)
            img.putpixel( (int(x+x1), int(y+y1)), color)

if __name__ == "__main__":
      color_white = (255,255,255)
      for radius in range(1, 100, 1):
            draw_circle(100, 100, radius, color_white)
            
      color_red = (255,0,0)
      draw_circle(100, 100, 50, color_red)

      img.save('circle-1.png')
      img.show()
