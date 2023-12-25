def generate_fibonacci(limit):
    first, second = 1, 1
    while first <= limit:
        yield first
        first, second = second, first + second

def sum_even_fibonacci(limit):
    even_sum = 0
    for number in generate_fibonacci(limit):
        if number % 2 == 0:
            even_sum += number
    return even_sum


result = sum_even_fibonacci(4000000)
print(result)
