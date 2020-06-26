import random
import time

# from . import selection_sort
# from . import insert_sort
from algorithms.sort import bubble_sort
from algorithms.sort import selection_sort
from algorithms.sort import insert_sort
from algorithms.sort import quick_sort


def get_arrs(num):
    arr = []
    for i in range(num):
        arr.append(random.randint(1, 1000))
    return arr

if __name__ == '__main__':

    for num in [10, 100, 1000, 10000]:
        print("----"*20)

        bubble_sort.bubble_sort(get_arrs(num))
        selection_sort.selection_sort(get_arrs(num))
        insert_sort.insert_sort(get_arrs(num))
        quick_sort.quick_sort_new(get_arrs(num))
        quick_sort.sort_lib_python(get_arrs(num))





