#Universidad del Valle de Guatemala
#Sara Zavala 18893
#RT1-Esferas
#Graficas

import struct
from structFunctions import *

def try_int(s, base=10, val=None):
    try:
        return int(s, base)
    except ValueError:
        return val

class Obj(object):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.lines=file.read().splitlines()
        #clasificaciones de datos dentro de archivo OBJ
        self.vertex=[]
        self.normals=[]
        self.tvertex=[]
        self.faces=[]
        self.read()

    def read(self):
        for line in self.lines:
            if line:
                try:
                    prefix, value = line.split(' ', 1)
                except:
                    continue
                if prefix == 'v': # vertices
                    self.vertex.append(list(map(float,value.split(' '))))
                elif prefix == 'vn': #normales
                    self.normals.append(list(map(float,value.split(' '))))
                elif prefix == 'vt': #tvertex
                    self.tvertex.append(list(map(float,value.split(' '))))
                elif prefix == 'f': #faces XX/YY/ZZ
                    self.faces.append([list(map(int,vert.split('/'))) for vert in value.split(' ')])


class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        image = open(self.path, 'rb')
        image.seek(10)
        headerSize = struct.unpack('=l', image.read(4))[0]

        image.seek(14 + 4)
        self.width = struct.unpack('=l', image.read(4))[0]
        self.height = struct.unpack('=l', image.read(4))[0]
        image.seek(headerSize)

        self.pixels = []

        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(image.read(1)) / 255
                g = ord(image.read(1)) / 255
                r = ord(image.read(1)) / 255
                self.pixels[y].append(color(r, g, b))

        image.close()

    def getColor(self, tx, ty):
        if tx >= 0 and tx <= 1 and ty >= 0 and ty <= 1:
            x = int(tx * self.width)
            y = int(ty * self.height)

            return self.pixels[y][x]
        else:
            return color(0,0,0)