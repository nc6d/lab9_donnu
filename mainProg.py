import numpy as np
import timeit


def bubble_sort(arr):
    num_comps = 0
    num_swaps = 0
    len_arr = len(arr)
    for i in range(len_arr):
        for j in range(0, len_arr - 1 - i):
            num_comps += 1
            if arr[j] > arr[j + 1]:
                num_swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return num_comps, num_swaps

def reversed_bubble_sort(arr):
    num_comps = 0
    num_swaps = 0
    len_arr = len(arr)
    for i in range(len_arr):
        for j in range(0, len_arr - 1 - i):
            num_comps += 1
            if arr[j] < arr[j + 1]:
                num_swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return num_comps, num_swaps


def select_sort(arr):
    num_comps = 0
    num_swaps = 0
    len_arr = len(arr)
    for i in range(len_arr - 1):
        min_index = i
        for j in range(i + 1, len_arr - 1):
            num_comps += 1
            if arr[j] < arr[min_index]:
                min_index = j
        num_swaps += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return num_comps, num_swaps


def reversed_select_sort(arr):
    num_comps = 0
    num_swaps = 0
    len_arr = len(arr)
    for i in range(len_arr - 1):
        min_index = i
        for j in range(i + 1, len_arr - 1):
            num_comps += 1
            if arr[j] > arr[min_index]:
                min_index = j
        num_swaps += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return num_comps, num_swaps

def insertion_sort(arr):
    num_comps = 0
    num_swaps = 0
    len_arr = len(arr)
    for i in range(1, len_arr):
        k = arr[i]
        min_index = i - 1
        num_comps += 1
        while min_index >= 0 and arr[min_index] > k:
            num_swaps += 1
            arr[min_index + 1] = arr[min_index]
            min_index -= 1
        arr[min_index + 1] = k
    return num_swaps, num_comps


def reversed_insertion_sort(arr):
    num_comps = 0
    num_swaps = 0
    len_arr = len(arr)
    for i in range(1, len_arr):
        k = arr[i]
        min_index = i - 1
        num_comps += 1
        while min_index >= 0 and arr[min_index] < k:
            num_swaps += 1
            arr[min_index + 1] = arr[min_index]
            min_index -= 1
        arr[min_index + 1] = k
    return num_swaps, num_comps


