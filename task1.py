#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.

n = int(input("введите первое число: "))
list_n = []
for i in range(n):
    amount1 = int(input("введите элементы: "))
    list_n.append(amount1)
print(list_n)

m = int(input("введите второе число: "))
list_m = []
for i in range(m):
    amount2 = int(input("введите элементы: "))
    list_m.append(amount2)
print(list_m)

list_fin = list_n + list_m
print(list_fin)
for i in set(list_fin):
    if list_fin.count(i) > 1:
        print(i)