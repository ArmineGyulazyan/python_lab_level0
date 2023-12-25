def pop_myversion(iterable,pos=-1):
    tmp = iterable[pos]
    iterable.remove(tmp)
    return tmp



print(pop_myversion([1,2,3,4,5]))
print(pop_myversion([1,2,3,4,5],0))
