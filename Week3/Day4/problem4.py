def contain_myversion(my_string,sub_str):
    sub_len = len(sub_str)
    for i in range(len(my_string)):
        if my_string[i:i+sub_len] == sub_str:
            return True
    return False

print(contain_myversion('asdsdsd','ds'))
print(contain_myversion('asdsdsd','dsa'))
print(contain_myversion('asdsdsd','dds'))
print(contain_myversion('happy','pp'))