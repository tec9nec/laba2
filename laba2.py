import numpy as np
import matplotlib.pyplot as plt


N, K = int(input('введите число N: ')), int(input('введите число K: '))
variant = int(input('Заполнение матрицы:\n1. рандомно\n2. из файла\nвведите вариант: '))

if variant == 1:
    A = np.random.randint(-10, 11, (N, N))
elif variant == 2:
    file = open('22.txt', 'r')
    A = np.loadtxt(file, dtype=int, max_rows=N, usecols=range(N))
    file.close()
else:
    print("Некорректный выбор.")
    exit()

print(f"Матрица A:\n{A}")

F = A.copy()
variable = 0
variable2 = 1
for i in range(N//2, N):
    for j in range(N//2):
        if j % 2 == 1 and F[i][j] > K:
            variable += 1
        elif j % 2 == 1:
            variable2 *= F[i][j]

if variable > variable2:
    for i in range(N//2):
        for j in range(N//2):
            F[i][j], F[N - i - 1][j] = F[N - i - 1][j], F[i][j]
else:
    for j in range(N//2):
        for i in range(N//2, N):
            F[i][j], F[j][i] = F[j][i], F[i][j]

print(f"Матрица F:\n{F}")

opr = round(np.linalg.det(A)) # определитель
sum_diag = np.trace(F) + np.trace(np.fliplr(F)) # сумма элементов диагоналей

if opr > sum_diag:
    AT = A.transpose()
    itog = np.dot(A, AT) - K * np.linalg.inv(F) # dot - умножение, linalg - степень 
    print(f"результат (1 вариант):\n{itog}")
else:
    FT = F.transpose()
    G = np.tril(A)
    itog = (np.linalg.inv(A) + G - FT) * K
    print(f"результат (2 вариант):\n{itog}")

# графики
x = np.linspace(-10, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")
plt.plot(x, y3, label="tan(x)", alpha=1)
plt.legend()
plt.grid()
plt.title("Графики функций")
plt.show()
