file = open('Жуков_Владислав_Ум232_8_1_vvod.txt','r')
s = []
A = []
for row in file:
    A.append([int(x) for x in row.split(' ')])
print(A)
file.close()
s = []
for i in range(len(A)):
    s.append(sum(A[i]))
print('Строка с наибольшей суммой элементов: ',A[s.index(max(s))],'=' ,max(s),'\nСтрока с наименьшей суммой элементов: ',A[s.index(min(s))],'=',min(s))

file = open('C:\\tee\Жуков_Владислав_Ум232_8_1_vivod.txt','w')
file.write('Строка с наибольшей суммой элементов: ' + str(A[s.index(max(s))]) + '=' + str(max(s)) + '\nСтрока с наименьшей суммой элементов: ' + str(A[s.index(min(s))]) + '=' + str(min(s)))
file.close()


