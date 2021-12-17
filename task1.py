from typing import List, Tuple
import math


class Commands:
    """Команды программы"""
    get_box = "принять"
    remove_box = "выгрузить"


class Task1:
    """
        Идея следующая: создадим стек из команд 'выгрузить' ->
        сформируем лучшую последовательность без лищних деталей ->
        начинаем формировать исходную последовательность след образом:
        если пришел ящик не из стека, то брасаем на вход в любом случае,
        иначе смотрим насколько далеко лежит деталь в стеке и сравниваем с уже имеющийся длинной на ленте
        если последовательность уже больше (т.е. доставать имеющуюся ленту дороже чем стек), то кидаем на вход,
        иначе на выход. ->
        считаем ответ, выполняя задачи по сформированному списку.
        асимптотика O(n^2), где n - кол-во комманд
        т.к. стек порядка n и комманд порядка n

    """
    sequence = []

    def analyze(self, program: List[Tuple[str, int]]) -> int:
        """решение задачи"""
        stack = []
        for command in program:  # последовательность выгрузки
            current_command = command[0]
            current_box = command[1]
            if current_command == Commands.remove_box:
                stack.append(current_box)

        # формируемая последовательность ленты. индекс 0 - вход, len-1 - выход
        answer = 0
        for command in program:
            current_command = command[0]
            current_box = command[1]
            if current_command == Commands.get_box:
                if current_box not in stack:  # добавляем на вход ящик, который не выгрузят
                    self._push_forward_box(current_box)
                else:  # если ящик в списке выгрузки
                    len_in_stack = stack.index(current_box)  # кол-во элементов в стеке перед данным элементом
                    if len(self.sequence) > len_in_stack:
                        self._push_back_box(current_box)
                    else:
                        self._push_forward_box(current_box)
                answer += 1  # энергии на загрузку
            else:  # команда выгрузить
                boxes_move = len(self.sequence) - self.sequence.index(current_box) - 1
                answer += boxes_move * 2 + 1  # энергии на разгрузку данного ящика
                stack.remove(current_box)   # убираем из стека ненужное значение, оно больше не влияет на решение
                self.sequence.remove(current_box)

        self._free()
        return answer

    def _push_back_box(self, box):
        """добавляем ящик на выход"""
        self.sequence += [box]

    def _push_forward_box(self, box):
        """добавляем ящик на вход"""
        self.sequence = [box] + self.sequence

    def _free(self):
        """обнуляем окружение класса, для возможного повторного использования"""
        self.sequence = []


class Checker:
    """
    класс для наивного решения, перебрав все варианты
    используется для проверки ответов
    перебирает все возможные варианты
    время течет 2^n
    результат лежит в поле answer
    """
    answer = math.inf  # ищем наименьший ответ

    def naive_solution(self, program: List[Tuple[str, int]], current_sequence=[], current_answer=0) -> None:
        if len(program) == 0:  # нашли какое-то решение
            self.answer = min(self.answer, current_answer)
            return
        command = program[0]  # берем первую команду
        current_command = command[0]
        current_box = command[1]
        if current_command == Commands.get_box:
            new_sequence = current_sequence + [current_box]
            self.naive_solution(program[1:], new_sequence, current_answer + 1)
            new_sequence = [current_box] + current_sequence
            self.naive_solution(program[1:], new_sequence, current_answer + 1)
        else:  # выгружаем
            boxes_move = len(current_sequence) - current_sequence.index(current_box) - 1
            current_answer += boxes_move * 2 + 1  # энергии на разгрузку данного ящика
            current_sequence.remove(current_box)
            self.naive_solution(program[1:], current_sequence, current_answer)

