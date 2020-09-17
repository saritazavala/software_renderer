#Universidad del Valle de Guatemala
#Sara Zavala 18893
#RT1-Esferas
#Graficas

from structFunctions import *
from Object import *
from mathFunctions import *


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

      # New function for loading my .obj
    def load_model(self, filename, translate=(0, 0, 0), scale=(1, 1, 1)):
      model = Obj(filename)

      light = V3(0, 0, 1)

      for face in model.faces:
        vcount = len(face)

        if vcount == 3:
          f1 = face[0][0] - 1
          f2 = face[1][0] - 1
          f3 = face[2][0] - 1

          v1 = V3(model.vertex[f1][0], model.vertex[f1][1], model.vertex[f1][2])
          v2 = V3(model.vertex[f2][0], model.vertex[f2][1], model.vertex[f2][2])
          v3 = V3(model.vertex[f3][0], model.vertex[f3][1], model.vertex[f3][2])

          x1 = round((v1.x * scale[0]) + translate[0])
          y1 = round((v1.y * scale[1]) + translate[1])
          z1 = round((v1.z * scale[2]) + translate[2])

          x2 = round((v2.x * scale[0]) + translate[0])
          y2 = round((v2.y * scale[1]) + translate[1])
          z2 = round((v2.z * scale[2]) + translate[2])

          x3 = round((v3.x * scale[0]) + translate[0])
          y3 = round((v3.y * scale[1]) + translate[1])
          z3 = round((v3.z * scale[2]) + translate[2])

          A = V3(x1, y1, z1)
          B = V3(x2, y2, z2)
          C = V3(x3, y3, z3)

          normal = norm(cross(sub(B, A), sub(C, A)))
          intensity = dot(normal, light)
          grey = round(255 * intensity)

          if grey < 0:
            continue

          self.change_color = color2(grey, grey, grey)

          self.triangle(A, B, C)

        else:
          f1 = face[0][0] - 1
          f2 = face[1][0] - 1
          f3 = face[2][0] - 1
          f4 = face[3][0] - 1

          v1 = V3(model.vertex[f1][0], model.vertex[f1][1], model.vertex[f1][2])
          v2 = V3(model.vertex[f2][0], model.vertex[f2][1], model.vertex[f2][2])
          v3 = V3(model.vertex[f3][0], model.vertex[f3][1], model.vertex[f3][2])
          v4 = V3(model.vertex[f4][0], model.vertex[f4][1], model.vertex[f4][2])

          x1 = round((v1.x * scale[0]) + translate[0])
          y1 = round((v1.y * scale[1]) + translate[1])
          z1 = round((v1.z * scale[2]) + translate[2])

          x2 = round((v2.x * scale[0]) + translate[0])
          y2 = round((v2.y * scale[1]) + translate[1])
          z2 = round((v2.z * scale[2]) + translate[2])

          x3 = round((v3.x * scale[0]) + translate[0])
          y3 = round((v3.y * scale[1]) + translate[1])
          z3 = round((v3.z * scale[2]) + translate[2])

          x4 = round((v4.x * scale[0]) + translate[0])
          y4 = round((v4.y * scale[1]) + translate[1])
          z4 = round((v4.z * scale[2]) + translate[2])

          A = V3(x1, y1, z1)
          B = V3(x2, y2, z2)
          C = V3(x3, y3, z3)
          D = V3(x4, y4, z4)

          normal = norm(cross(sub(B, A), sub(C, A)))
          intensity = dot(normal, light)
          grey = round(255 * intensity)
          if grey < 0:
            continue

          self.change_color = color2(grey, grey, grey)

          self.triangle(A, B, C)

          self.triangle(A, D, C)




