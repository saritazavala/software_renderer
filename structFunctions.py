#Universidad del Valle de Guatemala
#Sara Zavala 18893
#RT1-Esferas
#Graficas

import struct

def char(c):
    return struct.pack('=c', c.encode('ascii'))

# 2 bytes
def word(c):
    return struct.pack('=h', c)

# 4 bytes
def dword(c):
    return struct.pack('=l', c)

def color(red, green, blue):
     return bytes([round(blue * 255), round(green * 255), round(red * 255)])

def color2(r, g, b):
  return bytes([b, g, r])