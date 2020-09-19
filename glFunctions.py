#Universidad del Valle de Guatemala
#Sara Zavala 18893
#RT1-Esferas
#Graficas

from structFunctions import *
from Object import *
from mathFunctions import *
import math
import numpy as np

#Referencias para ciertas funciones
#Estas fueron adaptadas para este proyecto
#https://github.com/ThomIves/BasicLinearAlgebraToolsPurePy/blob/master/LinearAlgebraPurePython.py


class Render(object):

    # Initial values -------------------------------
    def __init__(self, filename):
      self.width = 0
      self.height = 0
      self.framebuffer = []
      self.change_color = color(0, 0, 0)
      self.filename = filename
      self.x_position = 0
      self.y_position = 0
      self.ViewPort_height = 0
      self.ViewPort_width = 0
      self.light = V3(0, 0, 1)
      self.active_texture = None
      self.active_texture2 = None
      # self.createViewMatrix()
      # self.createProjectionMatrix()
      self.glClear()

# Write a BMP file ---------------------------------

    # File Header ----------------------------------
    def header(self):
      doc = open(self.filename, 'bw')
      doc.write(char('B'))
      doc.write(char('M'))
      doc.write(dword(54 + self.width * self.height * 3))
      doc.write(dword(0))
      doc.write(dword(54))
      self.info(doc)

    # Info header ----------------------------------
    def info(self, doc):
      doc.write(dword(40))
      doc.write(dword(self.width))
      doc.write(dword(self.height))
      doc.write(word(1))
      doc.write(word(24))
      doc.write(dword(0))
      doc.write(dword(self.width * self.height * 3))
      doc.write(dword(0))
      doc.write(dword(0))
      doc.write(dword(0))
      doc.write(dword(0))

      # Image ----------------------------------
      for x in range(self.height):
        for y in range(self.width):
          doc.write(self.framebuffer[x][y])
      doc.close()

    # Writes all the doc
    def glFinish(self):
      #self.render_function()
      self.header()

    # Cleans a full image with the color defined in "change_color"
    def glClear(self):
      self.framebuffer = [[self.change_color for x in range(self.width)] for y in range(self.height)]
      self.zbuffer = [[-float('inf') for x in range(self.width)] for y in range(self.height)]

    # Draws a point according ot frameBuffer
    def glpoint(self, x, y):
      self.framebuffer[y][x] = self.change_color

    # Creates a window
    def glCreateWindow(self, width, height):
      self.width = width
      self.height = height
      self.glViewPort(0, 0, width, height)



    # Defines the area where will be able to draw
    def glViewPort(self, x_position, y_position, ViewPort_width, ViewPort_height):
      self.x_position = x_position
      self.y_position = y_position
      self.ViewPort_height = ViewPort_height
      self.ViewPort_width = ViewPort_width


    # ---------------------------------------------------------------------------------------



    # def transposeMatrix(self, m):
    #     a=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    #     for i in range(0, 4):
    #         for j in range(0, 4):
    #             a[j][i]=m[i][j]
    #     return a
    # def getMatrixMinor(self,m,i,j):
    #     return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
    #
    # def getMatrixDeternminant(self, m):
    #     #base case for 2x2 matrix
    #     if len(m) == 2:
    #         return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    #
    #     determinant = 0
    #     for c in range(len(m)):
    #         determinant += ((-1)**c)*m[0][c]*self.getMatrixDeternminant(self.getMatrixMinor(m,0,c))
    #     return determinant
    #
    # def getMatrixInverse(self, m):
    #     determinant = self.getMatrixDeternminant(m)
    #     #special case for 2x2 matrix:
    #     if len(m) == 2:
    #         return [[m[1][1]/determinant, -1*m[0][1]/determinant],
    #                 [-1*m[1][0]/determinant, m[0][0]/determinant]]
    #
    #     #find matrix of cofactors
    #     cofactors = []
    #     for r in range(len(m)):
    #         cofactorRow = []
    #         for c in range(len(m)):
    #             minor = self.getMatrixMinor(m,r,c)
    #             cofactorRow.append(((-1)**(r+c)) * self.getMatrixDeternminant(minor))
    #         cofactors.append(cofactorRow)
    #     cofactors = self.transposeMatrix(cofactors)
    #     for r in range(len(cofactors)):
    #         for c in range(len(cofactors)):
    #             cofactors[r][c] = cofactors[r][c]/determinant
    #     return cofactors







    def createProjectionMatrix(self, n = 0.1, f = 1000, fov = 60):

        t = math.tan((fov * math.pi / 180) / 2) * n
        r = t * self.ViewPort_width / self.ViewPort_height









    # def transform(self, vertex, vMatrix):  # sustitucion del transform antiguo
    #
    #     pVertex = [[vertex[0]], [vertex[1]], [vertex[2]], [1]]
    #     a = self.multMaster(self.viewportMatrix, self.projectionMatrix)
    #     b = self.multMaster(a, self.viewMatrix)
    #     c = self.multMaster(b, vMatrix)
    #     pVertex = self.multMaster(c, pVertex)
    #
    #     pVertex = (pVertex[0][0] / pVertex[3][0],
    #                pVertex[1][0] / pVertex[3][0],
    #                pVertex[2][0] / pVertex[3][0])
    #
    #     print(pVertex)
    #
    #     return pVertex



    # def createObjectMatrix(self, translate = (0,0,0), scale = (1,1,1), rotate=(0,0,0)):
    #     #matriz de traslacion
    #     translateMatrix = [[1, 0, 0, translate[0]],
    #                               [0, 1, 0, translate[1]],
    #                               [0, 0, 1, translate[2]],
    #                               [0, 0, 0, 1]]
    #
    #     #matriz de la escala
    #     scaleMatrix = [[scale[0], 0, 0, 0],
    #                           [0, scale[1], 0, 0],
    #                           [0, 0, scale[2], 0],
    #                           [0, 0, 0, 1]]
    #
    #     #matriz de rotacion
    #     rotationMatrix = self.createRotationMatrix(rotate)
    #     #multiplicacion de matrices sin numpy
    #     a=self.multiplicacion(translateMatrix, rotationMatrix, 4,4,4,4)
    #     b=self.multiplicacion(a, scaleMatrix, 4,4,4,4)
    #
    #     return b


    # def createRotationMatrix(self, rotate=(0,0,0)):
    #
    #     pitch = np.deg2rad(rotate[0])
    #     yaw = np.deg2rad(rotate[1])
    #     roll = np.deg2rad(rotate[2])
    #
    #     #matriz de rotacion en x
    #     rotationX = [[1, 0, 0, 0],
    #                         [0, math.cos(pitch),-math.sin(pitch), 0],
    #                         [0, math.sin(pitch), math.cos(pitch), 0],
    #                         [0, 0, 0, 1]]
    #     #matriz de rotacion en y
    #     rotationY = [[math.cos(yaw), 0, math.sin(yaw), 0],
    #                         [0, 1, 0, 0],
    #                         [-math.sin(yaw), 0, math.cos(yaw), 0],
    #                         [0, 0, 0, 1]]
    #     #matriz de rotacion en z
    #     rotationZ = [[math.cos(roll),-math.sin(roll), 0, 0],
    #                         [math.sin(roll), math.cos(roll), 0, 0],
    #                         [0, 0, 1, 0],
    #                         [0, 0, 0, 1]]
    #
    #     a=multiplicacion(rotationX, rotationY, 4,4,4,4)
    #     b=multiplicacion(a, rotationZ, 4,4,4,4)
    #     return (b)










