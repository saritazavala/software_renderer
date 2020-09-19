#Universidad del Valle de Guatemala
#Sara Zavala 18893
#RT1-Esferas
#Graficas

from collections import namedtuple
import math


V2 = namedtuple('Vertex2', ['x', 'y'])
V3 = namedtuple('Vertex3', ['x', 'y', 'z'])
V4 = namedtuple('Point4', ['x', 'y', 'z','w'])

def sum(v0, v1):
  return V3(v0.x + v1.x, v0.y + v1.y, v0.z + v1.z)

def sub(v0, v1):
  return V3(v0.x - v1.x, v0.y - v1.y, v0.z - v1.z)

def mul(v0, k):
  return V3(v0.x * k, v0.y * k, v0.z *k)

def dot(v0, v1):
  return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z

def cross(v1, v2):
  return V3(
    v1.y * v2.z - v1.z * v2.y,
    v1.z * v2.x - v1.x * v2.z,
    v1.x * v2.y - v1.y * v2.x,
  )

def length(v0):
  return (v0.x**2 + v0.y**2 + v0.z**2)**0.5


def norm(v0):
  v0length = length(v0)

  if not v0length:
    return V3(0, 0, 0)

  return V3(v0.x/v0length, v0.y/v0length, v0.z/v0length)

def bbox(*vertices):

  xs = [ vertex.x for vertex in vertices ]
  ys = [ vertex.y for vertex in vertices ]

  return (max(xs), max(ys), min(xs), min(ys))

def barycentric(A, B, C, P):
  cx, cy, cz = cross(
    V3(B.x - A.x, C.x - A.x, A.x - P.x),
    V3(B.y - A.y, C.y - A.y, A.y - P.y)
  )

  if abs(cz) < 1:
    return -1, -1, -1


  u = cx/cz
  v = cy/cz
  w = 1 - (cx + cy)/cz

  return w, v, u

# -------------------------------------------------------------------------
# def multiplicacion(matriz1, matriz2, c1, f1, c2, f2):  # función para multiplicar matrices
#   matriz3 = []
#   for i in range(f1):
#     matriz3.append([0] * c2)
#
#   for i in range(f1):
#     for j in range(c2):
#       for k in range(f2):
#         numf = matriz1[i][k] * matriz2[k][j]
#         matriz3[i][j] += numf
#
# def division(self, norm, frobenius):
#   if (frobenius==0):
#     res=[]
#     res.append(float('NaN'))
#     res.append(float('NaN'))
#     res.append(float('NaN'))
#     return res
#
#   else:
#     res=[]
#     res.append(norm[0]/ frobenius)
#     res.append(norm[1]/ frobenius)
#     res.append(norm[2]/ frobenius)
#     return res
#
# def frobenius(self, norm):
#     return ((norm[0] ** 2 + norm[1] ** 2 + norm[2] ** 2) ** (1 / 2))




