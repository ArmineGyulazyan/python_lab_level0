def same_most_and_least_significant_bits(num):
    num_bits = 0
    n = num
    while n > 0:
        num_bits += 1
        n >>= 1

    msb = (num >> (num_bits - 1)) & 1
    lsb = num & 1

    return msb == lsb


num1 = 9  # 1001
num2 = 12  # 1100

result1 = same_most_and_least_significant_bits(num1)
result2 = same_most_and_least_significant_bits(num2)

print(result1)
print(result2)
