def set_subset(s1,s2):
    if len(s1) <= len(s2):
        return True if s1.issubset(s2) else False
    else:
        return True if s2.issubset(s1) else False

s1 = {1,2,3,4,5,6,8}
s2 = {8}

print(set_subset(s1,s2))