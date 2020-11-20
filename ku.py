import matplotlib.pyplot as plt
import numpy as np
from beautifultable import BeautifulTable
from scipy import interpolate

m = []
f = open(input("Введите имя файла: ") + ".txt")
for i in f:
    m += [(float(i))]


class AverageValue:
    def __init__(self, me):
        self.m = me

    def rez(self):
        my_sum = 0
        my_len = 0
        for ii in self.m:
            my_sum += ii
            my_len += 1
        return round(my_sum / my_len, 3)


# Интерполяция
x = np.arange(0, len(m))
f = interpolate.interp1d(x, m, kind='quadratic')
x_new = np.arange(0, len(m) - 1, 0.1)
y_new = f(x_new)
plt.plot(x_new, y_new)

# Поиск мин и макс
min_x = 0
max_x = 0
min_y = 0
max_y = 0
for i in x_new:
    if f(i) > max_y:
        max_y = f(i)
        max_x = i
    if f(i) < min_y:
        min_y = f(i)
        min_x = i
ex_x = [min_x, max_x]
ex_y = [min_y, max_y]
plt.plot(ex_x, ex_y, "X")
plt.show()

# Поиск всех средних значений
t = AverageValue(m)
ari = t.rez()
print("Среднее арифметическое: " + str(ari))

count = 0
geo = 1
for i in m:
    if i > 0:
        count += 1

if count != len(m):
    print("Невозможно получить среднее геометрическое, поскольку не все элементы положительные")
else:
    for i in m:
        geo *= i
    res = round(geo**(1/len(m)), 3)
    print("Среднее геометрическое: " + str(res))

m2 = [i**2 for i in m]
quad = (sum(m2)/len(m2))**(1/2)
print("Среднее квадратическое: " + str(round(quad, 3)))

obr = []
for i in range(len(m)):
    obr.append(1/m[i])
harm = 1/(len(m) * sum(obr))
print("Среднее гармоническое: " + str(round(harm, 3)))

# Максимальное отклонение от среднего
otk = []
for i in m:
    otk.append(abs(i - t.rez()))
print("Максимальное отклонение от среднего арифметического: " + str(max(otk)))

# Минимальное убывание функции
muf = []
for i in range(len(m) - 1):
    if m[i] > m[i + 1]:
        muf.append(m[i] - m[i + 1])

print("Минимальное убывание функции: " + str(min(muf)))

# Таблица
table = BeautifulTable()
table.column_headers = ["№", "Значение"]
for i in x:
    table.append_row([i, m[i]])
print(table)
