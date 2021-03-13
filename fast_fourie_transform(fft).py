from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

import cv2 as cv
import argparse


class FastFourierTranform:

    def __init__(self):
        self.number_of_line_max = 1000
        self.frequency_max = 10000
        self.title_window = 'fft'
        self.N = 100
        self.T = 1.0 / 200
        self.x = None
        self.y = None
        self.yf = None
        self.xf = None
        self.build_gui()
        self.rebuild_plot()

    def build_gui(self):
        cv.namedWindow(self.title_window)
        trackbar_name = 'N '
        trackbar1_name = 'Freq (v)'
        cv.createTrackbar(trackbar_name, self.title_window, 1, self.number_of_line_max, self.on_trackbar)
        cv.createTrackbar(trackbar1_name, self.title_window, 1, self.frequency_max, self.on_trackbar1)
        cv.waitKey()

    def on_trackbar(self, val):
        try:
            self.N = val
        except ZeroDivisionError:
            return
        finally:
            print('number of wave', self.N)
            self.rebuild_plot()

    def rebuild_plot(self):
        self.x = np.linspace(0.0, self.N * self.T, self.N, endpoint=False)
        self.y = np.sin(50.0 * 2.0 * np.pi * self.x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * self.x)
        self.yf = fft(self.y)
        self.xf = fftfreq(self.N, self.T)[:self.N // 2]
        self.plot()

    def plot(self):
        plt.plot(self.xf, 2.0 / self.N * np.abs(self.yf[0:self.N // 2]))
        plt.grid()
        plt.show()

    def on_trackbar1(self, val):
        try:
            self.T = int(1.0 / (1 / val))
        except ZeroDivisionError:
            return
        finally:
            print('freq=', self.T)
            self.rebuild_plot()


if __name__ == '__main__':
    FastFourierTranform()
