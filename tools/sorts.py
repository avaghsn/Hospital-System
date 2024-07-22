def insertion_sort(array, key=None):
    n = len(array)
    for j in range(1, n):
        i = j
        k = array[i]
        while i > 0 and key(k) < key(array[i - 1]):
            array[i] = array[i - 1]
            i -= 1
        array[i] = k
    return array


def bubble_sort(array, key):
    for i in range(len(array)):
        j = 0
        while j + 1 < len(array):
            if key(array[j]) > key(array[j + 1]):
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
            j += 1
    return array


def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_ = i
        for j in range(i, n):
            if array[j] < array[min_]:
                min_ = j
        temp = array[i]
        array[i] = array[min_]
        array[min_] = temp

    return array


def insertion_sort2(array, ):
    n = len(array)
    for j in range(1, n):
        i = j
        k = array[i]
        while i > 0 and k < array[i - 1]:
            array[i] = array[i - 1]
            i -= 1
        array[i] = k
    return array
