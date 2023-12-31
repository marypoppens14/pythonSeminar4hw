#В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
#Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. 
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод. 
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
#Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
#Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. 
#Напишите программу для нахождения максимального числа ягод, 
#которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input("введите количество кустов: "))
list_1 = list()
for i in range(n):
    a =int(input('введите количество ягод: '))
    list_1.append(a)

amount_list = list()
for i in range(len(list_1)):
       amount_list.append(list_1[i-2] + list_1[i-1] + list_1[i])
print(max(amount_list))