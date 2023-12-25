def canVisitAllRooms(self, rooms) -> bool: #rooms: List[List[int]]
    visited = set()
    stack = [0]
    while stack:
        room = stack.pop()
        visited.add(room)
        for key in rooms[room]:
            if key not in visited:
                stack.append(key)
    return len(visited) == len(rooms)