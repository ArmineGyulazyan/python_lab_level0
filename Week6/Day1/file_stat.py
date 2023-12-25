with open('stat_file','r') as st_file:
    r_text = st_file.read()
    #lines
    print(len(r_text.splitlines()))
    #words
    r_text_list = r_text.split()
    print(len(r_text_list))
    #symbols
    '''
    count = 0
    for i in r_text:
        if i =='\n':
            continue
        else:
            count+=1
    print(count)
    '''
    count=0
    for i in r_text_list:
        count += len(i)
    print(count)