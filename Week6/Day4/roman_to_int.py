def roman_to_integer(s):
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    sum_r = 0
    for i in range(len(s)):
        if i + 1 < len(s) and rom_num[s[i]] < rom_num[s[i + 1]]:
            sum_r -= rom_num[s[i]]
        else:
            sum_r += rom_num[s[i]]
    return sum_r

print(roman_to_integer('IVII'))
print(roman_to_integer('LVIII'))
print(roman_to_integer('MCMXCIV'))




