#Universidad del Valle de Guatemala
#Sara Zavala 18893
#RT1-Esferas
#Graficas

from collections import namedtuple
import math

# REFERENCES
#https://www.it-swarm.dev/es/python/inversion-matricial-sin-numpy/1054196902/


V2 = namedtuple('Vertex2', ['x', 'y'])
V3 = namedtuple('Vertex3', ['x', 'y', 'z'])
V4 = namedtuple('Point4', ['x', 'y', 'z','w'])

def start_norm(x,a):
    y = 1 / a
    y = float(y)
    z = x ** y
    return z

def convert(a):
    a = (a * 3.14159165) / 180
    return a

def sum(v0, v1):
  return V3(v0.x + v1.x, v0.y + v1.y, v0.z + v1.z)

# def sub(v0, v1):
#   return V3(v0.x - v1.x, v0.y - v1.y, v0.z - v1.z)


def sub(a, b):
    c = [a[0] - b[0],
         a[1] - b[1],
         a[2] - b[2]]
    return c


# def mul(v0, k):
#   return V3(v0.x * k, v0.y * k, v0.z *k)

def mul(a, b):
    c=[]
    for i in range(len(a)):
        c.append([0]*len(b[0]))

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k]*b[k][j]

    return c

def dot(v0, v1):
  return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z

#Vector - List multiplication

def vec_matrx(a,b):
    c=[]
    for i in range(len(a)):
        c.append(0)
    for i in range(len(a)):
        for k in range(len(a[0])):
            c[i] += a[i][k]*b[k]
    return c

#Lists
def cross(a, b):
    c = [a[1] * b[2] - a[2] * b[1],
         a[2] * b[0] - a[0] * b[2],
         a[0] * b[1] - a[1] * b[0]]
    return c

# def cross(v1, v2):
#   return V3(
#     v1.y * v2.z - v1.z * v2.y,
#     v1.z * v2.x - v1.x * v2.z,
#     v1.x * v2.y - v1.y * v2.x,
#   )

def length(v0):
  return (v0.x**2 + v0.y**2 + v0.z**2)**0.5


# def norm(v0):
#   v0length = length(v0)
#   if not v0length:
#     return V3(0, 0, 0)
#
#   return V3(v0.x/v0length, v0.y/v0length, v0.z/v0length)

#Lists
def norm(a):
    c = start_norm(float(a[0]**2)+(a[1]**2)+(a[2]**2), 2)
    return c


def bbox(*vertices):

  xs = [ vertex.x for vertex in vertices ]
  ys = [ vertex.y for vertex in vertices ]

  return (max(xs), max(ys), min(xs), min(ys))


def barycentric(A, B, C, P):
    try:
        u = ( ((B.y - C.y)*(P.x - C.x) + (C.x - B.x)*(P.y - C.y) ) /
              ((B.y - C.y)*(A.x - C.x) + (C.x - B.x)*(A.y - C.y)) )

        v = ( ((C.y - A.y)*(P.x - C.x) + (A.x - C.x)*(P.y - C.y) ) /
              ((B.y - C.y)*(A.x - C.x) + (C.x - B.x)*(A.y - C.y)) )

        w = 1 - u - v
    except:
        return -1, -1, -1

    return u, v, w

# ---------------
#Codigo para hacer el inverso de una matriz obtenido de:
#https://www.it-swarm.dev/es/python/inversion-matricial-sin-numpy/1054196902/
def transpuesta(m):
    a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(0, 4):
        for j in range(0, 4):
            a[j][i] = m[i][j]
    return a

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transpuesta(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors




