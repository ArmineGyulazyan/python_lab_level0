def shortestSequence(self, rolls, k):
    res = 0
    seti = set()
    for i in rolls:
        seti.add(i)
        if len(seti) == k:
            res += 1
            seti.clear()
    return res + 1