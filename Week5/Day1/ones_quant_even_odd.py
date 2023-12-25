def ones_quant_even(num):
    count = 0
    while num > 0:
        count += num & 1
        num >>= 1
    return count % 2 == 0

print(ones_quant_even(11))
print(ones_quant_even(15))