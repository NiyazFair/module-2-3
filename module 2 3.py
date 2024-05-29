index = 0
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while index < len(my_list):
    index += 1
    if my_list[index-1] > 0:
        print(my_list[index-1])
    elif my_list[index-1] == 0:
        continue
    elif my_list[index-1] < 0:
        break

