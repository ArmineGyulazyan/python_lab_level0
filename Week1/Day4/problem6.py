import problem5

def primeSum(num):
    for i in range(2,int((num**0.5))+1):
        if problem5.isPrime(i) and problem5.isPrime(num-i):
            return 1
    return 0


num = int(input("Enter the number: "))
print(primeSum(num))