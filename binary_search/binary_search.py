# реализация функции бинарного поиска по отсортированному массиву


def search(lst, item):
    start = 0
    end = len(lst) - 1
    index = None
    while start <= end:
        middle = int((end + start) / 2)
        if lst[middle] == item:
            index = middle
            break
        elif lst[middle] > item:
            end = middle - 1
        elif lst[middle] < item:
            start = middle + 1
    return index
