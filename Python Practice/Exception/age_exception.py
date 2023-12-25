class InvalidAgeError(Exception):
    #print('you have to be 18 or older')
    pass
def age_check(age):
    if age < 18:
        raise InvalidAgeError('you have to be 18 or older')

try:
    user_age = int(input('Enter your age: '))
    age_check(user_age)
except InvalidAgeError as e:
    print(e)

age_check(25)
#print(positive_root(-25))
