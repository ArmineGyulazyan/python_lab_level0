def calc(n):
    res=n
    def inn(m=None):
        nonlocal res
        if m is None:
            return res
        res += m
        return inn
    return inn

print(calc(100)(10)(7)())
print(calc(1)())