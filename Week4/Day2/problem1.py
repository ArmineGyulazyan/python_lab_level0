def right_angle_tri(a,b,c):
    if a**2+b**2==c**2 or c**2+a**2==b**2 or c**2+b**2==a**2:
        return 'Right angle triangle'
    return 'Not right angle'

print(right_angle_tri(3,4,5))
print(right_angle_tri(3,5,5))
print(right_angle_tri(3,5,4))
print(right_angle_tri(10,8,6))