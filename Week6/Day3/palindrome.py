def isPalindrome(x):
    if x>=0 and str(x)==str(x)[::-1]:
        return True
    return False

print(isPalindrome(121))
print(isPalindrome(122))
print(isPalindrome(-121))