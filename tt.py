n = int(input('Введите количество чисел: '))

a1 = 1
a2 = 1
for i in range(2,n):
    a1, a2 = a2, a1+a2
    print(a2)
print('Сумма: ',a2) 
