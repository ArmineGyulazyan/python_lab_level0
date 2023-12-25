import re

def find_longest_word(input_string):
    words = re.sub(r'[^\w\s]', '', input_string).split()
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

input_string = "This is a sample, sentence with some long words"
result = find_longest_word(input_string)
print(result)