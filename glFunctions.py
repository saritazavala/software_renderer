#Universidad del Valle de Guatemala
#Sara Zavala 18893
#RT1-Esferas
#Graficas


#Referencias para ciertas funciones
#Estas fueron adaptadas para este proyecto
#https://github.com/ThomIves/BasicLinearAlgebraToolsPurePy/blob/master/LinearAlgebraPurePython.py


from structFunctions import *
from Object import Obj
from collections import namedtuple
from math import *
from mathFunctions import *




class Render(object):
    # Estado incial de colores
    def __init__(self, width, height, filename):
        self.framebuffer = []
        self.filename = filename
        self.change_color = color(1, 1, 1)
        self.change_color2 = color(0, 0, 0)
        self.glCreateWindow(width, height)
        self.light = V3(0, 0, 1)
        self.activeT = None
        self.actSha = None
        self.createViewMatrix()
        self.createProjectionMatrix()

    # Matriz de vista
    def createViewMatrix(self, camPosition=V3(0, 0, 0), camRotation=V3(0, 0, 0)):
        camMatrix = self.createObjectMatrix(translate=camPosition, rotate=camRotation)
        self.viewMatrix = getMatrixInverse(camMatrix)

    # Funcion para apuntar al objeto
    def lookAt(self, eye, camPosition=V3(0, 0, 0)):
        forward = sub(camPosition, eye)
        fnormal = norm(forward)
        forward[0] /= fnormal
        forward[1] /= fnormal
        forward[2] /= fnormal

        right = cross(V3(0, 1, 0), forward)
        rnormal = norm(right)
        right[0] /= rnormal
        right[1] /= rnormal
        right[2] /= rnormal

        up = cross(forward, right)
        unormal = norm(up)
        up[0] /= unormal
        up[1] /= unormal
        up[2] /= unormal

        camMatrix = [[right[0], up[0], forward[0], camPosition.x],
                     [right[1], up[1], forward[1], camPosition.y],
                     [right[2], up[2], forward[2], camPosition.z],
                     [0, 0, 0, 1]]
        self.viewMatrix = getMatrixInverse(camMatrix)
        # print(getMatrixInverse2(camMatrix))
        # print('-----------------------------------')
        # for x in getMatrixInverse(camMatrix):
        #     print(x)

    # Matriz de projecion
    def createProjectionMatrix(self, n=0.1, f=1000, fov=60):

        t = tan((fov * math.pi / 180) / 2) * n

        r = t * self.vpWidth / self.vpHeight

        self.projectionMatrix = [[n / r, 0, 0, 0],
                                 [0, n / t, 0, 0],
                                 [0, 0, -(f + n) / (f - n), -(2 * f * n) / (f - n)],
                                 [0, 0, -1, 0]]

    # Inicializador del tamaño del FrameBuffer
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()
        self.glViewport(0, 0, width, height)

    # Llenado del mapa de bits con un solo color
    def glClear(self):
        self.framebuffer = [[self.change_color2 for x in range(self.width)] for y in range(self.height)]
        self.zbuffer = [[float('inf') for x in range(self.width)] for y in range(self.height)]

    # Cambio de color de un pixel dado su posicion
    def glpoint(self, x, y, color=None):
        self.framebuffer[y][x] = color or self.change_color

    def glClearColor(self, r, g, b):
        if 0 <= r <= 1 and 0 <= g <= 1 and 0 <= b <= 1:
            self.change_color2 = color(r, g, b)
            self.glClear()

    # Definicion del area donde sera posible dibujar
    def glViewport(self, x, y, width, height):
        self.vpWidth = width
        self.vpHeight = height
        self.vpX = x
        self.vpY = y

        self.viewportMatrix = [[width / 2, 0, 0, x + width / 2],
                               [0, height / 2, 0, y + height / 2],
                               [0, 0, 0.5, 0.5],
                               [0, 0, 0, 1]]

    # Cambio de color de un punto en pantalla, con referencia al ViewPort
    def glVertex(self, x, y):
        x = int((x + 1) * (self.vpWidth / 2) + self.vpX)
        y = int((y + 1) * (self.vpHeight / 2) + self.vpY)
        if x >= self.width or x < 0 or y >= self.height or y < 0:
            return
        try:
            self.framebuffer[round(y)][round(x)] = color or self.change_color
        except:
            pass

    # Codigo basado en codigo visto en clase
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

    def header(self):
        doc = open(self.filename, 'bw')
        doc.write(char('B'))
        doc.write(char('M'))
        doc.write(dword(54 + self.width * self.height * 3))
        doc.write(dword(0))
        doc.write(dword(54))
        self.info(doc)

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
        for x in range(self.height):
            for y in range(self.width):
                doc.write(self.framebuffer[x][y])
        doc.close()

    def glFinish(self):
        self.header()

    # Transfomracion por matriz de translacion
    def transform(self, vertex, vMatrix):
        augVertex = V4(vertex[0], vertex[1], vertex[2], 1)
        augVertex = [augVertex.x, augVertex.y, augVertex.z, augVertex.w]

        transVertex = mul(
            mul(mul(self.viewportMatrix, self.projectionMatrix), self.viewMatrix), vMatrix)
        transVertex = vec_matrx(transVertex, augVertex)

        transVertex = V3(transVertex[0] / transVertex[3],
                         transVertex[1] / transVertex[3],
                         transVertex[2] / transVertex[3])
        return transVertex

    def dirTransform(self, vertex, vMatrix):
        augVertex = V4(vertex[0], vertex[1], vertex[2], 0)
        augVertex = [augVertex.x, augVertex.y, augVertex.z, augVertex.w]

        transVertex = vec_matrx(vMatrix, augVertex)

        transVertex = V3(transVertex[0],
                         transVertex[1],
                         transVertex[2])

        return transVertex

    # Matriz del objeto
    def createObjectMatrix(self, translate=V3(0, 0, 0), scale=V3(1, 1, 1), rotate=V3(0, 0, 0)):

        translateMatrix = [[1, 0, 0, translate.x],
                           [0, 1, 0, translate.y],
                           [0, 0, 1, translate.z],
                           [0, 0, 0, 1]]

        scaleMatrix = [[scale.x, 0, 0, 0],
                       [0, scale.y, 0, 0],
                       [0, 0, scale.z, 0],
                       [0, 0, 0, 1]]
        rotationMatrix = self.createRotationMatrix(rotate)

        return mul(translateMatrix, mul(rotationMatrix, scaleMatrix))

    # Matriz de rotacion
    def createRotationMatrix(self, rotate=V3(0, 0, 0)):

        pitch = convert(rotate.x)
        yaw = convert(rotate.y)
        roll = convert(rotate.z)

        rotationX = [[1, 0, 0, 0],
                     [0, cos(pitch), -sin(pitch), 0],
                     [0, sin(pitch), cos(pitch), 0],
                     [0, 0, 0, 1]]

        rotationY = [[cos(yaw), 0, sin(yaw), 0],
                     [0, 1, 0, 0],
                     [-sin(yaw), 0, cos(yaw), 0],
                     [0, 0, 0, 1]]

        rotationZ = [[cos(roll), -sin(roll), 0, 0],
                     [sin(roll), cos(roll), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]]

        return mul(rotationX, mul(rotationY, rotationZ))

    # Carga y dibujo de modelo .obj
    def loadModel(self, filename, translate=V3(0, 0, 0), scale=V3(1, 1, 1), rotate=V3(0, 0, 0)):
        model = Obj(filename)

        modelMatrix = self.createObjectMatrix(translate, scale, rotate)

        rotationMatrix = self.createRotationMatrix(rotate)

        for face in model.faces:

            vertCount = len(face)

            v0 = model.vertex[face[0][0] - 1]
            v1 = model.vertex[face[1][0] - 1]
            v2 = model.vertex[face[2][0] - 1]
            if vertCount > 3:
                v3 = model.vertex[face[3][0] - 1]

            v0 = self.transform(v0, modelMatrix)
            v1 = self.transform(v1, modelMatrix)
            v2 = self.transform(v2, modelMatrix)
            if vertCount > 3:
                v3 = self.transform(v3, modelMatrix)

            if self.activeT:
                vt0 = model.tvertex[face[0][1] - 1]
                vt1 = model.tvertex[face[1][1] - 1]
                vt2 = model.tvertex[face[2][1] - 1]
                vt0 = V2(vt0[0], vt0[1])
                vt1 = V2(vt1[0], vt1[1])
                vt2 = V2(vt2[0], vt2[1])
                if vertCount > 3:
                    vt3 = model.tvertex[face[3][1] - 1]
                    vt3 = V2(vt3[0], vt3[1])
            else:
                vt0 = V2(0, 0)
                vt1 = V2(0, 0)
                vt2 = V2(0, 0)
                vt3 = V2(0, 0)

            vn0 = model.normals[face[0][2] - 1]
            vn1 = model.normals[face[1][2] - 1]
            vn2 = model.normals[face[2][2] - 1]

            vn0 = self.dirTransform(vn0, rotationMatrix)
            vn1 = self.dirTransform(vn1, rotationMatrix)
            vn2 = self.dirTransform(vn2, rotationMatrix)
            if vertCount > 3:
                vn3 = model.normals[face[3][2] - 1]
                vn3 = self.dirTransform(vn3, rotationMatrix)

            self.triangle(v0, v1, v2, texcoords=(vt0, vt1, vt2), normals=(vn0, vn1, vn2))
            if vertCount > 3:  # asumamos que 4, un cuadrado
                self.triangle(v0, v2, v3, texcoords=(vt0, vt2, vt3), normals=(vn0, vn2, vn3))

    # Triangulos, profundidades, y coordenadas Barycentricas
    def triangle(self, A, B, C, texcoords=(), normals=(), _color=None):
        # bounding box
        minX = int(round(min(A.x, B.x, C.x)))
        minY = int(round(min(A.y, B.y, C.y)))
        maxX = int(round(max(A.x, B.x, C.x)))
        maxY = int(round(max(A.y, B.y, C.y)))

        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                if x >= self.width or x < 0 or y >= self.height or y < 0:
                    continue

                u, v, w = barycentric(A, B, C, V2(x, y))

                if u >= 0 and v >= 0 and w >= 0:

                    z = A.z * u + B.z * v + C.z * w
                    if z < self.zbuffer[y][x] and z <= 1 and z >= -1:
                        if self.actSha:
                            r, g, b = self.actSha(self, vert=(A, B, B), barycentric=(u, v, w), texCoords=texcoords,
                                                  normals=normals, color=_color or self.change_color)
                        else:
                            b, g, r = _color or self.change_color

                        try:
                            self.glpoint(x, y, color(r, g, b))
                        except:
                            self.glpoint(x, y, color2(r, g, b))

                        self.zbuffer[y][x] = z

