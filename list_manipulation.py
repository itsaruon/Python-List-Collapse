import random

def generate_random_list(k):
    return [random.randint(2, 10) for _ in range(k)]

def collapse_list(lst):
    new_list = []
    length = len(lst)
    for i in range(1, length, 2):
        new_list.append(lst[i] + lst[i - 1])
    if length % 2 == 1:
        new_list.append(lst[length - 1])
    return new_list

k = int(input("Enter the number of elements in the list: "))
my_list = generate_random_list(k)

print("Old List:", my_list)
collapsed_list = collapse_list(my_list)
print("Collapsed List:", collapsed_list)
