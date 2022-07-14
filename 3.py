# Самый быстрый алгоритм сортировки - это тот, который использует
# особенности данных на имеющемся оборудовании с учетом внешних ограничений.

# Так как по условию задачи массив может быть любого размера со случайным порядком чисел,
# то подобрать один алгоритм, который быстрее всего отсортирует произвольный массив чисел,
# невозможно, потому что я могу назвать хотя бы два различных алгоритма,
# использующиеся в одних из самых популярных языков программирования, а именно:
# 1. Timsort в Python, Java, Android, 2. Introsort в C++

# Timsort использует то, что часть чисел (в данном случае) массива уже упорядочена.
# В таком случае возможно более эффективно отсортировать оставшееся.
# Если массив уже отсортирован, то Timsort отработает за линейное время от длины массива.
# В худшем случае - за O(nlogn), где n - длина массива.

# Introsort, являющийся комбинацией Quicksort, Heapsort и Insertion sort
# в среднем имеет более малую скрытую константу (в О-символике),
# но в лучшем, среднем и худшем случаях сортирует за O(nlogn), где n - длина массива.

# Потому что Python использует Timsort в качестве сортировки по умолчанию,
# то для ответа на задачу представлена реализация Introsort.



import math
from heapq import heappush, heappop

array = [-3, 5, -10, 7, 0]


def heapsort():
    global array
    h = []

    for value in array:
        heappush(h, value)
    array = []

    array = array + [heappop(h) for i in range(len(h))]


def InsertionSort(begin, end):
    left = begin
    right = end

    for i in range(left + 1, right + 1):
        key = array[i]

        j = i - 1
        while j >= left and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


def Partition(low, high):
    global array

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def MedianOfThree(a, b, d):
    global array
    A = array[a]
    B = array[b]
    C = array[d]

    if A <= B and B <= C:
        return b
    if C <= B and B <= A:
        return b
    if B <= A and A <= C:
        return a
    if C <= A and A <= B:
        return a
    if B <= C and C <= A:
        return d
    if A <= C and C <= B:
        return d


def IntrosortUtil(begin, end, depthLimit):
    global array
    size = end - begin
    if size < 16:
        InsertionSort(begin, end)
        return

    if depthLimit == 0:
        heapsort()
        return

    pivot = MedianOfThree(begin, begin + size // 2, end)
    (array[pivot], array[end]) = (array[end], array[pivot])
    partitionPoint = Partition(begin, end)

    IntrosortUtil(begin, partitionPoint - 1, depthLimit - 1)
    IntrosortUtil(partitionPoint + 1, end, depthLimit - 1)


def Introsort(begin, end):
    depthLimit = 2 * math.floor(math.log2(end - begin))
    IntrosortUtil(begin, end, depthLimit)


n = len(array)
Introsort(0, n - 1)
print(array)
