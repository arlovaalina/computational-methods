from math import exp, sin, cos
from scipy.special import expi
from matplotlib import pyplot as plt

a = 4
b = 7

h1 = 0.2
h2 = 0.1
h3 = 0.05

precision1 = 0.1
precision2 = 0.01
precision3 = 0.001

_f = lambda x : exp(x) / (x ** 3) - (sin(x) ** 3)
_x = lambda j : a + (j - 1) * (b - a) / 20

_first_derivative_precise = lambda x : (exp(x) * (x - 3) / (x ** 4)) - (3 * (sin(x) ** 2) * cos(x))
_second_derivative_precise = lambda x : (exp(x) * (x - 3) * (x - 4) / (x ** 5)) - (3 * sin(x) * ((2 * (cos(x) ** 2)) - (sin(x) ** 2)))
_integral_precise = 6.118
# _integral_precise = lambda x : (expi(x) - exp(x) * (x + 1) / x ** 2) / 2 - (cos(x) + (cos(x) ** 3) / 3)

j_min = 1
j_max = 21

def first_derivative(x, h, f):
  x1 = x - h
  x3 = x + h
  deriviative = (f(x3) - f(x1)) / (2 * h)
  return deriviative

def second_derivative(x, h, f):
  x1 = x - h
  x3 = x + h
  deriviative = (f(x1) - 2 * f(x) + f(x3)) / (h ** 2)
  return deriviative

def middle(m, f):
  h = (b - a) / m
  x_array = [a + h * i for i in range(0, m + 1)]
  x_middle = [(x_array[i] + x_array[i + 1]) / 2 for i in range(0, len(x_array) - 1)]
  result = h * sum([f(x) for x in x_middle])
  return result

def trapezium(m, f):
  h = (b - a) / m
  x_array = [a + h * i for i in range(0, m + 1)]
  result = h * sum([(f(x_array[i]) + f(x_array[i + 1])) / 2 for i in range(0, len(x_array) - 1)])
  return result

def integral(precision, f):
  m_array = []
  precision_array = []
  m = 2
  stop = False
  while not stop:
    integral_middle = middle(m, f)
    integral_trapezium = trapezium(m, f)
    error = abs(integral_middle - integral_trapezium)
    stop = error < precision
    m_array.append(m)
    precision_array.append(error)
    m = m * 2
  return {
    'integral': (integral_trapezium + 2 * integral_middle) / 3,
    'm': m_array,
    'precision': precision_array
  }

def main():
  x_array = [_x(j) for j in range(j_min, j_max + 1)]

  first_precise = [_first_derivative_precise(x) for x in x_array]
  first_h1 = [first_derivative(x, h1, _f) for x in x_array]
  first_h2 = [first_derivative(x, h2, _f) for x in x_array]
  first_h3 = [first_derivative(x, h3, _f) for x in x_array]

  second_precise = [_second_derivative_precise(x) for x in x_array]
  second_h1 = [second_derivative(x, h1, _f) for x in x_array]
  second_h2 = [second_derivative(x, h2, _f) for x in x_array]
  second_h3 = [second_derivative(x, h3, _f) for x in x_array]

  integral_precision1 = integral(precision1, _f)
  integral_precision2 = integral(precision2, _f)
  integral_precision3 = integral(precision3, _f)

  f = [_f(x) for x in x_array]

  plt.figure("First Derivative")
  plt.plot(first_precise, color="green")
  plt.plot(first_h1, color="red")
  plt.plot(first_h2, color="yellow")
  plt.plot(first_h3, color="orange")

  plt.figure("Second Derivative")
  plt.plot(second_precise, color="green")
  plt.plot(second_h1, color="red")
  plt.plot(second_h2, color="yellow")
  plt.plot(second_h3, color="orange")

  plt.figure("Integral Precision 0.1")
  plt.plot(integral_precision1['precision'], integral_precision1['m'], color="red")

  plt.figure("Integral Precision 0.01")
  plt.plot(integral_precision2['precision'], integral_precision2['m'], color="green")

  plt.figure("Integral Precision 0.001")
  plt.plot(integral_precision3['precision'], integral_precision3['m'], color="orange")

  plt.show()

if __name__ == '__main__':
	main()
