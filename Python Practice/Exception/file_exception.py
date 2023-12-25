def file_read(fl):
    try:
        fs=open(fl)
        for i in fs:
            print(i)
    except FileNotFoundError:
        print('The file does not exist')



file_read('test.txt')
file_read('test1.txt')



