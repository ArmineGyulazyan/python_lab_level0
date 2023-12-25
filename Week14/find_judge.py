def findJudge(self, n: int, trust) -> int: #trust: List[List[int]]
    if not trust and n == 1:
        return 1
    ls = [0 for i in range(0, n + 1)]
    for u, v in trust:
        ls[u] -= 1
        ls[v] += 1
    for i in ls:
        if i == (n - 1):
            return ls.index(i)
    return -1