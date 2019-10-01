from math import exp, sin, cos
from matplotlib import pyplot as plt

a = 4
b = 7

m = 100
eps = 1e-4

x0 = 3
x1 = 4.5

_f = lambda x : exp(x) / (x ** 3) - (sin(x) ** 3) - 2

def wegstein(f):
  x_array = [x0, x1]
  i = 2
  stop = False
  while not stop:
    d = x_array[i - 1] - x_array[i - 2]
    x_new = x_array[i - 1] - f(x_array[i - 1]) * d / (f(x_array[i - 1]) - f(x_array[i - 2]))
    x_array.append(x_new)
    error = abs(x_array[i - 1] - x_new)
    i = i + 1
    stop = i > m or error < eps
  return x_new

def main():
  result = wegstein(_f)
  print(result)

if __name__ == '__main__':
	main()
