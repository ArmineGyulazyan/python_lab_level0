def common(seq1,seq2):
    # res = []
    # for i in seq1:
    #     if i in seq2:
    #         res.append(i)
    # return res
    return [i for i in seq1 if i in seq2]

print(common('jel','hello'))