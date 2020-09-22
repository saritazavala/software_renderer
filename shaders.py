from glFunctions import *
from mathFunctions import *
import random



def psychedelic(render, **kwargs):
    u, v, w = kwargs['barycentric']
    ta, tb, tc = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render:
        tx = ta.x * u + tb.x * v + tc.x * w
        ty = ta.y * u + tb.y * v + tc.y * w
        texColor = render.activeT.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = V3(nx, ny, nz)

    intensity = dot(normal, render.light)
    if intensity >0:
        if intensity > 0.95:
            r *= 0.7 * intensity
        elif intensity > 0.9:
            g *= 0.7 * intensity
        elif intensity > 0.85:
            b *= 0.7 * intensity
        elif intensity > 0.8:
            r *= 0.5 * intensity

        elif intensity > 0.75:
            g *= 0.5 * intensity

        elif intensity > 0.7:
            b *= 0.5 * intensity

        elif intensity > 0.65:
            r *= 0.25 * intensity

        elif intensity > 0.6:
            g *= 0.25 * intensity

        elif intensity > 0.55:
            b *= 0.25 * intensity

        elif intensity > 0.5:
            r *= 0.12 * intensity

        elif intensity > 0.4:
            g *= 0.12 * intensity

        elif intensity > 0.3:
            b *= 0.12 * intensity

        elif intensity > 0.2:
            r *= 0.6 * intensity

        elif intensity > 0.1:
            g *= 0.6 * intensity

        elif intensity >= 0.0:
            b *= 0.6 * intensity
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def intense(render, **kwargs):
    u, v, w = kwargs['barycentric']
    ta, tb, tc = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render:
        tx = ta.x * u + tb.x * v + tc.x * w
        ty = ta.y * u + tb.y * v + tc.y * w
        texColor = render.activeT.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = V3(nx, ny, nz)

    intensity = dot(normal, render.light)
    if intensity >0:
        if intensity > 0 and intensity < 0.25:
            intensity = 0.125
        elif intensity > 0.25 and intensity < 0.50:
            intensity = 0.375

        elif intensity > 0.50 and intensity <0.75:
            intensity = 0.625

        elif intensity > 0.75 and intensity <1:
            intensity = 0.875


    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


