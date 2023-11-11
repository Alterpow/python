file = open('Жуков_Владислав_Ум232_8_2_vvod.txt','r')
s = []
a = []
for row in file:
    a.append([int(x) for x in row.split(' ')])
print(a)
file.close()
a = [[1 if x>0 else 0 for x in i] for i in a]
file = open('C:\\tee\Жуков_Владислав_Ум232_8_2_vivod.txt','w')
for i in range(len(a)):
    b = []
    b = *[a[i][x] if x<=i else '' for x in range(len(a[i]))],''
    print(*[a[i][x] if x<=i else '' for x in range(len(a[i]))],'')
    file.writelines(str(b) + '\n')
file.close()
