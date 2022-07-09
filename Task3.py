def appearance(intervals: dict):
    '''
    Функция, вычисляющая и возвращающая время совместного присутствия ученика и преподавателя на уроке
    :param intervals: Словарь, содержащий ключи 'pupil', 'tutor' и 'lesson', значения которых - временные диапазоны
    присутствия на уроке (для pupil и tutor) или временной интервалл урока (для lesson) в виде списков целых чисел
    (измеряется в секундах)

    :return: Время совместного присутствия ученика и преподавателя на уроке в секундах
    '''
    time = 0
    if intervals['lesson'][1] < intervals['lesson'][0]:
        raise ValueError

    for i in range(len(intervals['pupil'])):
        if i != 0 and intervals['pupil'][i] < intervals['pupil'][i-1]:
            raise ValueError
        if intervals['pupil'][i] < intervals['lesson'][0]:
            intervals['pupil'][i] = intervals['lesson'][0]
        elif intervals['pupil'][i] > intervals['lesson'][1]:
            intervals['pupil'][i] = intervals['lesson'][1]

    for i in range(len(intervals['tutor'])):
        if i != 0 and intervals['tutor'][i] < intervals['tutor'][i-1]:
            raise ValueError
        if intervals['tutor'][i] < intervals['lesson'][0]:
            intervals['tutor'][i] = intervals['lesson'][0]
        elif intervals['tutor'][i] > intervals['lesson'][1]:
            intervals['tutor'][i] = intervals['lesson'][1]

    for i in range(0, len(intervals['pupil']), 2):
        for j in range(0, len(intervals['tutor']), 2):
            if not(intervals['pupil'][i+1] < intervals['tutor'][j] or intervals['tutor'][j+1] < intervals['pupil'][i]):
                time += min(intervals['pupil'][i+1], intervals['tutor'][j+1]) - max(intervals['pupil'][i],
                                                                                    intervals['tutor'][j])
    return time
