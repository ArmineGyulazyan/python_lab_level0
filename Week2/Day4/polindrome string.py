def is_palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()

    length = len(input_string)

    for i in range(length // 2):
        if input_string[i] != input_string[length - i - 1]:
            return False

    return True

print(is_palindrome("racecar"))  # True
print(is_palindrome("Hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True
