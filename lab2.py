from math import sqrt, exp, sin
from matplotlib import pyplot as plt

a = 4
b = 7

n = 4
m = 4

f = lambda x : exp(x) / x ** 3 - sin(x) ** 3
x_i = lambda i : a + (i - 1) * (b - a) / (m - 1)
x_error_i = lambda j : a + (j - 1) * (b - a) / 20

x_array = [x_i(i) for i in range(1, n + 1)]
x_error_array = [x_error_i(j) for j in range(1, 22)]

G = [[x ** i for i in range(n)] for x in x_array]
y = [f(x) for x in x_array]

def gauss(A_matrix, b_array):
    A = A_matrix[:]
    b = b_array[:]
    n = len(b)
    x = [0 for _ in range(n)]
    for k in range(n - 1):
        p = k
        for m in range(k + 1, n):
            if abs(A[p][k]) < abs(A[m][k]):
                p = m
        for j in range(k, n):
            r = A[k][j]
            A[k][j] = A[p][j]
            A[p][j] = r
        r = b[k]
        b[k] = b[p]
        b[p] = r
        for m in range(k + 1, n):
            с = A[m][k] / A[k][k]
            b[m] = b[m] - b[k] * с
            for i in range(k, n):
                A[m][i] = A[m][i] - A[k][i] * с
    x[n-1] = b[n-1] / A[n-1][n-1]
    for k in range(n - 1, -1, -1):
        s = 0
        for i in range(k + 1, n):
            s = s + A[k][i] * x[i]
        x[k] = (b[k] - s) / A[k][k]
    return x

def pog(c, x):
    p = c[n-1]
    for i in range(n - 2, -1, -1):
        p = p * x + c[i]
    return p

def calc_error(c):
    error = [f(x) - pog(c, x) for x in x_error_array]
    return error

def main():
    c = gauss(G, y)
    P = [pog(c, x) for x in x_array]
    function_result = [f(x) for x in x_error_array]
    polynom_result = [pog(c, x) for x in x_error_array]
    error = calc_error(c)
    print(error)

    plt.plot(function_result)
    plt.plot(polynom_result)
    plt.show()
    

if __name__ == '__main__':
	main()