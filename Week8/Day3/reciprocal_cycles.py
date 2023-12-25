num = longest = 1
for n in range(3, 1000, 2):
    if n % 5 == 0:
        continue
    p = 1
    while (10 ** p) % n != 1:
        p += 1

    if p > longest:
        num, longest = n, p

print(num)


# res = 0
# d = 999
# m_len = 0
#
# while d < 1000 and d > 1:
#     res = 1/d
#     st_res = str(res)
#     res_spl = st_res[2:]
#     st = ''
#     for i in range(len(res_spl)):
#         if st == res_spl[i:i+len(st)] and st:
#             m_len = len(st)
#             print('d is', d, 'len is', len(st))
#             d -= 1
#             break
#         else:
#             st += res_spl[i]