def cocktail_sort(arr):
    num_comps = 0
    num_swaps = 0
    len_arr = len(arr)
    swap_check = True
    for i in range(len_arr // 2):
        swap_check = False
        for j in range(i + 1, len_arr - 1):
            num_comps += 1
            if arr[j] < arr[j - 1]:
                num_swaps += 1
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swap_check = True
        if not swap_check:
            break
        swap_check = False
        for j in range(len(arr) - i - 1, i, -1):
            num_comps += 1
            if arr[j] < arr[j - 1]:
                num_swaps += 1
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swap_check = True
        if not swap_check:
            break
    return  num_swaps, num_comps


def reversed_cocktail_sort(arr):
    len_arr = len(arr)
    num_comps = 0
    num_swaps = 0
    swap_check = True
    for i in range(len_arr // 2):
        swap_check = False
        for j in range(i + 1, len_arr - 1):
            num_comps += 1
            if arr[j] > arr[j - 1]:
                num_swaps += 1
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swap_check = True
        if not swap_check:
            break
        swap_check = False
        for j in range(len(arr) - i - 1, i, -1):
            num_comps += 1
            if arr[j] > arr[j - 1]:
                num_swaps += 1
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swap_check = True
        if not swap_check:
            break
    return  num_swaps, num_comps

def shell_sort(arr):
    num_comps = 0
    num_swaps = 0
    len_arr = len(arr)
    space = len_arr // 2
    while space > 0:
        for i in range(space, len_arr):
            t = arr[i]
            j = i
            num_comps += 1
            while j >= space and arr[j - space] > t:
                num_swaps += 1
                arr[j] = arr[j - space]
                j -= space
            arr[j] = t
        space //= 2
    return num_swaps, num_comps


def reversed_shell_sort(arr):
    num_comps = 0
    num_swaps = 0
    len_arr = len(arr)
    space = len_arr // 2
    while space > 0:
        for i in range(space, len_arr):
            t = arr[i]
            j = i
            num_comps += 1
            while j >= space and arr[j - space] < t:
                num_swaps += 1
                arr[j] = arr[j - space]
                j -= space
            arr[j] = t
        space //= 2
    return num_swaps, num_comps


def heapify(arr, len_arr, i, num_swaps, num_comps):
    maxima = i
    l = 2 * i + 1
    r = 2 * i + 2
    num_comps += 1
    if l < len_arr and arr[i] < arr[l]:
        maxima = l
    num_comps += 1
    if r < len_arr and arr[maxima] < arr[r]:
        maxima = r
    if maxima != i:
        num_swaps += 1
        arr[i], arr[maxima] = arr[maxima], arr[i]
        num_swaps, num_comps = heapify(arr, len_arr, maxima, num_swaps, num_comps)
    return num_swaps, num_comps


def heap_sort(arr):
    num_swaps = 0
    num_comps = 0
    len_arr = len(arr)
    heapify(arr, len_arr, 0, num_swaps, num_comps)
    for i in range(len_arr, -1, -1):
        num_swaps, num_comps = heapify(arr, len_arr, i, num_swaps, num_comps)
    for i in range(len_arr - 1, 0, -1):
        num_swaps += 1
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, num_swaps, num_comps)
    return num_swaps, num_comps


def reversed_heapify(arr, len_arr, i, num_swaps, num_comps):
    minima = i
    l = 2 * i + 1
    r = 2 * i + 2
    num_comps += 1
    if l < len_arr and arr[l] < arr[minima]:
        minima = l
    num_comps += 1
    if r < len_arr and arr[r] < arr[minima]:
        minima = r
    if minima != i:
        num_swaps += 1
        arr[i], arr[minima] = arr[minima], arr[i]
        num_swaps, num_comps = reversed_heapify(arr, len_arr, minima, num_swaps, num_comps)
    return num_swaps, num_comps


def reversed_heap_sort(arr):
    num_swaps = 0
    num_comps = 0
    len_arr = len(arr)
    for i in range(len_arr // 2 - 1, -1, -1):
        num_swaps, num_comps = reversed_heapify(arr, len_arr, i, num_swaps, num_comps)
    for i in range(len_arr - 1, -1, -1):
        num_swaps += 1
        arr[0], arr[i] = arr[i], arr[0]

        reversed_heapify(arr, i, 0, num_swaps, num_comps)
    return num_swaps, num_comps


flag = input("If you wanna randomize entered data, press 'Enter'. To enter manually press any other key: ")

if flag == '':
    arr = np.random.randint(-1000, 1000, 1000)
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
        num_comps, num_swaps = bubble_sort(arr)
        name = 'BubbleSort Ascending function: '
    else:
        num_comps, num_swaps = reversed_bubble_sort(arr)
        name = 'BubbleSort Descending function: '
elif func_check == '2':
    reverse_check = input('Choose the sort order: \n 1.Ascending \n 2.Descending \n')
    if reverse_check == '1':
        num_comps, num_swaps = select_sort(arr)
        name = 'SelectSort Ascending function: '
    else:
        num_comps, num_swaps = reversed_select_sort(arr)
        name = 'SelectSort Descending function: '
elif func_check == '3':
    reverse_check = input('Choose the sort order: \n 1.Ascending \n 2.Descending \n')
    if reverse_check == '1':
        num_comps, num_swaps = insertion_sort(arr)
        name = 'InsertionSort Ascending function: '
    else:
        num_comps, num_swaps = reversed_insertion_sort(arr)
        name = 'InsertionSort Descending function: '
elif func_check == '4':
    reverse_check = input('Choose the sort order: \n 1.Ascending \n 2.Descending \n')
    if reverse_check == '1':
        num_comps, num_swaps = cocktail_sort(arr)
        name = 'CocktailSort Ascending function: '
    else:
        num_comps, num_swaps = reversed_cocktail_sort(arr)
        name = 'CocktailSort Descending function: '
elif func_check == '5':
    reverse_check = input('Choose the sort order: \n 1.Ascending \n 2.Descending \n')
    if reverse_check == '1':
        num_comps, num_swaps = shell_sort(arr)
        name = 'ShellSort Ascending function: '
    else:
        num_comps, num_swaps = reversed_shell_sort(arr)
        name = 'ShellSort Descending function: '
elif func_check == '6':
    reverse_check = input('Choose the sort order: \n 1.Ascending \n 2.Descending \n')
    if reverse_check == '1':
        num_swaps, num_comps = heap_sort(arr)
        name = 'HeapSort Ascending function: '
    else:
        num_swaps, num_comps = reversed_heap_sort(arr)
        name = 'HeapSort Descending function: '

len_arr = len(arr)
print(f'Sorted array: \n {arr}')
print(name)
print(f'Comparisons were executed {num_comps} times')
print(f'Swaps were executed {num_swaps} times')
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Program was executed by {t} seconds")
