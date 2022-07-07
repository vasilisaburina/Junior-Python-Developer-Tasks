def task(array: str):
    '''
    Функция, находящая индекс первого нуля в строке, состоящей из подряд идущих единиц и нулей
    
    :param array: Строка, состоящая из подряд идущих единиц и нулей соответственно
    :return: Индекс первого нуля
    '''
    left = 0
    right = len(array)
    middle = (left + right) // 2
    while left <= right:
        if array[middle] != '0' and array[middle] != '1':
            raise ValueError
        if array[middle] == '0' and array[middle-1] == '1':
            return middle
        if array[middle] == '0':
            right = middle
        else:
            left = middle
        middle = (left + right) // 2
