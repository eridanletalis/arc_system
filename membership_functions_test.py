"""
Функции принадлежности для алгоритмов управления печи
"""

import fuzzy_module as fuzzy
import matplotlib.pyplot as plt

def test_1(value):
    lo = -5.0
    lo_plate = 0.0
    hi_plate = 5.0
    hi = 10

    return fuzzy.spike_function(value, lo, hi)
    # return fuzzy.plate_function(value, lo, lo_plate, hi_plate, hi)

def test_2(value):
    lo = -5
    lo_plate = 0.0
    hi_plate = 5.0
    hi = 5

    return fuzzy.spike_function(value, lo, hi)
    # return fuzzy.plate_function(value, lo, lo_plate, hi_plate, hi)

def test_3(value):
    lo = -15
    lo_plate = 0.0
    hi_plate = 5.0
    hi = 15

    return fuzzy.plate_function(value, lo, lo_plate, hi_plate, hi)

def test_4(value):
    lo = -5
    cntr = 4
    hi = 5

    return fuzzy.spike_function(value, lo, hi, cntr)

x = []
y1 = []
y2 = []
y3 = []
y4 = []

for i in range(-200, 200):
    x.append(i/10)
    y1.append(test_1(i/10))
    y2.append(test_2(i / 10))
    y3.append(test_3(i / 10))
    y4.append(test_4(i / 10))

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.show()