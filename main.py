import math

def Mo(shear, length, width, slip):
  shear *= 1000000000
  length *= 1000
  width *= 1000
  return shear * length * width * slip

Mo = Mo(40, 500, 200, 10)

Mw = (math.log10(Mo)-9.1) / 1.5
print(Mw)
