from math import sqrt
from matplotlib import pyplot as plt

d = 2
q = -2.57
eps = 1e-4

w_min = 0.2
w_max = 2
h = 0.2

A = [[q, 1, 0, 0, 0],
    [1, -2, 1, 0, 0],
    [0, 1, -2, 1, 0],
    [0, 0, 1, -2, 1],
    [0, 0, 0, 1, q]]
    
b = [0, d, d, d, 0]

def main():
  n = len(A)
  w = w_min
  
  w_array = []
  iteration_array = []
  
  while w < w_max:
    print(w)
    stop = False
    x_curr = [0 for _ in range(n)]
    iteration = 0
    while not stop:
      x_prev = [x for x in x_curr]
      for i in range(n):
        sum1 = sum(-A[i][j] / A[i][i] * x_curr[j] for j in range(i))
        sum2 = sum(-A[i][j] / A[i][i] * x_prev[j] for j in range(i+1, n))
        c = b[i] / A[i][i]
        x = sum1 + sum2 + c
        x_new = w * x + (1 - w) * x_prev[i]
        x_curr[i] = x_new
          
      error = sqrt(sum((x_curr[i] - x_prev[i]) ** 2 for i in range(n)))
      stop = error <= eps
      iteration += 1
    
    w_array.append(w)
    iteration_array.append(iteration)
    plt.plot(w_array, iteration_array, color='green', marker='o', linestyle='solid')
    
    w = round(w + h, 2)
    
  print(x_curr)
  plt.show()

if __name__ == '__main__':
	main()