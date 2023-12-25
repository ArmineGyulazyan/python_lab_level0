def search_word(path,target):
    with open(path) as file:
        file = file.read().splitlines()
    indexes = []
    for idx in range(len(file)):
        if target in file[idx]:
            indexes.append(idx+1)
    return indexes


print(search_word('path','there'))