def strStr( haystack, needle):
    len_need = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i+len_need] == needle:
            return i
    return -1

print(strStr('hello','ll'))