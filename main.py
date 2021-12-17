import math

import data
from task1 import Task1, Checker
from task2 import Task2
from data import *

if __name__ == '__main__':
    """Тесты"""
    i = 1
    print("Тесты по первой задаче с проверкой")
    for test in data.data_for_task1:
        task1 = Task1()
        checker = Checker()
        answer = task1.analyze(test)
        checker.naive_solution(test, [], 0)
        output = 'правильно' if answer == checker.answer else 'неправильно'
        print("тест" + str(i) + ": " + output)
        i += 1
        if output == 'правильно':
            print("ответ: " + str(answer))

    i = 1
    print("\n\nТесты по второй задаче")
    for test in data.data_for_task2:
        task2 = Task2()
        answer = task2.calculate(test[0], test[1], test[2])
        print("тест" + str(i) + ": " + str(answer))
        i += 1
