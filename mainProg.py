import numpy as np
import timeit


def bubble_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        for j in range(0, len_arr - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def reversed_bubble_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        for j in range(0, len_arr - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def select_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr - 1):
        min_index = i
        for j in range(i + 1, len_arr - 1):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def reversed_select_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr - 1):
        min_index = i
        for j in range(i + 1, len_arr - 1):
            if arr[j] > arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    len_arr = len(arr)
    for i in range(1, len_arr):
        k = arr[i]
        min_index = i - 1
        while min_index >= 0 and arr[min_index] > k:
            arr[min_index + 1] = arr[min_index]
            min_index -= 1
        arr[min_index + 1] = k


def reversed_insertion_sort(arr):
    len_arr = len(arr)
    for i in range(1, len_arr):
        k = arr[i]
        min_index = i - 1
        while min_index >= 0 and arr[min_index] < k:
            arr[min_index + 1] = arr[min_index]
            min_index -= 1
        arr[min_index + 1] = k


def cocktail_sort(arr):
    len_arr = len(arr)
    swap_check = True
    for i in range(len_arr // 2):
        swap_check = False
        for j in range(i + 1, len_arr - 1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swap_check = True
        if not swap_check:
            break
        swap_check = False
        for j in range(len(arr) - i - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swap_check = True
        if not swap_check:
            break


def reversed_cocktail_sort(arr):
    len_arr = len(arr)
    swap_check = True
    for i in range(len_arr // 2):
        swap_check = False
        for j in range(i + 1, len_arr - 1):
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swap_check = True
        if not swap_check:
            break
        swap_check = False
        for j in range(len(arr) - i - 1, i, -1):
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swap_check = True
        if not swap_check:
            break


def shell_sort(arr):
    len_arr = len(arr)
    space = len_arr // 2
    while space > 0:
        for i in range(space, len_arr):
            t = arr[i]
            j = i
            while j >= space and arr[j - space] > t:
                arr[j] = arr[j - space]
                j -= space
            arr[j] = t
        space //= 2


def reversed_shell_sort(arr):
    len_arr = len(arr)
    space = len_arr // 2
    while space > 0:
        for i in range(space, len_arr):
            t = arr[i]
            j = i
            while j >= space and arr[j - space] < t:
                arr[j] = arr[j - space]
                j -= space
            arr[j] = t
        space //= 2


def heapify(arr, len_arr, i):
    maxima = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < len_arr and arr[i] < arr[l]:
        maxima = l
    if r < len_arr and arr[maxima] < arr[r]:
        maxima = r
    if maxima != i:
        arr[i], arr[maxima] = arr[maxima], arr[i]
        heapify(arr, len_arr, maxima)


def heap_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr, -1, -1):
        heapify(arr, len_arr, i)
    for i in range(len_arr - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def reversed_heapify(arr, len_arr, i):
    minima = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < len_arr and arr[l] < arr[minima]:
        minima = l
    if r < len_arr and arr[r] < arr[minima]:
        minima = r
    if minima != i:
        arr[i], arr[minima] = arr[minima], arr[i]
        reversed_heapify(arr, len_arr, minima)


def reversed_heap_sort(arr):
    len_arr = len(arr)
    for i in range(int(len_arr / 2) - 1, -1, -1):
        reversed_heapify(arr, len_arr, i)

    for i in range(len_arr - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]

        reversed_heapify(arr, i, 0)


flag = input("If you wanna randomize entered data, press 'Enter'. To enter manually press any other key: ")

if flag == '':
    arr = np.empty(10, dtype=int)
else:
    while True:
        try:
            arr = []
            for i in range(10):
                a = int(input(f'Enter {i + 1} element: '))
                arr.append(a)
            break
        except ValueError:
            print("Input an integer!")

print(f'Non-sorted array: \n {arr}')

func_check = input(
    'Choose one of the sort types: \n 1.Bubble \n 2.Selection \n 3.Insertion \n 4.Cocktail \n 5.Shell \n 6.Heapsort \n')
if func_check == '1':
    reverse_check = input('Choose the sort order: \n 1.Ascending \n 2.Descending \n')
    if reverse_check == '1':
        bubble_sort(arr)
    else:
        reversed_bubble_sort(arr)
elif func_check == '2':
    reverse_check = input('Choose the sort order: \n 1.Ascending \n 2.Descending \n')
    if reverse_check == '1':
        select_sort(arr)
    else:
        reversed_select_sort(arr)
elif func_check == '3':
    reverse_check = input('Choose the sort order: \n 1.Ascending \n 2.Descending \n')
    if reverse_check == '1':
        insertion_sort(arr)
    else:
        reversed_insertion_sort(arr)
elif func_check == '4':
    reverse_check = input('Choose the sort order: \n 1.Ascending \n 2.Descending \n')
    if reverse_check == '1':
        cocktail_sort(arr)
    else:
        reversed_cocktail_sort(arr)
elif func_check == '5':
    reverse_check = input('Choose the sort order: \n 1.Ascending \n 2.Descending \n')
    if reverse_check == '1':
        shell_sort(arr)
    else:
        reversed_shell_sort(arr)
elif func_check == '6':
    reverse_check = input('Choose the sort order: \n 1.Ascending \n 2.Descending \n')
    if reverse_check == '1':
        heap_sort(arr)
    else:
        reversed_heap_sort(arr)

len_arr = len(arr)

print(f'Sorted array: \n {arr}')
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Program was executed by {t} seconds")
