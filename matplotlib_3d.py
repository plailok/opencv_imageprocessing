# -*- coding: utf-8 -*-
import cv2
import pylab
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy


def makeData():
    x = numpy.random.rand(100) * 20.0 - 10.0
    y = numpy.random.rand(100) * 20.0 - 10.0
    x.sort()
    y.sort()
    xgrid, ygrid = numpy.meshgrid(x, y)

    zgrid = numpy.sin(xgrid * 0.3) * numpy.cos(ygrid * 0.75)
    return xgrid, ygrid, zgrid


if __name__ == '__main__':
    image = cv2.imread('background_1.jpg')
    r, g, b = cv2.split(image)
    print(len(r))
    listek = [r, g, b]
    colors = cm.colors
    print(colors)
    x = numpy.linspace(0, 1, 1024)
    y = numpy.linspace(0, 1, 768)
    xgrid, ygrid = numpy.meshgrid(x, y)

    # x, y, z = makeData()
    for index, value in enumerate(listek):
        print(value)
        fig = pylab.figure(index)
        axes = Axes3D(fig)
        z = value
        axes.plot_surface(xgrid, ygrid, z)
        pylab.show()
