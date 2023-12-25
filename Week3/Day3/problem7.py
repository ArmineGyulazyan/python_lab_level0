def zipp(*iterables):
    # min_iter = min([len(i) for i in iterables])
    # list_tuples = []
    # for i in range(min_iter):
    #     list_tuples.append(tuple(list[i] for list in iterables))
    # return list_tuples
    if not iterables:
        yield ()
    else:
        min_iter = min([len(i) for i in iterables])
        yield [tuple([j[i] for j in iterables])for i in range(min_iter)]


languages = ['Java', 'Python', 'JavaScript','PHP']
versions = [14, 3, 6]
print(languages)
print(versions)
res = zipp(languages,versions)
print(next(res))

