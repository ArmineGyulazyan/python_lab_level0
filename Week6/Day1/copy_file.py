# def file_copy(text,a,b):
#     r = text.read()
#     print(r)
    # with open('text1', 'w+') as replace_text:
    #      repla


with open('text','r') as filei, open('text2','w') as filei2 :
    t = filei.read()
    row = t.splitlines()
    print(row[0])

    new_t = t.replace('a','b')
    filei2.write(new_t)
    # for line in filei:
    #     new_l = line.replace('a','b')
    #     filei2.write(new_l)
    #     print(new_l)

