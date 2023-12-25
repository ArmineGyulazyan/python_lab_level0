def long_common_pref(strs):

    min_i = min([len(i) for i in strs])
    comm = ''

    for mi in range(min_i):
        for el in range(len(strs) - 1):
            if strs[el][mi] != strs[el + 1][mi]:
                return comm
        comm += strs[0][mi]
    return comm

print(long_common_pref(["flower","flow","flight"]))
print(long_common_pref(["dog","racecar","car"]))
print(long_common_pref([""]))
print(long_common_pref(["a"]))



