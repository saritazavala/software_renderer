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

#Creacion de render
r = Render(800,600, 'NEW.bmp')
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
r.lookAt(posModel, V3(3,2,0))

#Fondo
h = 640
w = 800

r.activeT = Texture('./models/a.bmp')
for y in range(len(r.framebuffer)):
    for x in range(len(r.framebuffer[y])):
        r.glpoint(x,y,r.activeT.getColor(x/w,y/h))

# #Penguin
posModel = V3(1,0,-1)
r.activeT = Texture('./models/Pen.bmp')
r.loadModel('./models/Pen.obj', posModel,V3(1,1,1), V3(-10,65,0))

# # dog
posModel = V3(3,-0.5,-4)
r.activeT = Texture('./models/husky.bmp')
r.loadModel('./models/husky.obj', posModel, V3(1,1,1), V3(-10,-20,5))
#
# # Conejo
posModel = V3(-1,-4,-8)
r.activeT = Texture('./models/rabbit.bmp')
r.loadModel('./models/rabbit.obj', posModel, V3(1,1,1), V3(-10,3,0))
# #
# # #duck
posModel = V3(2,-2,-6)
r.activeT = Texture('./models/duck.bmp')
r.loadModel('./models/duck.obj', posModel,V3(0.03,0.03,0.03), V3(-100,-15,0))
# #
# # #deer
posModel = V3(0,-1,-3)
r.activeT = Texture('./models/deer.bmp')
r.loadModel('./models/deer.obj', posModel,V3(0.02,0.02,0.02), V3(-90,0,0))

# bird
posModel = V3(0,0,-5)
r.activeT = Texture('./models/bird.bmp')
r.loadModel('./models/bird.obj', posModel, V3(0.1,0.1,0.1), V3(-90,0,0))


r.glFinish()


