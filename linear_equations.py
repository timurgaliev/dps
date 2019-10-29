# _*_UTF-8_*_
# linear_equations, https://github.com/timurgaliev/dps
# Galiev Timur 5305

import numpy as np
import matplotlib.pyplot as plt
import os


x_1 = {-2: 0, -1: 0}
x_2 = {-2: 0, -1: 0}
y_1 = {-2: 0, -1: 0}
y_2 = {-2: 0, -1: 0}
y_3 = {-2: 0, -1: 0}
y_4 = {-2: 0, -1: 0}


def given_upgrade():
    for n in range(8):
        x_1[n] = 0.8**n + 2**(n-1)
        x_2[n] = -2 - 0.4**n
        y_1[n] = 0.7 * x_1[n] - 0.5 * y_1[n-1]
        y_3[n] = 0.7 * x_2[n] - 0.5 * y_3[n-1]
        y_2[n] = 0.8 * x_1[n] + 0.6 * x_1[n - 1] - 1.6 * y_2[n - 1] - 1.4 * y_2[n - 2]
        y_4[n] = 0.8 * x_2[n] + 0.6 * x_2[n - 1] - 1.6 * y_4[n - 1] - 1.4 * y_4[n - 2]


def write(information, filename='linear_equations.txt'):
    with open(os.path.join(r'C:\Users\Timur\PycharmProjects\webhook\linear_equations', str(filename)), 'a') as f:
        f.write(information + '\n')


def plott(x, y, title_x='not found', title_y='not found'):
    a = np.arange(0, 8)
    res_x = []
    res_y = []
    for _ in range(8):
        res_x.append(x[_])
        res_y.append(y[_])
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,9))
    ax1.stem(a, res_x, use_line_collection=True)
    ax1.set_title(title_x)
    ax1.grid()
    ax2.stem(a, res_y, use_line_collection=True)
    ax2.set_title(title_y)
    ax2.grid()
    plt.savefig(os.path.join(r'C:\Users\Timur\PycharmProjects\webhook\linear_equations',
                             str(title_x) + str(title_y) + '.png'), figsize=(16, 9), dpi=100)
    #plt.show()


if __name__ == '__main__':
    given_upgrade()
    t = True
    while t:
        user_input = input('Выберите x(n) и y(n):')
        if user_input == 'выйти':
            t = False
        elif user_input == '11':
            write('Вариант x_1, y_1')
            for _ in range(8):
                write('x_1('+str(_)+') =  '+str('%.4f' % x_1[_]))
            for _ in range(8):
                write('y_1(' + str(_) + ') =  ' + str('%.4f' % y_1[_]))
            plott(x_1, y_1, title_x='x_1', title_y='y_1')
        elif user_input == '12':
            write('Вариант x_1, y_2')
            for _ in range(8):
                write('x_1('+str(_)+') =  '+str('%.4f' % x_1[_]))
            for _ in range(8):
                write('y_2(' + str(_) + ') =  ' + str('%.4f' % y_2[_]))
            plott(x_1, y_2, title_x='x_1', title_y='y_2')
        elif user_input == '21':
            write('Вариант x_2, y_3')
            for _ in range(8):
                write('x_2('+str(_)+') =  '+str('%.4f' % x_2[_]))
            for _ in range(8):
                write('y_1(' + str(_) + ') =  ' + str('%.4f' % y_3[_]))
            plott(x_2, y_3, title_x='x_2', title_y='y_3')
        elif user_input == '22':
            write('Вариант x_2, y_4')
            for _ in range(8):
                write('x_2('+str(_)+') =  '+str('%.4f' % x_2[_]))
            for _ in range(8):
                write('y_2(' + str(_) + ') =  ' + str('%.4f' % y_4[_]))
            plott(x_2, y_4, title_x='x_2', title_y='y_4')
        else:
            print('Ошибка')
