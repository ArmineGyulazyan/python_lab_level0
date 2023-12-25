def backspaceCompare(self, s, t):
    def comp(st):
        res = []
        for i in st:
            if i != '#':
                res.append(i)
            else:
                if len(res) != 0:
                    res.pop()
        return res

    return comp(s) == comp(t)
