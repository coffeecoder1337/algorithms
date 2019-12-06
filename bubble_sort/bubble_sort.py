# функция сортировки массива методом пузырька


def bubble_sort(lst):
    for _ in range(len(lst) - 1):
        for index in range(len(lst) - 1): 
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return lst
