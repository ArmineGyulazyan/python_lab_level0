def username_validation(fn):
    def wrapper(args):
        if len(args) > 5 and len(args) < 20 and args.isalnum() and args not in ['root', 'admin']:
            return fn(args)
        return 'Not a valid username'

    return wrapper

def email_validation(fn):
    def wrapper(args):
        if ('@' not in args) or ('.' not in args):
            return 'not valid email'
        for i in range(len(args)):
            if args[i] == '@':
                if not args[:i].isalpha() or not args[i + 1:args.index('.')].isalpha():
                    return 'not valid email'
            if args[i] == '.':
                if args[i + 1:] != 'com':
                    return 'not valid email'
        return fn(args)

    return wrapper


def phone_validation(fn):
    def wrapper(args):
        if (args[0] == '+' and args[1::].isdigit()) or args.isdigit():
            return fn(args)
        return 'Not a valid number'

    return wrapper


def pass_validation(fn):
    def wrapper(args):
        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False

        if len(args) < 8:
            return 'not valid pass'

        for i in args:

            if i.isupper():
                has_upper = True
            elif i.islower():
                has_lower = True
            elif i.isdigit():
                has_digit = True
            elif i in "!@#$%^&*":
                has_symbol = True

        if has_upper and has_lower and has_digit and has_symbol:
            return fn(args)

        return 'not valid pass'

    return wrapper


@phone_validation
def phone(num):
    return num


@email_validation
def email(mail):  # ann@exam.com
    return mail


@username_validation
def username(name):
    return name


@pass_validation
def password(psw):
    return psw


name = input("enter name: ")
mail = input("enter email: ")
num = input("enter phone num: ")
pasw1 = input("enter pasw: ")
pasw2 = input("repeat pasw: ")

print(username(name))
print(email(mail))
print(phone(num))
ps = password(pasw1)
print(ps) if ps == password(pasw2) else print('No match')

