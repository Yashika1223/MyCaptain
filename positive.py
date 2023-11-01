#print all positive numbers in a list
def print_pos_num(numbers):
    pos_num = [num for num in numbers if num > 0]
    if pos_num:
        print("Output:", ', '.join(map(str, pos_num)))
    else:
        print("No positive numbers in the list.")

#Input
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

print("Input:", list1)
print_pos_num(list1)

print("\nInput:", list2)
print_pos_num(list2)
