def root(n,max_it=100):
    '''
    res = n ** 0.5
    return res
    '''
    #method2
    '''
    x=0
    while x**2-n < 0.0001:
        x += 0.1
    return x
    '''
     #aranc **, miayn lriv armati depquma ashxatum
    # for i in range(int(n/2)+1):
    #     if i * i == n:
    #         return i
    guess = 0.1
    for _ in range(max_it):
        next_guess = 0.5*(guess+n/guess)
        if abs(next_guess-guess) < 0.00000001:
            return next_guess
        guess = next_guess


print(root(25))
print(root(256))
print(root(5))
print(root(16))
print(root(15))

