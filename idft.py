# inverse discrete Fourier transform
# _*_UTF-8_*_
# Galiev Timur 5305
import numpy as np
import cmath as c

N = 8
X = {0: 10.502,
1: -1.472-0.67j,
2: -1.35-1.62j,
3: -0.67-3.76j,
4: 16.49,
5: -0.67+3.76j,
6: -1.35+1.62j,
7: -1.47+0.67j}


def twiddle_factor(n):
    return np.e**(1j*2*np.pi*n/8)  # N = 8


def result():
    res = []
    for n in range(8):
        s = 0
        for k in range(8):
            s += (1/N)*X[k]*(twiddle_factor(n)**k)
        res.append(str('%.4f'%s.real))
    return res


if __name__ == '__main__':
    print(result())
