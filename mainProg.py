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


flag = input("If you wanna randomize entered data, press 'Enter'. To enter manually press any other key: ")

if flag == '':
    arr = np.empty(5, dtype=int)
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

func_check = input('Choose one of the sort types: \n 1.Bubble \n 2.Selection \n 3.Insertion \n')
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

print(f'Sorted array: \n {arr}')
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Program was executed by {t} seconds")
