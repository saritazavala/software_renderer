#Universidad del Valle de Guatemala
#Sara Zavala 18893
#RT1-Esferas
#Graficas

from glFunctions import *
from shaders import *

from Object import *
from glFunctions import *
from shaders import *
from mathFunctions import *

r = Render(800,600, 'Nueva.bmp')
r.glClear()
r.actSha = gourad
light = V3(0.5,0,1)
posModel = V3(0,0,-5)
normal = norm(light)

light = V3(light[0]/normal,light[1]/normal,light[2]/normal)
r.light = light

r.lookAt(posModel, V3(0,0,0))

# Conejo
r.activeT = Texture('./models/rabbit.bmp')
r.loadModel('./models/rabbit.obj', posModel, V3(1,1,1), V3(0,10,0))
#
# dog
r.activeT = Texture('./models/husky.bmp')
r.loadModel('./models/husky.obj', posModel, V3(1,1,1), V3(0,0,0))
#
# #deer
r.activeT = Texture('./models/deer.bmp')
r.loadModel('./models/deer.obj', posModel,V3(0.02,0.02,0.02), V3(0,0,0))

#duck
r.activeT = Texture('./models/duck.bmp')
r.loadModel('./models/duck.obj', posModel,V3(0.05,0.05,0.05), V3(0,30,10))
#
 #Penguin
posModel = V3(-2,0,-5)
r.activeT = Texture('./models/Pen.bmp')
r.loadModel('./models/Pen.obj', posModel,V3(1,1,1), V3(0,0,0))

r.glFinish()


