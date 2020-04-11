import numpy as np
import timeit


def heapify(arr, len_arr, i):
    global num_swaps
    global num_comps
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
        heapify(arr, len_arr, maxima)



def heap_sort(arr):
    global num_swaps
    global num_comps
    len_arr = len(arr)
    heapify(arr, len_arr, 0)
    for i in range(len_arr, -1, -1):
        heapify(arr, len_arr, i)
    for i in range(len_arr - 1, 0, -1):
        num_swaps += 1
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)



flag = input("If you wanna randomize entered data, press 'Enter'. To enter manually press any other key: ")

if flag == '':
    arr = np.random.randint(-10000, 10000, 1000)
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
num_swaps = 0
num_comps = 0
heap_sort(arr)

len_arr = len(arr)
print(f'Sorted array: \n {arr}')
print(num_comps, 'comparisons were executed')
print(num_swaps, 'swaps were executed ')
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Program was executed by {t} seconds")
