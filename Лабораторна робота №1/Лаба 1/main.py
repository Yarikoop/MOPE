import random as rand
import timeit

def rand_a():
    return rand.randint(0, 20)
start = timeit.default_timer()

def rand_x(sp):
    for i in range(8):
        sp.append(rand.randint(0, 20))

def define_x0(sp):
    return (max(sp)+min(sp))/2

def define_y(sp_1, sp_2, sp_3):
    for i in range(8):
        y = a0 + a1*sp_1[i] + a2*sp_2[i] + a3*sp_3[i]
        sp_Y.append(y)
        
def normal(x, x0, dx):
    return ((x - x0))/dx

def opt(sp_y):
    global ind
    a = sum(sp_y)/len(sp_y)
    for i in sorted(sp_y):
        if a < i:
            ind = i
            return i


ind = 0
a0 = rand_a()
a1 = rand_a()
a2 = rand_a()
a3 = rand_a()
sp_X1 = []
sp_X2 = []
sp_X3 = []  #фактори експерименту
sp_Y = []
sp_X1_norm = []
sp_X2_norm = []
sp_X3_norm = []

rand_x(sp_X1)
rand_x(sp_X2)
rand_x(sp_X3)

x_01 = define_x0(sp_X1)
x_02 = define_x0(sp_X2)
x_03 = define_x0(sp_X3)
define_y(sp_X1, sp_X2, sp_X3)
Y_et = a0 + x_01*a1 + a2*x_02 + a3*x_03
print(sp_X1)
dx1 = x_01 - min(sp_X1)
dx2 = x_01 - min(sp_X2)
dx3 = x_01 - min(sp_X3)
for i in range(8):
    sp_X1_norm.append(normal(sp_X1[i], x_01, dx1))
    sp_X2_norm.append(normal(sp_X2[i], x_02, dx2))
    sp_X3_norm.append(normal(sp_X3[i], x_03, dx3))


Optim_Y = opt(sp_Y)
index = sp_Y.index(ind)
opt_x = [sp_X1[index], sp_X2[index], sp_X3[index]]
stop = timeit.default_timer()
print("N   X1   X2   X3     Y        XH1    XH2    XH3")
for i in range(8):
    print(f"{i+1:^1} |{sp_X1[i]:^4} {sp_X2[i]:^4} {sp_X3[i]:^4} |"
          f" {sp_Y[i]:^5} || {'%.2f' %sp_X1_norm[i]:^5}  {'%.2f' %sp_X2_norm[i]:^5}  {'%.2f' %sp_X3_norm[i]:^5} |")

print(f"\nX0| {x_01:^4} {x_02:^4} {x_03:^4}|")
print(f"dx| {dx1:^4} {dx2:^4} {dx3:^4}|")
print(f"Function: y = {a0} + {a1}x1 + {a2}x2 + {a3}x3")
print("Y_ет =", Y_et)
print("Optimal point :  Y({0}, {1}, {2}) = {3}".format(*opt_x, "%.1f" % Optim_Y))
print("Program execution time: ", stop-start)