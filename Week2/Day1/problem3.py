def rec_list(ls):
    if len(ls) == 0:
        return

    print(ls)
    rec_list(ls[1::])


rec_list([1,2,3,4,5])