# файл для проверок
# runfile('', wdir='C:/Users/ggamm/PycharmProjects/Geogebra_python')
import numpy as np

np.set_printoptions(precision=4, threshold=99999, linewidth=99999, suppress=True)
# n = map(int, input().split())
a, b = eval(open('input.txt').read())
a1 = a[:, 0]
a2 = a[:, 1]
b1 = b[:, 0]
b2 = b[:, 1]
res = a1 * b1 + a2 * b2
print(repr(res))