import copy
# 1
null_List = []
my_list = [0, 1, 2, 3, 4]
my_list1 = [0, "qq", 2.3, True]
my_list2 = [[1, 2, 3], [4, 2]]
# 2
copy_list = copy.copy(my_list)
deep_copy_list = copy.deepcopy(my_list2)

print(copy_list)
print(deep_copy_list)
# 3
null_List.extend(my_list)
my_list.append(my_list1)
print("add elements in empty list : ", null_List)
print(my_list)
# 4
print("task4 ")
task = [1, 2, 3, 4, 5, 6, 7]
# a
print(task[0])
# b
max_ele = max(task)
print(max_ele)
# c
task[0] = [22.2, 11.1, 4]
print(task)
# d
del task[1]
print(task)
# e
removed_element = task.pop(1)
print("Видалений елемент зі значенням:", removed_element)
print("Список після видалення другого елемента:", task)
# f
value_to_remove = 5
task.remove(value_to_remove)
print(f"Список value_to_remove}:", task)

# 5
l = [22, ['ogo', 1, 3, 88], 'apple']

element_with_88 = l[1][3]
print(element_with_88)
# 6
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
midpoint = len(original_list) // 2
second_ = original_list[midpoint:]
print("Новий список (друга половина):", second_)
# 7

original_lis1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
last_three = original_lis1[-3:]
del original_list[-3:]
original_lis1 = last_three + original_lis1
print("Список після переміщення трьох останніх елементів на початок:", original_lis1)
# 8
list4 = [3, -2, 0, 5, -1, 4, 0, -3]
new_list = [1 if x >= 0 else x for x in list4]

print("new list:", new_list)
# 9
sorted_list = sorted(list4, reverse=True)
print("sorted_list:", sorted_list)
# 10
numbers = [10, 20, 30, 40, 50]
numbers1 = [-10, -20, -30, 40, 50]


sum_of_elements = 0

print("Елементи списку:")
for num in numbers:
    print(num)
    sum_of_elements += num

print("sum_of_elements:", sum_of_elements)

sum_of_elements1 = sum([num for num in numbers1])

print("Елементи списку:")
for num in numbers1:
    print(num)

print("sum_of_elements:", sum_of_elements1)
# 11

l = [2, 9, 2]
new_list = [2 * x for x in range(1, 5)]
print(new_list)

# 12
n1 = int(input("Введіть початкове значення n1: "))
n2 = int(input("Введіть кінцеве значення n2: "))
new_list = list(range(n1, n2 + 1))
print("new_list:", new_list)
# 13
s = "Hello my dear friend"
result_list = s.split()
print(result_list)
# 14
l1 = [1, 2, 9, 4]
l2 = [6, 5]

l1.append(l2)

print(l1)
# 15
l1 = [1, 2, 9, 4]
l2 = [6, 5]
result_list = l1 + l2

print(result_list)
# 16
l = [[4, 3], [1, 2], [0, 5], [4, 0]]
l.sort(key=lambda x: x[0], reverse=True)
print(l)
