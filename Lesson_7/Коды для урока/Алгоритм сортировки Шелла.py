import timeit
import random

def shell_sort(a):
        def new_increment(a):
            i = int(len(a) / 2)
            yield i
            while i != 1:
                if i == 2:
                    i = 1
                else:
                    i = int(round(i/2.2))
                yield i
        for increment in new_increment(a):
            for i in range(increment, len(a)):
                for j in range(i, increment-1, -increment):
                    if a[j - increment] < a[j]:
                        break
                    a[j],a[j - increment] = a[j - increment],a[j]
        return a



orig_list = [0,3,5,1,2,3,5,4,2,34,43,24]

# замеры
print(shell_sort(orig_list))
#orig_list = [random.randint(-100, 100) for _ in range(1000)]

#print(timeit.timeit("shell_sort(orig_list)", \
    #setup="from __main__ import shell_sort, orig_list", number=1000))


