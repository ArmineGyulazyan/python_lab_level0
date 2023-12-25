def plusOne(digits):
    num = int(''.join([str(i) for i in digits]))+1
    return [int(i) for i in str(num)]

print(plusOne([1,2,3]))