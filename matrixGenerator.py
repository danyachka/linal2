from typing import Final
import sympy as s
import math
import Utils

# 1-8
a: Final[float] = 2
b: Final[float] = 3
rotationAngle = 30

# 9
c: Final[float] = 3

# 10
d = 4

examplePoint1: s.Matrix = s.Matrix([[2], [-1]])
examplePoint2: s.Matrix = s.Matrix([[2], [2]])
examplePoint3: s.Matrix = s.Matrix([[2], [3]])


def m1():
    m: s.Matrix = s.Matrix([[1, 0], [0, -1]])
    alfa = math.atan(a)
    m = Utils.rotate(m, alfa)

    i = Utils.square
    j = Utils.convertPoints(i, m)
    plots = [Utils.Plot(i, Utils.Color.red, m=m), Utils.Plot(j, Utils.Color.green)]
    Utils.drawColoredPlots(plots, 1, True)
    return m


def m2():
    m: s.Matrix = s.Matrix([[1, 0], [0, 0]])
    alfa = math.atan(a)
    m = Utils.rotate(m, alfa)

    i = Utils.square
    j = Utils.convertPoints(i, m)
    plots = [Utils.Plot(i, Utils.Color.red), Utils.Plot(j, Utils.Color.green)]
    Utils.drawColoredPlots(plots, 2, True)
    return m


def m3():
    alfa = -rotationAngle * s.pi / 180
    sin = math.sin(alfa)
    cos = math.cos(alfa)
    m: s.Matrix = s.Matrix([[cos, sin], [-sin, cos]])

    i = Utils.square
    j = Utils.convertPoints(i, m)
    plots = [Utils.Plot(i, Utils.Color.red), Utils.Plot(j, Utils.Color.green)]
    Utils.drawColoredPlots(plots, 3)
    return m


def m4():
    m: s.Matrix = s.Matrix([[-1, 0], [0, -1]])

    i = Utils.square
    j = Utils.convertPoints(i, m)
    plots = [Utils.Plot(i, Utils.Color.red), Utils.Plot(j, Utils.Color.green)]
    Utils.drawColoredPlots(plots, 4)
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

    i = Utils.square
    j = Utils.convertPoints(i, m)
    plots = [Utils.Plot(i, Utils.Color.red), Utils.Plot(j, Utils.Color.green)]
    Utils.drawColoredPlots(plots, 5, True)
    return m


def m6():
    alfa = math.atan(a)
    gamma = math.atan(b)
    m: s.Matrix = s.Matrix([[math.cos(alfa), math.cos(gamma)],
                            [math.sin(alfa), math.sin(gamma)]])

    i = Utils.square
    j = Utils.convertPoints(i, m)
    plots = [Utils.Plot(i, Utils.Color.red), Utils.Plot(j, Utils.Color.green)]
    Utils.drawColoredPlots(plots, 6, True, True)
    return m


def m7():
    alfa = math.atan(a)
    gamma = math.atan(b)
    m: s.Matrix = s.Matrix([[math.cos(alfa), math.cos(gamma)],
                            [math.sin(alfa), math.sin(gamma)]])
    m = m.inv()
    i = Utils.square
    j = Utils.convertPoints(i, m)
    plots = [Utils.Plot(i, Utils.Color.red), Utils.Plot(j, Utils.Color.green)]
    Utils.drawColoredPlots(plots, 7, True, True)
    return m


def m8():
    alfa = math.atan(a)
    beta = math.atan(b)

    gamma = (alfa + beta) / 2
    m: s.Matrix = s.Matrix([[1, 0],
                            [0, -1]])
    m = Utils.rotate(m, gamma)

    i = Utils.square
    j = Utils.convertPoints(i, m)
    plots = [Utils.Plot(i, Utils.Color.red), Utils.Plot(j, Utils.Color.green)]
    Utils.drawColoredPlots(plots, 8, True, True)
    return m


def m9():
    scale = c**0.5
    m: s.Matrix = s.Matrix([[scale, 0],
                            [0, scale]])

    Utils.createCircleAndOtherPlot(m, 9)
    return m


def m10():
    scaleX = 2**0.5 * d**0.5
    scaleY = 0.5**0.5 * d**0.5
    m: s.Matrix = s.Matrix([[scaleX, 0], [0, scaleY]])

    Utils.createCircleAndOtherPlot(m, 10)
    return m


def m11():
    m: s.Matrix = s.Matrix([[0.5, 1], [1, 2]])

    i = Utils.square
    j = Utils.convertPoints(i, m)
    plots = [Utils.Plot(i, Utils.Color.red, m=m), Utils.Plot(j, Utils.Color.green)]
    Utils.drawColoredPlots(plots, 11)
    return m


def m12():
    m: s.Matrix = s.Matrix([[0.5, 1], [0, 0.5]])
    i = Utils.square
    j = Utils.convertPoints(i, m)
    plots = [Utils.Plot(i, Utils.Color.red, m=m), Utils.Plot(j, Utils.Color.green)]
    Utils.drawColoredPlots(plots, 12)
    return m


def m13():
    m: s.Matrix = s.Matrix([[0.5, -1], [1, 2]])
    i = Utils.square
    j = Utils.convertPoints(i, m)
    plots = [Utils.Plot(i, Utils.Color.red, m=m), Utils.Plot(j, Utils.Color.green)]
    Utils.drawColoredPlots(plots, 13)
    return m


def m14():
    m: s.Matrix = s.Matrix([[1, 0], [0, 1]])
    i = Utils.square
    j = Utils.convertPoints(i, m)
    plots = [Utils.Plot(i, Utils.Color.red, m=m), Utils.Plot(j, Utils.Color.green)]
    Utils.drawColoredPlots(plots, 14)
    return m


def m15():
    A: s.Matrix = s.Matrix([[1, 0], [0, -1]])
    B: s.Matrix = s.Matrix([[1, 1], [2, 2]])

    m15And16(A, B, 15)
    return


def m16():
    A: s.Matrix = s.Matrix([[1, 0], [0, 1]])
    B: s.Matrix = s.Matrix([[1, 3], [1, 2]])

    m15And16(A, B, 16)
    return


def m15And16(A, B, number):
    matrix1: s.Matrix = A * B
    matrix2: s.Matrix = B * A
    print("Первая матрица - " + str(A))
    print("Вторая матрица - " + str(B))
    print("\nA*B - " + str(matrix1))
    Utils.printEigenValues(matrix1)
    print("\nB*A - " + str(matrix2))
    Utils.printEigenValues(matrix2)

    i = Utils.square
    j = Utils.convertPoints(i, matrix1)
    k = Utils.convertPoints(i, matrix2)
    plots = [Utils.Plot(i, Utils.Color.red), Utils.Plot(j, Utils.Color.green, m=matrix1, plotName="A*B"),
             Utils.Plot(k, Utils.Color.blue, m=matrix2, plotName="B*A")]
    Utils.drawColoredPlots(plots, number)

    j = Utils.convertPoints(i, A)
    k = Utils.convertPoints(i, B)
    plots = [Utils.Plot(j, Utils.Color.green, m=matrix1, plotName="A"),
             Utils.Plot(k, Utils.Color.blue, m=matrix2, plotName="B")]
    Utils.drawColoredPlots(plots, number)
