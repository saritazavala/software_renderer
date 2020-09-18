#Universidad del Valle de Guatemala
#Sara Zavala 18893
#RT1-Esferas
#Graficas

from structFunctions import *
from Object import *
from mathFunctions import *
import numpy

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
      self.createViewMatrix()
      self.createProjectionMatrix()
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
      self.render_function()

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



    # Defines the area where will be able to draw
    def glViewPort(self, x_position, y_position, ViewPort_width, ViewPort_height):
      self.x_position = x_position
      self.y_position = y_position
      self.ViewPort_height = ViewPort_height
      self.ViewPort_width = ViewPort_width
      self.viewportMatrix = numpy.matrix([[ViewPort_width / 2, 0, 0, x_position + ViewPort_width / 2],
                                    [0, ViewPort_height / 2, 0, y_position + ViewPort_height / 2],
                                    [0, 0, 0.5, 0.5],
                                    [0, 0, 0, 1]])


    def glVertex_coord(self, x, y, color = None):
      if x < self.x_position or x >= self.x_position + self.ViewPort_width or y < self.y_position or y >= self.y_position + self.ViewPort_height:
        return

      if x >= self.width or x < 0 or y >= self.height or y < 0:
        return

      try:
        self.framebuffer[y][x] = color or self.curr_color
      except:
        pass



    def inverseMatrix(self):
      pass


    def createViewMatrix(self, camPosition = V3(0,0,0), camRotation = V3(0,0,0)):
        camMatrix = self.createObjectMatrix( translate = camPosition, rotate = camRotation)
        #self.viewMatrix=self.inverseMatrix(camMatrix)






    # Compuse el vertex por que me daba error el range
    def glVertex(self, x, y):
      x_temp = round((x + 1) * (self.ViewPort_width / 2) + self.x_position)
      y_temp = round((y + 1) * (self.ViewPort_height / 2) + self.y_position)
      self.glpoint(round(x_temp), round(y_temp))


    # This function creates a Line using the glpoint() function
    def glLine(self, x1, y1, x2, y2):
      dy = abs(y2 - y1)
      dx = abs(x2 - x1)
      steep = dy > dx

      if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dy = abs(y2 - y1)
        dx = abs(x2 - x1)

      if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

      offset = 0
      threshold = 1
      y = y1
      for x in range(x1, x2):
        if steep:
          self.glpoint(y, x)
        else:
          self.glpoint(x, y)

        offset += dy * 2

        if offset >= threshold:
          y += 1 if y1 < y2 else -1
          threshold += 2 * dx



      #Functions for creating triangules utilizando glpoint()

    def triangle_bc(self, A, B, C, texcoords=(), normals=(), _color=None):
      # bounding box
      minX = round(min(A.x, B.x, C.x))
      minY = round(min(A.y, B.y, C.y))
      maxX = round(max(A.x, B.x, C.x))
      maxY = round(max(A.y, B.y, C.y))

      for x in range(minX, maxX + 1):
        for y in range(minY, maxY + 1):
          if x >= self.width or x < 0 or y >= self.height or y < 0:
            continue

          u, v, w = barycentric(A, B, C, V2(x, y))

          if u >= 0 and v >= 0 and w >= 0:

            z = A.z * u + B.z * v + C.z * w
            if z < self.zbuffer[y][x] and z <= 1 and z >= -1:

              if self.active_shader:

                r, g, b = self.active_shader(self, verts=(A, B, C), baryCoords=(u, v, w), texCoords=texcoords, normals=normals,color=_color or self.change_color)
              else:
                b, g, r = _color or self.change_color

              self.glVertex_coord(x, y, color(r, g, b))
              self.zbuffer[y][x] = z

    def loadModel(self, filename, translate = V3(0,0,0), scale = V3(1,1,1), rotate=V3(0,0,0)):
        model = Obj(filename)

        modelMatrix = self.createObjectMatrix(translate, scale, rotate)

        rotationMatrix = self.createRotationMatrix(rotate)

        for face in model.faces:

            vertCount = len(face)

            v0 = model.vertices[ face[0][0] - 1 ]
            v1 = model.vertices[ face[1][0] - 1 ]
            v2 = model.vertices[ face[2][0] - 1 ]
            if vertCount > 3:
                v3 = model.vertices[ face[3][0] - 1 ]

            v0 = self.transform(v0, modelMatrix)
            v1 = self.transform(v1, modelMatrix)
            v2 = self.transform(v2, modelMatrix)
            if vertCount > 3:
                v3 = self.transform(v3, modelMatrix)

            if self.active_texture:
                vt0 = model.texcoords[face[0][1] - 1]
                vt1 = model.texcoords[face[1][1] - 1]
                vt2 = model.texcoords[face[2][1] - 1]
                vt0 = V2(vt0[0], vt0[1])
                vt1 = V2(vt1[0], vt1[1])
                vt2 = V2(vt2[0], vt2[1])
                if vertCount > 3:
                    vt3 = model.texcoords[face[3][1] - 1]
                    vt3 = V2(vt3[0], vt3[1])
            else:
                vt0 = V2(0,0)
                vt1 = V2(0,0)
                vt2 = V2(0,0)
                vt3 = V2(0,0)

            vn0 = model.normals[face[0][2] - 1]
            vn1 = model.normals[face[1][2] - 1]
            vn2 = model.normals[face[2][2] - 1]

            vn0 = self.dirTransform(vn0, rotationMatrix)
            vn1 = self.dirTransform(vn1, rotationMatrix)
            vn2 = self.dirTransform(vn2, rotationMatrix)
            if vertCount > 3:
                vn3 = model.normals[face[3][2] - 1]
                vn3 = self.dirTransform(vn3, rotationMatrix)


            self.triangle_bc(v0,v1,v2, texcoords = (vt0,vt1,vt2), normals = (vn0,vn1,vn2))
            if vertCount > 3:
                self.triangle_bc(v0,v2,v3, texcoords = (vt0,vt2,vt3), normals = (vn0,vn2,vn3))

    def createProjectionMatrix(self, n = 0.1, f = 1000, fov = 60):
      t = numpy.tan((fov * math.pi / 180) / 2) * n
      r = t * self.ViewPort_width / self.ViewPort_height

      self.projectionMatrix =numpy.matrix([[n / r, 0, 0, 0],
                                           [0, n / t, 0, 0],
                                           [0, 0, -(f+n)/(f-n), -(2*f*n)/(f-n)],
                                           [0, 0, -1, 0]])


    def triangle(self, A, B, C):
      xmax, ymax, xmin, ymin = bbox(A, B, C)

      for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
          P = V2(x, y)
          w, v, u = barycentric(A, B, C, P)
          if w < 0 or v < 0 or u < 0:
            continue
          z = A.z * w + B.z * u + C.z * v
          try:
            if z > self.zbuffer[x][y]:
              self.glpoint(x, y)
              self.zbuffer[x][y] = z
          except:
            pass


    def createRotationMatrix(self, rotate=V3(0,0,0)):
      pitch = numpy.deg2rad(rotate.x)
      yaw = numpy.deg2rad(rotate.y)
      roll = numpy.deg2rad(rotate.z)

      rotationX = numpy.matrix([[1, 0, 0, 0],
                                [0, numpy.cos(pitch), -numpy.sin(pitch), 0],
                                [0, numpy.sin(pitch), numpy.cos(pitch), 0],
                                [0, 0, 0, 1]])

      rotationY = numpy.matrix([[numpy.cos(yaw), 0, numpy.sin(yaw), 0],
                            [0, 1, 0, 0],
                            [-numpy.sin(yaw), 0, numpy.cos(yaw), 0],
                            [0, 0, 0, 1]])

      rotationZ = numpy.matrix([[numpy.cos(roll),-numpy.sin(roll), 0, 0],
                            [numpy.sin(roll), numpy.cos(roll), 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])

      return rotationX * rotationY * rotationZ



    def createObjectMatrix(self, translate = V3(0,0,0), scale = V3(1,1,1), rotate=V3(0,0,0)):
      translateMatrix = numpy.matrix([[1, 0, 0, translate.x],
                                  [0, 1, 0, translate.y],
                                  [0, 0, 1, translate.z],
                                  [0, 0, 0, 1]])

      scaleMatrix = numpy.matrix([[scale.x, 0, 0, 0],
                              [0, scale.y, 0, 0],
                              [0, 0, scale.z, 0],
                              [0, 0, 0, 1]])

      rotationMatrix = self.createRotationMatrix(rotate)

      return translateMatrix * rotationMatrix * scaleMatrix

    def transform(self, vertex, vMatrix):
      augVertex = V4(vertex[0], vertex[1], vertex[2], 1)
      transVertex = self.viewportMatrix @ self.projectionMatrix @ self.viewMatrix @ vMatrix @ augVertex
      transVertex = transVertex.tolist()[0]
      transVertex = V3(transVertex[0] / transVertex[3],
                       transVertex[1] / transVertex[3],
                       transVertex[2] / transVertex[3])
      return transVertex



    def dirTransform(self, vertex, vMatrix):
      augVertex = V4(vertex[0], vertex[1], vertex[2], 0)
      transVertex = vMatrix @ augVertex
      transVertex = transVertex.tolist()[0]
      transVertex = V3(transVertex[0],
                       transVertex[1],
                       transVertex[2])

      return transVertex

    def zeros_matrix(rows, cols):
        """
        Creates a matrix filled with zeros.
            :param rows: the number of rows the matrix should have
            :param cols: the number of columns the matrix should have
            :return: list of lists that form the matrix
        """
        M = []
        while len(M) < rows:
            M.append([])
            while len(M[-1]) < cols:
                M[-1].append(0.0)

        return M

















