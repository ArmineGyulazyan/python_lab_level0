def trig_angles(a,b,c):
    cosx = (a**2+b**2-c**2)/(2*a*b)
    sinx = (1-cosx**2)**0.5
    tgx = sinx/cosx if cosx != 0 else print("tgx doesn't exist")
    ctgx = cosx/sinx if sinx != 0 else print("ctgx doesn't exist")

    return sinx, cosx, tgx, ctgx

print(trig_angles(10,24,26))
print(trig_angles(3,4,5))
print(trig_angles(5,5,7))
print(trig_angles(26,24,10))



