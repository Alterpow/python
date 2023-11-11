stroka = 'Анатолий Вассерман знает все'
print('Исходная строка:',stroka)
count_a=0
count_A=0
count_a = stroka.count('а')
count_A = stroka.count('А')
stroka = stroka.replace('А', 'О')
stroka = stroka.replace('а', 'о')
print('Количество заменяемых букв "а":',count_a, '\nКоличество заменяемых букв "A":', count_A)
print('Полученная строка:',stroka)
