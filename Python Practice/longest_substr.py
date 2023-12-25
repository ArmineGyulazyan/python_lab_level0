def len_longest_substr(s):
    st_d = {}
    left,right = 0,0
    len_st = 0
    while right<len(s):
        if s[right] in st_d:
            left = max(st_d[s[right]]+1,left)
        st_d[s[right]]=right
        len_st = max(len_st,right-left+1)
        right+=1
        print(st_d)
        print(left)
        print(right)
    return len_st

# print(len_longest_substr('abcabcbb'))
# print(len_longest_substr('bbbbb'))
print(len_longest_substr('pwwkew'))



