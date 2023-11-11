lst = [10, 15, 8, 3, 29, 41, 62]
lst2 = [10, 8, 6, 4, 2, 20, 14]
lst3 = []
for i in lst:
    if i % 2 != 0:
        lst3.append(i)
lst3.sort(reverse=True)
for j in range(len(lst3)):
    if lst3[j] % 2 != 0:
        print(lst3[j], end=" ")
    else:
        print('Нечетных чисел нет')


