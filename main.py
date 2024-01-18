import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

def e(i, x):
   return max(0, 1 - abs((x - i * h) / h))

def de(i, x):
    if h * (i - 1) <= x <= h * i:
        return 1 / h
    if h * i <= x <= h * (i + 1):
        return -1 / h
    return 0

def k(x):
    if 0 <= x <= 1:
        return 1
    if 1 < x <= 2:
        return 2 * x
    else:
        raise Exception("x must be in range [0, 2]")
    
def f(x):
    return 100 * x
    
def B(i, j, start, end):
    return quad(lambda x: k(x) * de(i, x) * de(j, x), start, end)[0] - k(0) * e(i, 0) * e(j, 0)

def L(i, start, end):
    return quad(lambda x: f(x) * e(i, x), start, end)[0] - 20 * k(0) * e(i, 0)

def A_matrix():
    matrix = np.zeros((n + 1, n + 1))
    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1:
                continue
            if abs(i - j) == 1:
                start = 2. * min(i, j) / n
                end = 2. * max(i, j) / n
            else:
                start = 2. * max(0, (i - 1) / n)
                end = 2. * min(1, (i + 1) / n)
            matrix[i][j] = B(i, j, start, end)

    for i in range(n + 1):
        matrix[n][i] = 0.
        matrix[i][n] = 0.
        
    matrix[n][n] = 1.

    return matrix

def B_matrix():
    vector = np.zeros(n + 1)

    for i in range(n):
        start = 2. * max(0, (i - 1) / n)
        end = 2. * min(1, (i + 1) / n)

        vector[i] = L(i, start, end)

    vector[n] = 0.

    return vector

def solve(n):
    global h
    h = 2 / n

    a = A_matrix()
    b = B_matrix()

    x = [h * i for i in range(n + 1)]
    y = np.linalg.solve(a, b)

    return x, y

def show(x, y, n):
    plt.style.use('bmh')
    plt.title('Heat transfer equation solution using FEM')
    plt.xlabel(f'n = {n}')
    plt.plot(x, y, color='blue', label='u(x)')
    plt.show()

def main():
    global n
    n = int(input("Enter the number of elements: "))
    
    if n <= 2:
        raise Exception("n must be greater than 2")
    
    x, y = solve(n)
    show(x, y, n)

if __name__ == "__main__":
    main()