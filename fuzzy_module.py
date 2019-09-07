"""
Базовые алгоритмы, используемые при нечётких вычислениях
"""


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


def spike_function(value, lo, hi):
    """
    Функция задаёт функцию принадлежности в виде треугольника. lo и hi задают базовые вершины треугольника.
    Высшая точка задёся как hi/2

    :param value: текущее значение
    :param lo: левая вершина треугольника
    :param hi:  правая вершина треугольника
    :return: значение функции принадлежности для текущего value
    """

    value += (-lo)  # уменьшим текущее значение на значение минимального порога

    # преобразование для вершин в зависимости от того, где они расположены
    if lo < 0 and hi < 0:
        hi = -(hi - lo)
    elif lo < 0 and hi > 0:
        hi += lo
    elif lo > 0 and hi > 0:
        hi -= lo

    peak = hi * 0.5

    lo = 0.0

    if value < peak:
        return value / peak
    elif value > peak:
        return (hi - value) / peak

    return 1.0


def plate_function(value, lo, lo_plat, hi_plat, hi):
    """
    Функция задаёт функцию принадлежности в форме трапеции.

    :param value: текущее значение
    :param lo: левое нижнее значение трапеции
    :param lo_plat: левое верхнее значение трапеции
    :param hi_plat: правое верхнее значение трапеции
    :param hi: правое нижнее значение трапеции
    :return: значение функции приналжежности для текущего value
    """

    value += (-lo)

    if lo < 0.0:
        lo_plat += -lo
        hi_plat += -lo
        hi += -lo
        lo = 0
    else:
        lo_plat -= lo
        hi_plat -= lo
        hi = lo
        lo = 0

    upslope = 1.0 / (lo_plat - lo)
    downslope = 1.0 / (hi - hi_plat)

    if value < lo:
        return 0.0
    elif value > hi:
        return 1.0
    elif value >= lo_plat and value <= hi_plat:
        return 1.0
    elif value < lo_plat:
        return (value - lo) * upslope
    elif value > hi_plat:
        return (hi - value) * downslope
    return 0.0
