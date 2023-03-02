import random
import timeit

import matplotlib.pyplot as plt


# Detrminant simplu
def det_simplu(x: int):
    det_simplu_c(gen_random_m(x))

def det_simplu_c(m: list[list]):
    n = len(m)
    assert n == len(m[0]), "Matricea nu e patratica!"
    if n == 1:
        return m[0][0]
    elif n == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    else:
        det = 0
        for j in range(n):
            subm = [[m[i][k] for k in range(n) if k != j] for i in range(1, n)]
            cofactor = (-1)**j * det_simplu_c(subm)
            det += m[0][j] * cofactor
        return det


# Gauss-Jordan
def det_gauss_jordan(x: int):
    det_gauss_jordan_c(gen_random_m(x))


def det_gauss_jordan_c(m: list[list]):
    randuri, coloane = len(m), len(m[0])
    assert randuri == coloane, "Matricea nu e patratica"
    det = 1
    for i in range(randuri):
        m_val = abs(m[i][i])
        m_rand = i
        for j in range(i+1, randuri):
            if abs(m[j][i]) > m_val:
                m_val = abs(m[j][i])
                m_rand = j
        if m_val == 0:
            return 0
        if m_rand != i:
            m[i], m[m_rand] = m[m_rand], m[i]
            det *= -1
        det *= m[i][i]
        for j in range(i+1, randuri):
            c = m[j][i] / m[i][i]
            for k in range(i, coloane):
                m[j][k] -= c * m[i][k]
    return det

def gen_random_m(n: int):
    return [[random.randint(0, 10) for x in range(n)] for y in range(n)]

# matrice = gen_random_m(5)

# st = time.process_time()
# print(det_simplu_c(matrice))
# et = time.process_time()
# print(et-st)

# qst = time.process_time()
# print(round(det_gauss_jordan_c(matrice)))
# qet = time.process_time()
# print(qet-qst)

simplu = []
gauss_jordan = []

for num in range(2, 13):
    a = timeit.timeit("det_simplu(num)", globals=globals(), number = 100)
    b = timeit.timeit("det_gauss_jordan(num)", globals=globals(), number = 100)
    simplu.append(a)
    gauss_jordan.append(b)
    print(num, "gata")

n_values = list([x+1 for x in range(1, len(simplu)+1)])

plt.plot(n_values, simplu, label='Simplu')
plt.plot(n_values, gauss_jordan, label='Gauss-Jordan')
plt.xlabel('n')
plt.ylabel('Timp (s)')
plt.legend()
plt.show()