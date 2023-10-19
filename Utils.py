import numpy as np
import sympy as s
from matplotlib import pyplot as plt
from matplotlib import patches
import matrixGenerator

MAX_X_AND_Y = 5


def drawToPoints(red: [s.Matrix], green: [s.Matrix], lineA=False, lineB=False):
    fig = plt.figure(figsize=(7, 7))
    greenX = [green[i][0, 0] for i in range(len(green))]
    greenY = [green[i][1, 0] for i in range(len(green))]
    redX = [red[i][0, 0] for i in range(len(red))]
    redY = [red[i][1, 0] for i in range(len(red))]

    ax = fig.add_subplot()
    ax.plot(greenX, greenY, "D", color="green")
    ax.plot(redX, redY, "D", color="red")
    ax.grid()

    if lineA:
        x = MAX_X_AND_Y
        y = matrixGenerator.a * x
        ax.plot([-x, x], [-y, y], "--", color="Blue")
    if lineB:
        x = MAX_X_AND_Y
        y = matrixGenerator.b * x
        ax.plot([-x, x], [-y, y], "--", color="Blue")

    ax.set_xlim([-MAX_X_AND_Y, MAX_X_AND_Y])
    ax.set_ylim([-MAX_X_AND_Y, MAX_X_AND_Y])


def drawCircles(x1, y1, color: str, x2, y2, color2: str):
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot()

    ax.plot(x1, y1, "--", color=color)
    ax.plot(x2, y2, "--", color=color2)

    ax.grid()

    ax.set_xlim([-MAX_X_AND_Y, MAX_X_AND_Y])
    ax.set_ylim([-MAX_X_AND_Y, MAX_X_AND_Y])


def rotate(m: s.Matrix, alfa):
    t: s.Matrix = s.zeros(2)
    sin = s.sin(alfa)
    cos = s.cos(alfa)

    t[0, 0] = cos
    t[0, 1] = sin
    t[1, 0] = -sin
    t[1, 1] = cos

    m = t.inv() * m * t
    return m
