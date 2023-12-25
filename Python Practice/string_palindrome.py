def isPalindrome(s):
    new_st=''
    for i in s:
        if not i.isalnum():
            new_st+=i.replace(i, '')
        else:
            new_st+=i.lower()

    if new_st == new_st[::-1]:
        return True
    return False

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(' '))
#another version
'''
def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for a case-insensitive check
    input_string = input_string.replace(" ", "").lower()
    
    length = len(input_string)
    
    for i in range(length // 2):
        if input_string[i] != input_string[length - i - 1]:
            return False

    return True

# Test cases
print(is_palindrome("racecar"))   # True
print(is_palindrome("Hello"))     # False
print(is_palindrome("A man a plan a canal Panama"))  # True

'''