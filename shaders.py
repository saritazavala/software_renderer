from glFunctions import *
from mathFunctions import *
import random


def gourad(render, **kwargs):
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

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def toon(render, **kwargs):
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

    if intensity > 0:
        if intensity > 0.95:
            intensity = 1
        elif intensity > 0.9:
            intensity = 0.95
        elif intensity > 0.8:
            intensity = 0.85
        elif intensity > 0.6:
            intensity = 0.7
        elif intensity > 0.4:
            intensity = 0.5
        elif intensity > 0.2:
            intensity = 0.3
        elif intensity > 0:
            intensity = 0.1

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def night(render, **kwargs):
    u, v, w = kwargs['baryCoords']
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

    b *= intensity / 1
    g *= intensity / 2
    r *= intensity / 3

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def static(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    ta, tb, tc = kwargs['texCoords']
    na, nb, nc = kwargs['normals']

    b = random.random()
    g = random.random()
    r = random.random()

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

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def topographic(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    na, nb, nc = kwargs['normals']

    if render:
        b = 1
        g = 1
        r = 1

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = V3(nx, ny, nz)

    intensity = dot(normal, render.light)

    if intensity > 0:
        if intensity > 0.95:
            r *= 0.44 * intensity
            g *= 0.02 * intensity
            b *= 0 * intensity
        elif intensity > 0.9:
            r *= 0.69 * intensity
            g *= 0.11 * intensity
            b *= 0.08 * intensity
        elif intensity > 0.8:
            r *= 0.91 * intensity
            g *= 0.23 * intensity
            b *= 0.07 * intensity
        elif intensity > 0.6:
            r *= 0.91 * intensity
            g *= 0.44 * intensity
            b *= 0.17 * intensity
        elif intensity > 0.4:
            r *= 0.91 * intensity
            g *= 0.66 * intensity
            b *= 0.27 * intensity
        elif intensity > 0.3:
            r *= 0.63 * intensity
            g *= 0.91 * intensity
            b *= 0.15 * intensity
        elif intensity > 0:
            r *= 0.15 * intensity
            g *= 0.91 * intensity
            b *= 0.8 * intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def comic(render, **kwargs):
    u, v, w = kwargs['baryCoords']
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

    b = round(b * intensity, 1)
    g = round(g * intensity, 1)
    r = round(r * intensity, 1)

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def grises(render, **kwargs):
    u, v, w = kwargs['baryCoords']
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
    ba = b
    b = b * intensity
    g = ba * intensity
    r = ba * intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def invgourad(render, **kwargs):
    u, v, w = kwargs['baryCoords']
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
    if intensity > 0:
        intensity = 1 - intensity

    if intensity < 0:
        intensity += 1

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0