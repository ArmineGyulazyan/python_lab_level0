def quadr_equation(a,b,c):
    if a == 0:
        return 'Not a quadratic equation'

    discr = b**2 - (4*a*c)
    if discr == 0:
        x = (-1*b)/(2*a)
        return x
    elif discr > 0:
        x1 = ((-1*b)+(discr**0.5))/(2*a)
        x2 = ((-1*b)-(discr**0.5))/(2*a)
        return x1,x2
    else:

        return 'No roots'

print(quadr_equation(2,3,1))
print(quadr_equation(0,3,1))
print(quadr_equation(1,6,9))