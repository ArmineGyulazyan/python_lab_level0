# def foo(n=None):
#     return n
#     yield [1,2,3]
#
# print(foo([]))

# ls=[bool(None),bool('much'),1,0,int(),bool()]
# print(ls)
# ls.sort()
# print(ls) #[False, 0, 0, False, True, 1]

# y=[1,2,3]
# z=(1,2,3)
# print(type((x for x in y)).__name__)#generator
# print(type([h for h in y]).__name__)#list

# #recursive
# def gcd(n1, n2):
#     if n2 == 0:
#         return n1
#     return gcd(n2,n1%n2)
#
# print(gcd(25,15))
# #iterative
# def gcd(n1, n2):
#     while n2 != 0:
#         n1,n2=n2,n1%n2
#     return n1
#
# print(gcd(25,15))

# def fib_rec(num):
#     if num in [1,2]:
#         return num-1
#     return fib_rec(num-1)+fib_rec(num-2)
#
# print(fib_rec(1))
# #iterative
# def fib(n):
#     if n in [1,2]:
#         return n-1
#
#     sum_f = 0
#     prev = 0
#     next_i = 1
#     for i in range(2,n):
#         sum_f = prev + next_i
#         prev = next_i
#         next_i = sum_f
#     return sum_f

#count 1s
# def count_one(n):
#     count=0
#     while n>0:
#         count += n&1
#         n >>= 1
#     return count

# def repeat(st):
#     i=0
#     j=1
#     for letter in st:
#         pos = ord(letter)-97
#         if i & j<<pos > 0:
#             return False
#         else:
#              i |= j<<pos
#     return True

# def foo():
#     return 666
#     yield 42
#
# print(foo().__class__.__name__)

# def repeat(ls):
#     x = ls[0]
#     for i in ls[1:]:
#         x^=i
#     return x
# print(repeat([4,2,4,2,1]))

# def has_repeated_string(strings):
#     seen = set()
#     for string in strings:
#         if string in seen:
#             return True
#         seen.add(string)
#     return False
#
# # Example usage:
# strings = ["apple", "banana", "cherry", "apple", "date"]
# result = has_repeated_string(strings)
# print(result)  # Prints: True

# ls=[1,2,3,[5,6]]
# l=ls[:]
# l[0]=100
# l[3][0]=300
# print(ls) #[1, 2, 3, [300, 6]]
# print(l)  #[100, 2, 3, [300, 6]]