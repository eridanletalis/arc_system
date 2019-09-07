"""
Функции принадлежности для алгоритмов управления печи
"""

import fuzzy_module as fuzzy
import matplotlib.pyplot as plt

def ngeative(value):
    concentration = -1.0
    maximum = 0.2
    gain = 1.0

    return fuzzy.gaussmf(value, concentration , maximum, gain)

def nzero(value):
    concentration = 0
    maximum = 0.5
    gain = 1.0

    return fuzzy.gaussmf(value, concentration , maximum, gain)

def positive(value):
    concentration = 1
    maximum = 0.2
    gain = 1.0

    return fuzzy.gaussmf(value, concentration , maximum, gain)

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

for i in range(-100, 100):
    x.append(i/100)
    y1.append(ngeative(i/100))
    y2.append(nzero(i / 100))
    y3.append(positive(i / 100))
    y4.append(test_4(i / 100))

# plt.plot(x,y1, label="N")
# plt.plot(x,y2, label="NZ")
# plt.plot(x,y3, label="P")
# plt.plot(x,y4)
# plt.legend()
# plt.show()


mf1 = {"name": "gaussmf", "concentration":-1.0, "maximum":0.2, "gain": 1.0}
mf2 = {"name": "gaussmf", "concentration":0, "maximum":0.5, "gain": 1.0}
mf3 = {"name": "gaussmf", "concentration":1.0, "maximum":0.2, "gain": 1.0}

mf_s = [mf1, mf2, mf3]
mf_c = [1, 0, -1]
mf_value = fuzzy.fuzzification(0.7, mf_s)
concl = fuzzy.simple_conclusuion(mf_value, mf_c)
print(concl)

y = []
for i in range(-100, 100):
    y.append(fuzzy.simple_conclusuion(fuzzy.fuzzification(i/100, mf_s), mf_c))

plt.plot(x,y)
plt.show()