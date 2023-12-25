def large_palindrome(n):
    #di = {}
    ls=[]
    for i in range(100,n+1):
        for j in range(i,n+1):
            max_p = i*j
            if is_palindrome(max_p):
                res = max_p
                ls.append(res)
                #di[res]=j

    return max(ls)

def is_palindrome(n):
    return n == int(str(n)[::-1])

print(large_palindrome(999))