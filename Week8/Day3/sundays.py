Weekcode = 1
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sunday_count = 0

for cur_year in range(1900, 2001):

    if (cur_year % 4 == 0 and cur_year % 100 != 0) or (cur_year % 400 == 0):
        months[1] = 29
    else:
        months[1] = 28

    for y in months:
        Weekcode = (Weekcode + y) % 7

        if Weekcode == 0 and cur_year > 1900:
            sunday_count += 1

print(sunday_count)