def isAnagram(self, s, t):
    if len(s) != len(t):
        return False

    return all(s.count(i) == t.count(i) for i in t)
