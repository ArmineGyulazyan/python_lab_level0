def valid_username(username):
    def wrap(args):
        if len(args)>5 and len(args)<20 and args.isalnum() and args not in ['root','admin']:
            return username(args)
        return 'invalid input'
    return wrap

def valid_mail(email):
    def wrap(args):
        if '@' or '.' not in args:
            return 'invalid input'
        for i in range(len(args)):
            if args[i] == '@':
                if not args[:i].isalnum() or not args[i+1:args.index('.')].isalnum():
                    return 'invalid input'
            elif args[i] == '.':
                if args[i+1::] != 'com':
                    return 'invalid input'
        return email(args)
    return wrap


def valid_phone(phone):
    def wrap(args):
        if (args[0] == '+' and args[1::].isdigit()) or args.isdigit():
            return phone(args)
        return 'invalid input'
    return wrap

def valid_pasword(password):
    def wrap(args):
        if len(args)<8:
            return 'Invalid input'
        has_num = False
        has_let = False
        has_upp = False
        has_low = False
        has_symb = False

        for i in range(len(args)):
            if args[i].isdigit():
                has_num = True
            elif args[i].isalpha():
                has_let = True
            elif args[i].islower():
                has_low = True
            elif args[i].isupper():
                has_upp = True
            elif args[i] in ['!@#$%^&*']:
                has_symb = True

        if has_num and has_let and has_upp and has_low and has_symb:
            return password(args)
    return wrap

@valid_username
def username(name):
    return name
@valid_mail
def email(mail):
    return mail
@valid_phone
def phone(num):
    return num
@valid_pasword
def password(psw):
    return psw

us = input('Enter username: ')
em = input('Enter email: ')
ph = input('Enter phome number: ')
psw = input('Enter password: ')
psw2 = input('Repeat password: ')

print(username(us))
print(email(em))
print(phone(ph))
print(psw if password(psw) == password(psw2) else 'No match')