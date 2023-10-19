import math
from typing import Final
import sympy as s
import numpy as np
import Utils

# 1-8
a: Final[float] = 1
b: Final[float] = 2
rotationAngle = 30

# 9
c: Final[float] = 3

examplePoint1: s.Matrix = s.Matrix([[2], [-1]])
examplePoint2: s.Matrix = s.Matrix([[2], [2]])


def m1():
    m: s.Matrix = s.Matrix([[1, 0], [0, -1]])
    alfa = math.atan(a)
    m = Utils.rotate(m, alfa)

    i = examplePoint1
    j = m * i
    Utils.drawToPoints([i], [j], True)
    return m


def m2():
    m: s.Matrix = s.Matrix([[1, 0], [0, 0]])
    alfa = math.atan(a)
    m = Utils.rotate(m, alfa)

    i = examplePoint1
    j = m * i
    Utils.drawToPoints([i], [j], True)
    return m


def m3():
    alfa = -rotationAngle * s.pi / 180
    sin = math.sin(alfa)
    cos = math.cos(alfa)
    m: s.Matrix = s.Matrix([[cos, sin], [-sin, cos]])

    i = examplePoint1
    j = m * i
    Utils.drawToPoints([i], [j])
    return m


def m4():
    m: s.Matrix = s.Matrix([[-1, 0], [0, -1]])

    i = examplePoint1
    j = m * i
    Utils.drawToPoints([i], [j])
    return m


def m5():
    m: s.Matrix = s.Matrix([[1, 0], [0, -1]])
    alfa = s.atan(a)
    m = Utils.rotate(m, alfa)

    alfa = -rotationAngle * s.pi / 180
    sin = math.sin(alfa)
    cos = math.cos(alfa)
    t: s.Matrix = s.Matrix([[cos, sin], [-sin, cos]])

    m = m * t

    i = examplePoint1
    j = m * i
    Utils.drawToPoints([i], [j], True)
    return m


def m6():
    alfa = math.atan(a)
    gamma = math.atan(b)
    m: s.Matrix = s.Matrix([[math.cos(alfa), math.cos(gamma)],
                            [math.sin(alfa), math.sin(gamma)]])

    i = examplePoint2
    j = m * i
    Utils.drawToPoints([i], [j], True, True)
    return m


def m7():
    alfa = math.atan(a)
    gamma = math.atan(b)
    m: s.Matrix = s.Matrix([[math.cos(alfa), math.cos(gamma)],
                            [math.sin(alfa), math.sin(gamma)]])
    m = m.inv()
    i = examplePoint2
    j = m * i
    Utils.drawToPoints([i], [j], True, True)
    return m


def m8():
    alfa = math.atan(a)
    beta = math.atan(b)

    gamma = (alfa + beta) / 2
    m: s.Matrix = s.Matrix([[1, 0],
                            [0, -1]])
    m = Utils.rotate(m, gamma)

    i = examplePoint2
    j = m * i
    Utils.drawToPoints([i], [j], True, True)
    return m


def m9():
    scale = c**0.5
    m: s.Matrix = s.Matrix([[scale, 0],
                            [0, scale]])

    count = 100
    angles = np.linspace(0, 2*math.pi, count)
    x1 = 1 * np.cos(angles)
    y1 = 1 * np.sin(angles)

    x2 = np.empty((count))
    y2 = np.empty((count))

    v: s.Matrix = s.Matrix([[0], [0]])
    for i in range(count):
        v[0, 0] = x1[i]
        v[1, 0] = y1[i]
        v = m * v
        x2[i] = v[0, 0]
        y2[i] = v[1, 0]

    Utils.drawCircles(x1, y1, "r", x2, y2, "g")
    return m
