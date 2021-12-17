from typing import List


class Task2:
    """
        Идея следующая: динамика.
        Если есть некий день, то для него мы можем однозначно выбрать лучший.
        разбиваем данный временной промежуток на 2, считаем лучшую сумму для таких 2х отрезков (длиной не больше n)
        задача решена, когда посчитаем задачу для длины m
        используем меморизацию, чтобы увеличить скорость работы
        для каждого для находим лучший приз за O(n) таких дней n -> O(n^2)
    """
    memory = {}  # лучшие варианты для каждого дня
    variants_for_day = []  # суммарная награда полученная за уровень, отсчет уровней с 0ля
    max_lvls = 0

    def calculate(self, m: int, n: int, p: List[int]) -> int:
        """инициализация данных и вызов динамики"""
        self.max_lvls = n
        self.memory = {}
        self.variants_for_day = [sum(p[:i+1]) for i in range(n)]  # все варианты призов за кол-во дней серии
        return self._dynamics(m - 1)

    def _dynamics(self, day: int):
        """динамический подсчет лучшего результата для некого дня"""
        current_best_price = self.memory.get(day, None)
        if current_best_price is not None:  # динамика уже просчитана
            return current_best_price
        if day < 0:  # ситуация, когда вышли за границу
            return 0
        if day == 0:  # первый день серии (база) - максимум можно набрать - за первый уровень
            self.memory[0] = self.variants_for_day[0]
            return self.memory[0]
        max_price = -1

        for i in range(day):  # перебираем длину отрезков
            v1 = self._dynamics(i)
            v2 = self._dynamics(day - i - 2)  # -1 из-за потери дня при обнулении уровня, -1 при переходе к индексу
            if day >= self.max_lvls:  # если не можем набрать серию из уровня для этого дня, тогда это просто сумма
                curr_price = v1 + v2
            else:  # иначе, это либо некоторая сумма, либо уровень на текущий день
                curr_price = max(v1 + v2, self.variants_for_day[day])
            max_price = max(max_price, curr_price)

        self.memory[day] = max_price
        return self.memory[day]
