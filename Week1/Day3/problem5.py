def move_even_to_front_inplace(input_list):

    left, right = 0, len(input_list) - 1

    while left < right:

        while input_list[left] % 2 == 0 and left < right:
            left += 1

        while input_list[right] % 2 != 0 and left < right:
            right -= 1

        input_list[left], input_list[right] = input_list[right], input_list[left]

    return input_list


input_list = [3, 6, 16, 15, 5]
move_even_to_front_inplace(input_list)
print(input_list)


#with additional lists

# ls = [1,2,5,3,4,5,6,20,7,23,80]
# evens = []
# odds = []
#
# for i in ls:
#     if i % 2 == 0:
#         evens.append(i)
#     else:
#         odds.append(i)
# all = evens + odds
# print(all)
#

