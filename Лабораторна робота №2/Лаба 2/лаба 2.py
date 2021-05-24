import random as rand
import math
import numpy as np

def rand_int(min, max):
    return rand.randint(min,max)

#def romanovski():



y_min = 190
y_max = 290
x1_min = -10
x1_max = 50
x2_min = 20
x2_max = 60
m = 10
Rkr = 2.41
p = 0.95

x1_i = [-1, 1, -1]
x2_i = [-1, -1, 1]
mx1 = 0
mx2 = 0
list_y = [[], [], []]
list_y_average = []
dispersias = []
osn_vidh = 0
F_uv = []
sigma_uv = []
R_uv = []


def main(m):
    for i in range(len(list_y)):
        for j in range(m):
            list_y[i].append(rand_int(y_min, y_max))

    for i in list_y:
        list_y_average.append(sum(i)/len(i))

    for i in range(len(list_y)):
        a = 0
        for j in range(m):
            a += (list_y[i][j] - list_y_average[i])*(list_y[i][j] - list_y_average[i])
        dispersias.append(a/m)

    osn_vidh = math.sqrt((2*(2*m-2))/(m*(m-4)))
    for i in range(3):
        if dispersias[i-1] > dispersias[i]:
            F_uv.append(round(dispersias[i-1]/dispersias[i], 1))
        else:
            F_uv.append(round(dispersias[i]/dispersias[i-1], 1))
        sigma_uv.append(((m-2)/m)*F_uv[i])
        R_uv.append(round(abs(sigma_uv[i]-1)/osn_vidh, 1))

    print("Матриця планування експерименту")
    print(" Х1   Х2   Y1   Y2   Y3   Y4   Y5   Y6   Y7   Y8   Y9   Y10")
    for i in range(len(x1_i)):
        print(" {}   {}   {}  {}  {}  {}  {}  {}  {}  {}  {}  {}".format(
            x1_i[i], x2_i[i], list_y[i][0], list_y[i][1], list_y[i][2], list_y[i][3],
            list_y[i][4], list_y[i][5], list_y[i][6], list_y[i][7], list_y[i][8],
            list_y[i][9]
        ))
    print("\nДисперсії по рядках:")
    for i in dispersias:
        print(round(i,1))
    print("\nRkr", Rkr)
    print("\nFuv:  ")

    for i in F_uv:
        print(i)
    print()
    print("Перевірка дисперсії на однорідність:")

    if R_uv[0] < Rkr and R_uv[1] < Rkr and R_uv[2] < Rkr:
        print("{} < {}".format(R_uv[0], Rkr))
        print("{} < {}".format(R_uv[1], Rkr))
        print("{} < {}".format(R_uv[2], Rkr))
        print("\nДисперсія однорідна\n")
    else:
        print("Дисперсія неоднорідна")
        return main(m+1)
    mx1 = sum(x1_i)/len(x1_i)
    mx2 = sum(x2_i)/len(x2_i)
    my = sum(list_y_average)/len(list_y_average)

    a1 = (x1_i[0]*x1_i[0] + x1_i[1]*x1_i[1] + x1_i[2]*x1_i[2])/len(x1_i)
    a2 = (x1_i[0]*x2_i[0] + x1_i[1]*x2_i[1] + x1_i[2]*x2_i[2])/len(x1_i)
    a3 = (x2_i[0]*x2_i[0] + x2_i[1]*x2_i[1] + x2_i[2]*x2_i[2])/len(x1_i)
    a11 = (x1_i[0]*list_y_average[0] + x1_i[1]*list_y_average[1] + x1_i[2]*list_y_average[2])/len(x1_i)
    a22 = (x2_i[0]*list_y_average[0] + x2_i[1]*list_y_average[1] + x2_i[2]*list_y_average[2])/len(x1_i)


    b0_chysel = np.matrix('{} {} {}; {} {} {} ; {} {} {}'.format(my, mx1, mx2, a11, a1, a2, a22, a2, a3))
    b1_chysel = np.matrix('{} {} {}; {} {} {} ; {} {} {}'.format(1, my, mx2, mx1, a11, a2, mx2, a22, a3))
    b2_chysel = np.matrix('{} {} {}; {} {} {} ; {} {} {}'.format(1, mx1, my, mx1, a1, a11, mx2, a2, a22))

    b012_znam = np.matrix('{} {} {}; {} {} {} ; {} {} {}'.format(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3))
    b0 = round(np.linalg.det(b0_chysel)/np.linalg.det(b012_znam), 1)
    b1 = round(np.linalg.det(b1_chysel)/np.linalg.det(b012_znam), 1)
    b2 = round(np.linalg.det(b2_chysel)/np.linalg.det(b012_znam), 1)

    print("b0 = ", b0)
    print("b1 = ", b1)
    print("b2 = ", b2)
    print("\nНормоване рівняння регресії: ")
    print("y = {} + {}x1 + {}x2".format(b0, b1, b2))

    delta_x1 =abs(x1_max - x1_min)/2
    delta_x2 =abs(x2_max - x2_min)/2
    x10 = (x1_max + x1_min)/2
    x20 = (x2_max + x2_min)/2

    a0 = round(b0 - b1*(x10/delta_x1) - b2*(x20/delta_x2),1)
    a1 = round(b1/delta_x1, 1)
    a2 = round(b2/delta_x2, 1)

    print("\nНатуралізоване рівняння регресії:")
    print("y = {} + {}x1 + {}x2".format(a0, a1, a2))

if __name__ == '__main__':
    main(m)
#print(list_y_average)



