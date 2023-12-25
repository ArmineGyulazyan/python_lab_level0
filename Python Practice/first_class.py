def filt(func,iterable):
    if func is None:
        fill_el = [i for i in iterable if bool(i)]
    else:
        fill_el = [i for i in iterable if func(i)]
    for i in fill_el:
        yield i

def enum(iterable,start=0):
    for i in iterable:
        yield start,i
        start += 1

def zipp(*iterable):
    if not iterable:
        yield ()
    else:
        min_iter = min([len(i) for i in iterable])
        yield [tuple([j[i] for j in iterable])for i in range(min_iter)]

def mapp(func,*iterable):
    min_iter = min([len(i) for i in iterable])
    yield [func(*(it[i] for it in iterable)) for i in min_iter]

def reduce(func,iterable,initial=None):
    it = iter(iterable)
    if initial is None:
        value = next(it)
    else:
        value = initial
    for i in it:
        value = func(value,i)
    return value
