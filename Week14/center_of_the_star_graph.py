def findCenter(self, edges) -> int: #edges: List[List[int]]
    return list(set(edges[0]) & set(edges[1]))[0]