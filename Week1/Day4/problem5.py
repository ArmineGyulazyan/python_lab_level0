def isPrime(num):

    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False

    return True


#num = int(input("Enter a number: "))
#print(isPrime(num))

# a=range(0,101,2)
# print(*a)

# for i in range(1,7):
#     line=i
#     print('*',end=' ')
# inp1 = int(input("frist num: "))
# inp2 = int(input("second num: "))
#
# all = range(inp1,inp2+1)
# l=len(all)/2
# if inp1<inp2:
#     tmp = inp1 #1
#     inp2 = inp1 #10
#     inp2 = tmp
#     res= int((inp1+inp2)*l)
#     print(res)