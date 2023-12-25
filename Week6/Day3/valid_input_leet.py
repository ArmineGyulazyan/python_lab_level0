def valid_input(s):
    pairs = {'(':')','[':']','{':'}'}
    stack=[]
    for item in s:
        if item in pairs:
            stack.append(item)
        elif len(stack)==0 or pairs[stack.pop()]!=item:
            return False
    return len(stack)==0

print(valid_input("()[]{}"))
print(valid_input("(]"))