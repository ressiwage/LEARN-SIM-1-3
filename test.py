# Ниже код, который для некоторого многомерного массива возвращает айдишники форматов для каждой ячейки.
# Форматы - объекты, описывающие визуальное представление ячейки.
# Формула+формат - по сути, утверждение в духе "покрась красным цветом все ячейки с плохими значениями"
#
# Передаваемые функции - внутренние(генерятся автоматически). Считаем, что не опасные.
# Возвращают всегда число. Состоят из базовой арифметики, тернарников и возможно базовых математических функций.
#
# Считаем, что реальный массив больше, чем в примере и с бОльшим числом измерений - вполне может быть порядка гигабайта.
# При этом форматы не обязательно существуют для всех ячеек - могут быть большие пустые пространства.
#
# Порядок форматов имеет значение. Считаем, [1, 2, 3] не равно [3, 2, 1]
# (Есть исключения, но опущено для простоты)
#
#
# Вопросы:
# 1) Какие могут быть ускорения в рамках самого кода(если не трогать входные и выходные данные)
# 2) Какие могут быть ускорения со стороны входных данных?
# 3) Какие могут быть ускорения со стороны выхода(текущий формат обоснован передачей в json)?

import itertools
import time
from collections import defaultdict
from pprint import pprint

import numpy as np


class FormatEvaluator:

    def __init__(self, formulae: dict):
        self.formulae = formulae

    def slice_calc(self,
                   array: np.ndarray,
                   coordinates: list[list[int]],
                   ):  #  -> dict[str, list[int]]

        result = defaultdict(list)

        for dim_index, functions in self.formulae.items():
            for function, dest in functions:

                slices = coordinates.copy()

                if dest not in slices[dim_index]:
                    continue

                slices[dim_index] = [dest]

                for co in itertools.product(*slices):
                    format_id = int(function(array, *co))
                    result[co].append(format_id)

        return {','.join(map(str, co)): v for co, v in result.items()}


def main():

    def func1_1(arr, x1, x2, x3):
        return 50 if arr[x1, x2, 0] + arr[x1, x2, 1] > arr[x1, x2, 2] else 0
    dest1_1 = 5

    def func1_2(arr, x1, x2, x3):
        return 100 if arr[x1, x2, 3] > arr[x1, x2, 4] else 200
    dest1_2 = 5

    def func2_1(arr, x1, x2, x3):
        return 300 if arr[0, x2, x3] < arr[1, x2, x3] else 400
    dest2_1 = 3

    formulae = {
        2: [(func1_1, dest1_1), (func1_2, dest1_2), ],
        0: [(func2_1, dest2_1)],
    }

    ###################################

    evaluator = FormatEvaluator(formulae)

    array = np.zeros((10, 2, 10), dtype=np.float64)
    np.random.seed(123)
    array[...] = np.random.random(array.shape)

    t1 = time.time()

    full_coords = [list(range(size)) for size in array.shape]
    result = evaluator.slice_calc(array, full_coords)

    t2 = time.time()
    print(f'time: {t2-t1: 0.6f}')

    pprint(result)


if __name__ == '__main__':
    main()
