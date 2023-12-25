def create_counter(start=0):
    count = start

    def increment(n=1):
        nonlocal count
        count += n

    def decrement(n=1):
        nonlocal count
        count -= n

    def get_counter_value():
        return count

    return increment,decrement,get_counter_value

inp = int(input('Enter a start value or leave with default 0: '))
incr,decr,res = create_counter(inp)
while True:
    print("Options\n1.increment\n2.decrement\n3.current result\n4.quit")
    num = input('Choose a number ')

    if num == '1':
        inp1 = int(input('Enter a increment value or leave with default 1: '))
        incr(inp1)
    elif num == '2':
        inp2 = int(input('Enter a decrement value or leave with default 1: '))
        decr(inp2)
    elif num == '3':
        print(res())
    elif num == '4':
        break










































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































