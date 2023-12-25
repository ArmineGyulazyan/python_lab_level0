def joinn(iterables,sep):
    container = ''
    for i in iterables:
        container += i
        container +=sep
    return container

text = ['Python','is','a', 'fun', 'programming', 'language' ]
print(joinn(text, ' ;'))
print((joinn(['12','ab','c'],',')))
print((joinn('abcd12g',',')))