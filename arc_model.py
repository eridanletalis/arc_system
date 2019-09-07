#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
R1=10;R2=20;L=0.02;C=0.00005;E=100;tm=0.02; # параметры электрической цепи

L1 = 0.005
L2 = 0.0045
L3 = 0.0055
r1 = 12.15678
r2 = 18.1867489
r3 = 09.9878
alpha = 1
beta = 0.00001
teta = 0.25

# def g1()



def f(y, t):#  дифференциальное уравнение переходного процесса.
                y1,y2 = y
                return [y2,-((L+R1*R2*C)/(R2*L*C))*y2-((R1+R2)/(R2*L*C))*y1+E/(L*C)]
t = np.linspace(0,tm,1000)
y0 = [E,0]#начальные условия
z = odeint(f, y0, t)#решение  дифференциального уравнения
y1=z[:,0] # вектор значений решения
y2=100*(C*z[:,1]+y1/R2)
y3=100*C*z[:,1]
y4=100*y1/R2
plt.title('Напряжение на конденсаторе и токи  при замыкании цепи', size=12)
plt.plot(t*1000,y1,linewidth=2, label=' Uc(t)')
plt.plot(t*1000,y2,linewidth=2, label=' i1(t)*100')
plt.plot(t*1000,y3,linewidth=2, label='i3(t)*100')
plt.plot(t*1000,y4,linewidth=2, label=' i2*100')
plt.ylabel("Uc(t),i1(t),i2(t),i3(t)")
plt.xlabel("t*1000")
plt.legend(loc='best')
plt.grid(True)
plt.show()