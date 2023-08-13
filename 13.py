import random

n = int(input("Введите n: "))
m = int(input("Введите m: "))

matrix_1 = []
matrix_2 = []

for i in range(n):
    row = []
    for j in range(m):
        num = random.randint(-100, 100)
        row.append(num)
    matrix_1.append(row)

print(matrix_1)

for i in range(n):
    row = []
    for j in range(m):
        num = random.randint(-100, 100)
        row.append(num)
    matrix_2.append(row)

print(matrix_2)

matrix_3 = []

for i in range (n):
    row = []
    for j in range (m):
        num = matrix_1[i][j] + matrix_2[i][j]
        row.append(num)
    matrix_3.append(row)

print(matrix_3)

