class InvalidOperator(Exception):
    pass

def addition(n1,n2):
    res = n1+n2
    print(res)

def subtraction(n1,n2):
    res = n1-n2
    print(res)

def multiplication(n1,n2):
    res = n1*n2
    print(res)

def division(n1,n2):
    try:
        res = n1/n2
    except ZeroDivisionError:
        print('\nThe second element cannot be 0')
    else:
        print(res)

while True:
    print("Operation list\n")
    print("1.Addition +\n2.Subtraction -\n3.Multiplication *\n4.Division /\n5.exit\n")
    op = input('Enter the operator: ')
    try:
        if op not in ['+','-','*','/','exit']:
            raise InvalidOperator('Invalid operator')
        if op == 'exit':
            break
        inp1 = float(input('Enter the first number: '))
        inp2 = float(input('Enter the second number: '))
    except InvalidOperator as e:
        print(e)
    except ValueError:
        print('You should enter numbers')

    if op == '+':
        addition(inp1,inp2)
    elif op == '-':
        subtraction(inp1,inp2)
    elif op == '*':
        multiplication(inp1,inp2)
    elif op == '/':
        division(inp1,inp2)
