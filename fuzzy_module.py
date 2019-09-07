"""
Базовые алгоритмы, используемые при нечётких вычислениях
"""

import numpy as np


def test_variables(a, b=0.0):
    if a > 1 or a < 0 or type(a) not in [float, int]:
        return -2
    if b > 1 or b < 0 or type(b) not in [float, int]:
        return -2
    return 0


# Операторы нечёткой логики

def maxmin_or(a, b):
    """ Максиминное нечёткое ИЛИ
        Осуществляется проверка значения переменной и её тип
        В случае ошибки возвращается значение -2
        """
    if test_variables(a, b) == 0:
        if a >= b:
            return a
        return b
    return -2


def maxmin_and(a, b):
    """ Максиминное нечёткое И
        Осуществляется проверка значения переменной и её тип
        В случае ошибки возвращается значение -2
        """

    if test_variables(a, b) == 0:
        if a < b:
            return a
        return b
    return -2


def maxmin_not(a):
    """
    Нечёткое НЕ
    Производится проверка переменной и её тип. Ошибка возвращает -2
    :param a:
    :return 1.0 - a:
    """
    if test_variables(a) == 0:
        return 1.0 - a
    return -2


def colormetr_or(a, b):
    """Колорметрическое или
       Осуществляется проверка значения переменной и её тип
       В случае ошибки возвращается значение -2
       """
    if test_variables(a, b) == 0:
        return a + b - a * b
    return -2


def colormetn_and(a, b):
    """Колорметрическое и
       Осуществляется проверка значения переменной и её тип
       В случае ошибки возвращается значение -2
       """
    if test_variables(a, b) == 0:
        return a * b
    return -2


# Описание функций принадлежности


def spike_function(value, lo, hi, cntr=None):
    """
    Функция задаёт функцию принадлежности в виде треугольника. lo и hi задают базовые вершины треугольника.
    использующиеся для задания неопределенностей типа: «приблизительно равно»,
     «среднее значение», «расположен в интервале», «подобен объекту», «похож на предмет» и т.п.
    Высшая точка задёся как hi - lo /2

    :param value: текущее значение
    :param lo: левая вершина треугольника
    :param hi:  правая вершина треугольника
    :param cntr: центр треугольника. Если не указан, значит треугольник равносторонний
    :return: значение функции принадлежности для текущего value
    """

    assert hi > lo

    if cntr is None:
        cntr = (hi + lo) * 0.5

    assert hi > cntr
    assert lo < cntr

    if value > hi or value < lo:
        return 0.0
    if value <= cntr:
        return (value - lo) / (cntr - lo)
    if value >= cntr:
        return (hi - value) / (hi - cntr)


def trimf(value, lo, hi, cntr=None):
    """
    Синоним для spike_function
    """

    return spike_function(value, lo, hi, cntr)


def plate_function(value, lo, lo_plat, hi_plat, hi):
    """
    Функция задаёт функцию принадлежности в форме трапеции.
    использующиеся для задания неопределенностей типа: «приблизительно равно», «среднее значение»,
    «расположен в интервале», «подобен объекту», «похож на предмет» и т.п.
    :param value: текущее значение
    :param lo: левое нижнее значение трапеции
    :param lo_plat: левое верхнее значение трапеции
    :param hi_plat: правое верхнее значение трапеции
    :param hi: правое нижнее значение трапеции
    :return: значение функции приналжежности для текущего value
    """

    assert lo <= lo_plat
    assert lo_plat <= hi_plat
    assert hi_plat <= hi

    if value < lo and value > hi:
        return 0.0
    if value >= lo_plat and value <= hi_plat:
        return 1.0
    if value > lo and value < lo_plat:
        return (value - lo) / (lo_plat - lo)
    if value > hi_plat and value < hi:
        return (hi - value) / (hi - hi_plat)

    return 0.0

def trapmf(value, lo, lo_plat, hi_plat, hi):
    """
    Синоним для plate_function
    """

    return plate_function(value, lo, lo_plat, hi_plat, hi)

def smf(value, lo, hi):
    """
    Квадратичный S-сплайн
    использующиеся для задания неопределенностей типа: «большое количество», «большое значение»,
     «значительная величина», «высокий уровень» и т.п.

    :param value: текущее значение
    :param lo: левая граница
    :param hi: правая граница
    :return: значение функции принадлежности
    """

    assert lo < hi

    cntr = (lo + hi) * 0.5

    if value <= lo:
        return 0.0
    if value >= hi:
        return 1.0
    if value <= cntr:
        return 2 * ((value - lo) ** 2) / (hi - lo) ** 2
    if value > cntr:
        return 1 - (2 * (value - lo) ** 2) / (hi - lo) ** 2


def zmf(value, lo, hi):
    """
    Квадратичный Z-сплайн
    использующиеся для задания неопределенностей типа: «большое количество», «большое значение»,
     «значительная величина», «высокий уровень» и т.п.
    :param value: текущее значение
    :param lo: левая граница
    :param hi: правая граница
    :return: значение функции принадлежности
    """

    assert lo < hi

    cntr = (lo + hi) * 0.5

    if value <= lo:
        return 1.0
    if value >= hi:
        return 0.0
    if value < cntr:
        return 1 - (2 * (value - lo) ** 2) / (hi - lo) ** 2
    if value > cntr:
        return 2 * ((value - lo) ** 2) / (hi - lo) ** 2

def gbellmf(value, concentration, slope, maximum):
    """
    Колоколообразная функция принадлежности
    использующиеся для задания неопределенностей типа: «приблизительно в пределах от и до», «примерно равно», «около»
    К данному типу функций принадлежности можно отнести целый класс кривых, которые по своей форме напоминают колокол,
    сглаженную трапецию или букву "П".
    :param value: текущее значение
    :param concentration: коэффициент концентрации функции принадлежности
    :param slope: коэффициент крутизны функции принадлежности
    :param maximum: координата максимума функции принадлежности
    :return: значение функции принадлежности
    """

    assert concentration != 0.0

    return 1 / (1 + abs((value - maximum) / concentration)** (2 * slope))

def gaussmf(value, concentration, maximum, gain=1.0):
    """
    Гауссовская функция принадлежности
    использующиеся для задания неопределенностей типа: «приблизительно в пределах от и до», «примерно равно», «около»
    К данному типу функций принадлежности можно отнести целый класс кривых, которые по своей форме напоминают колокол,
    сглаженную трапецию или букву "П".
    :param value: текущее значение
    :param concentration: коэффициент концентрации функции принадлежности
    :param maximum: координата максимума функции принадлежности
    :return:
    """

    assert maximum != 0.0

    expression = - ((value - concentration) ** 2) / (2 * (maximum ** 2))
    return np.exp(gain*expression)

def fuzzification(value, mfs):
    """
    фаззификатор для случая одной переменной
    :param value: вход
    :param mfs: список словарей функций принадлежности и параметров
    :return: список значений
    """

    a = []
    for func in mfs:
        if func["name"] == "gaussmf":
            x = gaussmf(float(value),
                        float(func["concentration"]),
                        float(func["maximum"]),
                        float(func["gain"]))
            a.append(x)

    return a

def simple_conclusuion(A, C):
    """
    Функция простого нечёткого вывода для случая плоских условий
    :param A: список значений первой функции принадлежности
    :param C: список значений выхода
    :return: чёткий вывод
    """

    assert len(A) == len(C)

    num = 0.0
    denum = 0.0

    for i in range(len(A)):
        num += A[i]*C[i]
        denum += A[i]

    if denum != 0:
        return num/denum
    else:
        return np.inf