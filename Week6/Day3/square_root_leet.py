def sqrt_leet(n):
    guess = 0.1
    for _ in range(101):
        next_guess = 0.5*(guess+(n/guess))
        if abs(next_guess-guess)<0.000000000000001:
            return int(next_guess)
        guess = next_guess

print(sqrt_leet(4))