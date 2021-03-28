import random as rand
import numpy as np
import math

def rand_int(min, max):
    return rand.randint(min,max)


def for_a(a, b):
    c = 0
    for i in range(len(a)):
        c += a[i] * b[i]
    return c


def dispersias(numb_of_y = 0):
    ret = 0
    for i in range(m):
        ret += (Y_lines[numb_of_y][i] - y_aver[numb_of_y])**2
    return round(ret/m, 2)


def betas(x_plans):
    suma = 0
    for i in range(4):
        suma += y_aver[i]*x_plans[i]
    return suma/4


x0_plan = [1, 1, 1, 1]
x1_plan = [-1, -1, 1, 1]
x2_plan = [-1, 1, -1, 1]
x3_plan = [-1, 1, 1, -1]

x1_min = -10
x2_min = 20
x3_min = 50
x1_max = 50
x2_max = 60
x3_max = 55
y_min = 200 +(x1_min+x2_min+x3_min)/3
y_max = 200 +(x1_max+x2_max+x3_max)/3
m = 10

X1 = [x1_min, x1_min, x1_max, x1_max]
X2 = [x2_min, x2_max, x2_min, x2_max]
X3 = [x3_min, x3_max, x3_max, x3_min]
Y_lines = [[], [], [], []]




for i in range(len(Y_lines)):
    for j in range(m):
        Y_lines[i].append(rand_int(y_min, y_max))
    
    
print("Матриця планування експерименту")
print(" Х1   Х2   X3    Y1    Y2    Y3    Y4    Y5    Y6    Y7    Y8    Y9    Y10 ")
for i in range(4):
    print(" {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}".format(
        X1[i], X2[i], X3[i], Y_lines[i][0], Y_lines[i][1], Y_lines[i][2], Y_lines[i][3],
        Y_lines[i][4], Y_lines[i][5], Y_lines[i][6], Y_lines[i][7], Y_lines[i][8],
        Y_lines[i][9]
    ))

y_aver = []
for i in range(4):
    y_aver.append(sum(Y_lines[i])/len (Y_lines[i]))

mx1 = sum(X1)/len(X1)
mx2 = sum(X2)/len(X2)
mx3 = sum(X3)/len(X3)
my = sum(y_aver)/len(y_aver)

a1 = for_a(X1, y_aver)/4
a2 = for_a(X2, y_aver)/4
a3 = for_a(X3, y_aver)/4
a11 = for_a(X1, X1)/4
a22 = for_a(X2, X2)/4
a33 = for_a(X3, X3)/4
a12 = a21 = for_a(X1, X2)/4
a13 = a31 = for_a(X1, X3)/4
a23 = a32 = for_a(X2, X3)/4


b0_chysel = np.matrix('{} {} {} {}; {} {} {} {}; {} {} {} {}; {} {} {} {}'.format(my, mx1, mx2, mx3,
                                                                                  a1, a11, a12, a13,
                                                                                  a2, a12, a22, a32,
                                                                                  a3, a13, a23, a33))

b1_chysel = np.matrix('{} {} {} {}; {} {} {} {}; {} {} {} {}; {} {} {} {}'.format(1, my, mx2, mx3,
                                                                                  mx1, a1, a12, a13,
                                                                                  mx2, a2, a22, a32,
                                                                                  mx3, a3, a23, a33))

b2_chysel = np.matrix('{} {} {} {}; {} {} {} {}; {} {} {} {}; {} {} {} {}'.format(1, mx1, my, mx3,
                                                                                  mx1, a11, a1, a13,
                                                                                  mx2, a12, a22, a32,
                                                                                  mx3, a13, a23, a33))

b3_chysel = np.matrix('{} {} {} {}; {} {} {} {}; {} {} {} {}; {} {} {} {}'.format(1, mx1, mx2, my,
                                                                                  mx1, a11, a12, a1,
                                                                                  mx2, a12, a22, a2,
                                                                                  mx3, a13, a23, a3))

b0123_znam = np.matrix('{} {} {} {}; {} {} {} {}; {} {} {} {}; {} {} {} {}'.format(1, mx1, mx2, mx3,
                                                                                  mx1, a11, a12, a13,
                                                                                  mx2, a12, a22, a32,
                                                                                  mx3, a13, a23, a33))

b0 = round(np.linalg.det(b0_chysel)/np.linalg.det(b0123_znam), 3)
b1 = round(np.linalg.det(b1_chysel)/np.linalg.det(b0123_znam), 3)
b2 = round(np.linalg.det(b2_chysel)/np.linalg.det(b0123_znam), 3)
b3 = round(np.linalg.det(b3_chysel)/np.linalg.det(b0123_znam), 3)

print("\nНормоване рівняння регресії: ")
print("y = {} + {}x1 + {}x2 + {}x3".format(b0, b1, b2, b3))
print("\nПеревірка однорідності дисперсії за критерієм Кохрена")
dispers = []
for i in range(4):
    dispers.append(dispersias(i))

Gp = max(dispers)/sum(dispers)
f1 = m - 1
f2 = 4
Gt = 0.4775
if Gp < Gt:
    print("Дисперсія однорідна")
else:
    print("Дисперсія не однорідна")
print("Перевірка пройшла успішно")
print("\nПеревірка однорідності дисперсії за критерієм Стьюдента")

sigma_b = sum(dispers)/len(dispers)
sigma_bs2 = sigma_b/(4*m)
sigma_bs = math.sqrt(sigma_bs2)

beta0 = betas(x0_plan)
beta1 = betas(x1_plan)
beta2 = betas(x2_plan)
beta3 = betas(x3_plan)

t0 = abs(beta0)/sigma_bs
t1 = abs(beta1)/sigma_bs
t2 = abs(beta2)/sigma_bs
t3 = abs(beta3)/sigma_bs

t = [t0, t1, t2, t3]
f3 = f1*f2  # 36
t_tabl = 2.03
print("t табличне = " + str(t_tabl))
print("t0 = {}\nt1 = {}\nt2 = {}\nt3 = {}".format(t0, t1, t2, t3))
print("\nЯкщо t0 або t1 або t2 або t3 менші ніж t табличне,\n"
      "то потрібно виключити з рівняння коефіцієнти b0, b1, b2 чи b3 відповідно\n")
d = 4
for i in range(len(t)):
    if t[i] < t_tabl:
        d -= 1
        print("b{} потрібно виключити з рівняння".format(i))
y_s = []
for i in range(m):
    y_s.append(b0)

print("Перевірка пройшла успішно")
print("\nПеревірка однорідності дисперсії за критерієм Фішера")

f4 = 4 - d
s2_ad = 0
for i in range(4):
    s2_ad += (y_s[i]-y_aver[i])**2
s2_ad = s2_ad*(m/(4-d))


Fp = s2_ad/sigma_bs2
ft = 4.05
if Fp < ft:
    print("Рівняння адекватне оригіналу")
else:
    print("Рівняння не адекватне оригіналу")
print("Перевірка пройшла успішно")
