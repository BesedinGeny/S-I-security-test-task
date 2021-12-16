from typing import List, Tuple


class Commands:
    """Команды программы"""
    get_box = "принять"
    remove_box = "выгрузить"


def analyze(program: List[Tuple[str, int]]) -> int:
    """
        Идея следующая: создадим стек из команд 'выгрузить' ->
        сформируем лучшую последовательность без лищних деталей ->
        начинаем формировать исходную последовательность след образом:
        если пришел ящик не из стека, то брасаем на вход в любом случае,
        иначе смотрим насколько далеко лежит деталь в стеке и сравниваем с уже имеющийся длинной на ленте
        если последовательность уже больше (т.е. доставать имеющуюся ленту дороже чем стек), то кидаем на вход,
        иначе на выход. ->
        считаем ответ, выполняя задачи по сформированному списку

    """
    # TODO: добавить функции добавления в начало и в конец ленты ящика

    stack = []
    for command in program:
        current_command = command[0]
        current_box = command[1]
        if current_command == Commands.remove_box:
            stack.append(current_box)

    sequence = []  # формируемая последовательность ленты. индекс 0 - вход, len-1 - выход
    answer = 0
    for command in program:
        current_command = command[0]
        current_box = command[1]
        if current_command == Commands.get_box:
            if current_box not in stack:  # добавляем на вход ящик, который не выгрузят
                sequence = [current_box] + sequence
            else:  # если ящик в списке выгрузки
                len_in_stack = stack.index(current_box)  # кол-во элементов в стеке перед данным элементом
                if len(sequence) > len_in_stack:
                    sequence += [current_box]
                else:
                    sequence = [current_box] + sequence
                stack.remove(current_box)  # убираем из стека ненужное значение, оно больше не влияет на решение
            answer += 1  # энергии на загрузку
        else:  # команда выгрузить. тут надо просчитать ответ
            boxes_move = len(sequence) - sequence.index(current_box) - 1
            answer += boxes_move * 2 + 1  # энергии на разгрузку данного ящика
            sequence.remove(current_box)
    return answer
