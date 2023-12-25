class TextNotFound(Exception):
    pass

def add_data(file):
    inp = input('Enter data: ')
    with open(file,'w') as file:
        file.write(inp)

def data_ret(file):
    with open(file,'r') as file:
        s=file.read()
        print(s)

def data_update(file):
    inp = input('Enter the data to update: ')
    up = input('Enter value to replace with: ')
    with open(file,'r+') as file:
        text = file.read()
        try:
            if inp not in text:
                raise TextNotFound('The data is not found')
            t_rep = text.replace(inp,up)
            file.write(t_rep)
        except TextNotFound as e:
            print(e)

def data_del(file):
    inp = input('Enter the data to delete: ')
    with open(file, 'r+') as file:
        text = file.read()
        t_rep=text.replace(inp,'')
        file.write(t_rep)

while True:
    print("\nHello! Here are the options we offer\n")
    print("1.Add data\n2.Retrieve data\n3.Data update\n4.Data Deletion\n5.Quit\n")
    inp = input("Select what you want to do: ")

    if inp == '1':
        add_data('file.txt')

    elif inp == '2':
        data_ret('file.txt')

    elif inp == '3':
        data_update('file.txt')

    elif inp == '4':
        data_del('file.txt')

    elif inp == '5':
        break
    else:
        print('\nInvalid input, Choose again\n')


