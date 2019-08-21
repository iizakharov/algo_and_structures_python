
import timeit
import random
from memory_profiler import profile

# Вариант 1
#@profile
def quick_sort(orig_list):
    if len(orig_list) <= 1:
        return orig_list
    else:
        q = random.choice(orig_list)
        L = []
        M = []
        R = []
        for elem in orig_list:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return quick_sort(L) + M + quick_sort(R)


# замеры
orig_list = [random.randint(-100, 100) for _ in range(500)]
print(timeit.timeit("quick_sort(orig_list)", \
    setup="from __main__ import quick_sort, orig_list", number=10))


# Вариант 2
'''
def quick_sort(orig_list):
    if len(orig_list) <= 1:
        return orig_list
    else:
        q = random.choice(orig_list)
        L = [elem for elem in orig_list if elem < q]

        M = [q] * orig_list.count(q)
        R = [elem for elem in orig_list if elem > q]
        return quick_sort(L) + M + quick_sort(R)

orig_list = [0,3,5,1,2,3,5,4,2,34,43,24]

# замеры
print(quick_sort(orig_list))

print(timeit.timeit("quick_sort(orig_list)", \
    setup="from __main__ import quick_sort, orig_list", number=1000))
'''

# Вариант 3
'''
def quick_sort(orig_list, l, r):
    if l >= r:
        return
    else:
        q = random.choice(orig_list[l:r + 1])
        i = l
        j = r
        while i <= j:
            while orig_list[i] < q:
                i += 1

            while orig_list[j] > q:
                j -= 1
            if i <= j:
                orig_list[i], orig_list[j] = orig_list[j], orig_list[i]
                i += 1
                j -= 1
                quick_sort(orig_list, l, j)
                quick_sort(orig_list, i, r)
    return orig_list

orig_list = [0,3,5,1,2,3,5,4,2,34,43,24]

# замеры
l = 0
r = len(orig_list)-1
print(quick_sort(orig_list, l, r))

print(timeit.timeit("quick_sort(orig_list, l, r)", \
    setup="from __main__ import quick_sort, orig_list, l, r", number=1000))
'''