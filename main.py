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

r = Render(800,600, 'Escena.bmp')
r.glClear()
r.activeT = Texture('./models/peach.bmp')

posModel = V3( 0, 0, -5)
r.actSha = gourad

light = V3(0.5,0,1)

normal = norm(light)

light = V3(light[0]/normal,light[1]/normal,light[2]/normal)
r.light = light

r.lookAt(posModel, V3(0,0,5))
r.loadModel('./models/peach-tennis.obj', posModel,V3(2,2,2), V3(0,0,0))

r.glFinish()


