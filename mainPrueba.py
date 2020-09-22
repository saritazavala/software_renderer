from Object import *
from glFunctions import *
from shaders import *
from mathFunctions import *

#Creacion de render
r = Render(800,600, 'PruebaShaders.bmp')
r.glClear()

#Shader
r.actSha = intense

#Luz
light = V3(0.5,0,1)
normal = norm(light)
light = V3(light[0]/normal,light[1]/normal,light[2]/normal)
r.light = light

#Poscion de modelo
posModel = V3(0,0,-5)

#Camara
r.lookAt(posModel, V3(0,0,0))

# #Cara de prueba

r.activeT = Texture('./models/model.bmp')
r.loadModel('./models/model.obj', posModel,V3(2,2,2), V3(0,0,0))

r.glFinish()
