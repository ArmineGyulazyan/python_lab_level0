class FormulaError(Exception):
    pass

def calculator(formula):

    expr = formula.split()

    while expr != ''.join(expr):
        if len(expr) != 3:
            raise FormulaError('You should enter 3 elements')
        try:
            float(expr[0])
            float(expr[2])
        except ValueError:
            raise FormulaError('First or Third element cannot be cast to float')

        if expr[1] not in ['+', '-', '*', '/']:
            raise FormulaError('Second element is not an operator')


        if expr[1] == '+':
            sum_num = float(expr[0]) + float(expr[2])
            print(sum_num, "\n")

        elif expr[1] == '-':
            sub_num = float(expr[0]) - float(expr[2])
            print(sub_num, "\n")

        elif expr[1] == '*':
            mul_num = float(expr[0]) * float(expr[2])
            print(mul_num, "\n")

        elif expr[1] == '/':
            div_num = float(expr[0]) / float(expr[2])
            print(div_num, "\n")
        expr = input('Enter to count: ')
    return

inp=input('Enter to count: ')
calculator(inp)