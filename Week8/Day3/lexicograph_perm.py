from itertools import permutations
numbers = list(permutations('0123456789'))
print(int(''.join(numbers[999999])))

# def permutations(iterable, r=None):
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#
#     if r > n:
#         return
#
#     indices = list(range(n))
#     cycles = list(range(n, n - r, -1))
#
#     yield tuple(pool[i] for i in indices[:r])
#
#     while n:
#         for i in reversed(range(r)):
#             cycles[i] -= 1
#             if cycles[i] == 0:
#                 indices[i:] = indices[i + 1:] + indices[i:i + 1]
#                 cycles[i] = n - i
#             else:
#                 j = cycles[i]
#                 indices[i], indices[-j] = indices[-j], indices[i]
#                 yield tuple(pool[i] for i in indices[:r])
#                 break
#         else:
#             return
#
# print(''.join(list(permutations('0123456789'))[999999]))

'''
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

def nth_permutation(p):
    arr = [0,1,2,3,4,5,6,7,8,9]
    arr_cpy = [0,1,2,3,4,5,6,7,8,9]
    result = []
    remainder = p
    for i in range(len(arr)-1,0,-1):
        permutation = 1
        lowest_pos = 1
        while lowest_pos*factorial(i)<remainder and lowest_pos <= i:
            permutation = lowest_pos*factorial(i)
            lowest_pos+=1
        print(lowest_pos-1)
        result.append(arr_cpy[lowest_pos-1])
        arr_cpy.remove(arr_cpy[lowest_pos-1])
        remainder -= permutation

nth_permutation(1000000)
'''