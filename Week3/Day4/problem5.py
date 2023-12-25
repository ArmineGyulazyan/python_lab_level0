def split_myversion(my_string,sep=' '):
    container = []
    tmp_str = ''

    for i in range(len(my_string)):
        if my_string[i] != sep:
            tmp_str += my_string[i]

            if i==len(my_string)-1:
                container.append(tmp_str)
        else:
            container.append(tmp_str)
            tmp_str = ''
    if not container:
        return [my_string]
    return container


print('Real split','simple thing to do'.split())

print('My version split',split_myversion('simplethingtodo',','))

print('My version split',split_myversion('simple thing to do'))

print('My version split',split_myversion('simple thing to do',','))
print('My version split',split_myversion('simple,thing,to,do',','))

