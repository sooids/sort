from random import randrange

# bubble sort
# in-place sort, stable-sort
def BubbleSort(li, comp=None):
    if not comp:
        comp = lambda A, B: A < B
    if len(li) <= 1:
        return
    else:
        for i in range(len(li), 0, -1):
            for j in range(i - 1):
                if comp(li[j + 1], li[j]):
                    li[j], li[j + 1] = li[j + 1], li[j]
        return li

# selection sort
# in-place sort, unstable-sort
def SelectionSort(li, comp=None):
    if not comp:
            comp = lambda A, B: A < B
    if len(li) <= 1:
        return
    else:
        for i in range(len(li) - 1, -1, -1):
            idx = 0
            for j in range(1, i + 1):
                if comp(li[idx], li[j]):
                    idx = j
            li[i], li[idx] = li[idx], li[i]
        return li


# insertion sort
# in-place sort, stable-sort
def InsertionSort(li, comp=None):
    if not comp:
        comp = lambda A, B: A < B
    if len(li) <= 1:
        return li
    else:
        for i in range(1, len(li)):
            cur = li[i]
            j = i - 1
            while j >= 0 and comp(cur, li[j]):
                li[j + 1] = li[j]
                j -= 1
            li[j + 1] = cur
        return li

# shell sort
# in-place sort, stable-sort
def IntervalInsertionSort(li, Begin, Interval, comp):
    for i in range(Begin + Interval, len(li), Interval):
        cur = li[i]
        j = i - Interval
        while j >= 0 and comp(cur, li[j]):
            li[j + Interval] = li[j]
            j -= Interval
        li[j + Interval] = cur
            
def ShellSort(li, comp=None):
    if not comp:
        comp = lambda A, B: A < B
    if len(li) <= 1:
        return li
    else:
        gap = len(li) // 2
        while gap > 0:
            for i in range(gap):
                IntervalInsertionSort(li, i, gap, comp)
            gap //= 2
        return li

# quick sort
# out-place sort, stable-sort
# use O(n) memory more faster
def QuickSort(li, comp=None):
    if not comp:
        comp = lambda A, B: A < B
    if len(li) <= 1:
        return li
    else:
        pivot = li[0]
        L = [elem for elem in li[1:] if comp(elem, pivot)]
        R = [elem for elem in li[1:] if not comp(elem, pivot)]
        return QuickSort(L, comp) + [pivot] + QuickSort(R, comp)

# quick sort
# in-place sort, unstable-sort
def Partition(li, L, U, comp):
    pivot = L
    pivot_val = li[L]

    while L <= U:
        while L <= U and comp(li[L], pivot_val): L += 1
        while L <= U and comp(pivot_val, li[U]): U -= 1
        if L < U:
            li[L], li[U] = li[U], li[L]
            U -= 1
            L += 1
    li[pivot], li[U] = li[U], li[pivot]
    return U

def Partition_Iter(li, L, U, comp):
    pivot = L
    pivot_val = li[L]
    li[pivot], li[U] = li[U], li[pivot]

    idx = L
    for i in range(L, U):
        if comp(li[i], pivot_val):
            li[i], li[idx] = li[idx], li[i]
            idx += 1
    li[U], li[idx] = li[idx], li[U]
    return idx

def QuickSort_InPlace(li, comp=None):
    if not comp:
        comp = lambda A, B: A <= B
    if len(li) <= 1:
        return
    else:
        def _Qsort(li, L, U):
            if L < U:
                pivot = Partition_Iter(li, L, U, comp)
                _Qsort(li, L, pivot - 1)
                _Qsort(li, pivot + 1, U)
        _Qsort(li, 0, len(li) - 1)
        return li

# merge sort
# out-place sort, stable-sort
def MergeSort(li, comp=None):
    if not comp:
        comp = lambda A, B: A < B
    if len(li) <= 1:
        return li
    else:
        M = len(li) // 2
        L = MergeSort(li[:M], comp)
        R = MergeSort(li[M:], comp)
        return Merge(L, R, comp)

def Merge(L, R, comp):
    C = []
    while L or R:
        if L and R:
            if comp(L[0], R[0]):
                C.append(L[0])
                L = L[1:]
            else:
                C.append(R[0])
                R = R[1:]
        else:
            return C + L + R
    return C

# sort test
def IsSorted(li, orignal):
    return li == sorted(orignal)

def SortTest(size=100, begin=0, end=100000):
    data = [randrange(begin, end) for _ in range(size)]
    inplace_sort = [BubbleSort, SelectionSort, InsertionSort, ShellSort, QuickSort_InPlace]
    outplace_sort = [QuickSort, MergeSort]

    results = list(map(lambda f: IsSorted(f(list(data)), list(data)), inplace_sort + outplace_sort))
    print(results)

if __name__ == "__main__":
    SortTest()
