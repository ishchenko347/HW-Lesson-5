# 3. Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.

first = []
second = []

file = open('task03_1.txt', 'r')
for i in file:
    first.append(i)
file.close()
print(first)

file = open('task03_2.txt', 'r')
for i in file:
    second.append(i)
file.close()
print(second)

str_first = ' '.join(first).split(' + ')
str_second = ' '.join(second).split(' + ')

str_list = str_first + str_second
# print(str_list)

for_five = []
for_four = []
for_three = []
for_two = []
for_one = []
for_null = []

for i in str_list:
    if i[-1] == '5':
        for_five.append(i[:2])
    elif i[-1] == '4':
        for_four.append(i[:2])
    elif i[-1] == '3':
        for_three.append(i[:2])
    elif i[-1] == '2':
        for_two.append(i[:2])
    elif i[-1] == '1':
        for_one.append(i[:2])
    elif i[-1] == '0':
        for_null.append(i[:2])

def Func(a):
    res = 0
    for i in a:
        res = res + int(i)
    res_list.append(res)

y = 5
res_list = []
Func(for_five)
Func(for_four)
Func(for_three)
Func(for_two)
Func(for_one)
Func(for_null)

print(res_list)

done = [f'{res_list[i]} * x^{y-i}' if y-i != 0 else f'{res_list[i]}' for i in range(len(res_list)) if res_list[i] !=0]
# print(' + '.join(done) + ' = 0')

file = open('task03_result.txt', 'w')
file.write(' + '.join(done) + ' = 0')
file.close()


# 4. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

data = open('task04.txt', 'r')
list = []

for i in data:
    list.append(i)
data.close()

str_list = ' '.join(list).split(' ')

count = 0
for i in range(len(str_list)):
    if int(str_list[i]) - 1 != int(str_list[i-1]):
        count += 1
        if count == 2:
            str_list.insert(i, (int(str_list[i]) - 1))

# print(' '.join(map(str, str_list)))

data = open('task04.txt', 'a')
data.write('\n' + ' '.join(map(str, str_list)))
data.close()

# 5. Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#    [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

list = [5, 2, 3, 4, 6, 1, 7]
new_list = []

for j in range(len(list) - 1):
    index = j
    temp_list = [list[j]]
    while index < len(list) - 1:
        rem_list = [i for i in list[index:] if i > temp_list[-1]]
        if len(rem_list) != 0:
            current_min = min(rem_list)
        else:
            break
    
        temp_list.append(current_min)
        index += list[index:].index(current_min)

    print(temp_list)

    if len(temp_list) > len(new_list):
        new_list = temp_list.copy()

print(new_list)

print(f'Исходный список - {list}')
print(f'Возрастаяющая последовательность - {new_list}')
