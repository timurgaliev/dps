# -*-utf-8_*_, python 3.7
#'''Timur Galiev 5305'''

import numpy as np
import matplotlib.pyplot as plt


def given(n):
    return 1.5+(-1.2)**n


def twiddle_factor(n):
    return np.e**(-1j*2*np.pi*n/8)  # N = 8


def solution():
    res = list([])
    for k in range(8):
        s = 0
        for n in range(8):
            s += given(n)*(twiddle_factor(n)**k)
        res.append(s)
    return res


def amplitude_spectrum_plot():
    w = list([i for i in range(8)])
    res_abs = [abs(i) for i in solution()]
    plt.stem(w, res_abs)
    plt.grid(True)
    #plt.xlim(0, 7)
    plt.xlabel('w')
    plt.ylabel('|x(w)|')
    plt.savefig('amplitude_spectrum.png', dpi=80)
    plt.show()


def phase_spectrum_plot():
    w = list([i for i in range(8)])
    res_arg = [np.angle(i, deg=True) for i in solution()]
    plt.stem(w, res_arg)
    plt.grid(True)
    #plt.xlim(0, 7)
    plt.savefig('phase_spectrum.png', dpi=80)
    plt.xlabel('w')
    plt.ylabel('arg')
    plt.show()


if __name__ == '__main__':
    print('Найдем x(n):')
    for _ in range(8):
        print('x(' + str(_) + ') = ' + str('%.3f') % given(_))
    print('Найдем x(k):')
    for __ in range(8):
        print('x(' + str(__) + ') = ' + str(solution()[__]))
    print('Найдем |x(k)|:')
    for _ in solution():
        print(abs(_))
    print('Найдем arg:')
    for _ in solution():
        print(np.angle(_, deg=True))
    amplitude_spectrum_plot()
    phase_spectrum_plot()
