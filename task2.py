from typing import List


memory = {}  # лучшие варианты для каждого дня
variants_for_day = []  # суммарная награда полученная за уровень, отсчет уровней с 0ля
max_lvls = 0

def calculate(m: int, n: int, p: List[int]) -> int:
    """
    Идея следующая: динамика.
    Если есть некий день, то для него мы можем однозначно выбрать лучший.
    разбиваем данный временной промежуток на 2, считаем лучшую сумму для таких 2х отрезков (длиной не больше n)
    задача решена, когда посчитаем задачу для длины m
    Если m >> n то выбираем лучший вариант для n -> выбираем для m % n лучший вариант ->
    перемножаем на кол-во чиклов и суммируем с остатком
    используем меморизацию
    для каждого для находим лучший приз за O(n) таких дней n -> O(n^2)
    """
    global memory, variants_for_day, max_lvls
    max_lvls = n
    variants_for_day = [sum(p[:i+1]) for i in range(n)]  # все варианты призов за кол-во дней серии
    return dynamics(m - 1)


def dynamics(day: int):
    global memory, variants_for_day, max_lvls
    current_best_price = memory.get(day, None)
    if current_best_price is not None:  # динамика уже просчитана
        return current_best_price
    if day < 0:  # ситуация, когда вышли за границу
        return 0
    if day == 0:  # первый день серии (база) - максимум можно набрать - за первый уровень
        memory[0] = variants_for_day[0]
        return memory[0]
    max_price = -1

    for i in range(day):
        v1 = dynamics(i)
        v2 = dynamics(day - i - 2)
        if day >= max_lvls:  # если не можем набрать серию из уровня для этого дня, тогда это просто сумма
            curr_price = v1 + v2
        else:  # иначе, это либо некоторая сумма, либо уровень на текущий день
            curr_price = max(v1 + v2, variants_for_day[day])
        max_price = max(max_price, curr_price)

    memory[day] = max_price
    return memory[day]
