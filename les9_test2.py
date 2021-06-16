
#Закодируйте любую строку по алгоритму Хаффмана.

import collections


c = collections.Counter()
#str = "beep boop beer!"
str = input("Введите строку для кодирования: ")
lst = list(str)
for word in lst:
    c[word] += 1

while len(c) != 1: # цикл работает пока все буквы не придут в одну строку
    c = collections.OrderedDict(sorted(c.items(), key=lambda t: t[1]))
    first = c.popitem(last = False) # извлекаю из коллекции первый отсортированный элемент
    second = c.popitem(last = False) # извлекаю из коллекции второй отсортированный элемент

    first = list(first) # преобразую буквы первого элемента, добавояя перед ними требуемый шифр
    first[0] = first[0].split(',')
    e = ['0' + i for i in first[0]]
    str_first = e[0]
    for j in range(1, len(e)):
        str_first += ',' + e[j]

    second = list(second) # преобразую буквы второго элемента, добавояя перед ними требуемый шифр
    second[0] = second[0].split(',')
    d = ['1' + i for i in second[0]]
    str_second = d[0]
    for j in range(1, len(d)):
        str_second += ',' + d[j]

    c[str_first + ',' + str_second] = first[1] + second[1] # добавил собранный элемент в конец коллекции
    c.move_to_end(str_first + ',' + str_second, last=False) # перенес собранный элемент в начало коллекции, чтобы он
    # отсортировался перед другими элементами с таким же весом

c = list(c) # извелаю из коллекции списоксимволов с кодом
my_list = c[0].split(',')

my_dict = dict() # создаю словарь для кодировки
for value in my_list:
    my_dict[value[-1]] = value[: -1]

res = '' # получаю закодированную строку
for i in lst:
    res += my_dict[i] + ' '
print(res)


