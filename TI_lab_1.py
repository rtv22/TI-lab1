import numpy

import random


Matrix = numpy.array([[18, 13, 15],
                    [0, 13, 16],
                    [1, 17, 9]])

count = 1
A = 0
B = 0

x = numpy.zeros(3)
y = numpy.zeros(3)

sum_A = numpy.zeros(3)
sum_B = numpy.zeros(3)

max_v_min = numpy.inf * -1
min_v_max = numpy.inf

e = numpy.inf

while e > 0.1:
    A_list = []
    B_list = []

    x[A] += 1
    y[B] += 1

    sum_A = sum_A + Matrix[:, B]

    max_A = max(sum_A)

    for i in range(3):
        if sum_A[i] == max_A:
            A_list.append(i)

    v_max = max_A / count

    if v_max < min_v_max:
        min_v_max = v_max

    sum_B = sum_B + Matrix[A, :]
    min_B = min(sum_B)

    for j in range(3):
        if sum_B[j] == min_B:
            B_list.append(j)

    v_min = min_B / count

    if v_min > max_v_min:
        max_v_min = v_min

    e = min_v_max - max_v_min

    print(f'''
    ______________________
    # {count}
    Выбор игрока А: {A + 1}
    Выбор игрока B: {B + 1}

    Выигрыш игрока А: {sum_A}
    Проигрыш игрока B: {sum_B}

    Верхняя оценка игры v_max: {v_max}
    Нижняя оценка игры v_min: {v_min}

    Погрешность e: {e}''')

    A = random.choice(A_list)
    B = random.choice(B_list)

    count += 1
count -= 1

print("Оптимальная смешанная стратегия игрока A: " f'{x / count}')
print("Оптимальная смешанная стратегия игрока B: " f'{ y / count}')