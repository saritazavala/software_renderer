#Universidad del Valle de Guatemala
#Sara Zavala 18893
#RT1-Esferas
#Graficas

from glFunctions import *
from shaders import *

r = Render('help.bmp')
r.glCreateWindow(800,600)
r.glClear()
r.active_texture = Texture('./models/model.bmp')
r.active_shader = toon

posModel = V3(0, 0, -5)

r.lookAt(posModel, V3(0, 0, 0), V3(0, 1, 0))


r.load_model('./models/model.obj', translate=(-0.8, 0.6, 0), scale=(0.35,0.5,0.5), rotate=(0, 0, 0))

r.glFinish()
