def okr(a,b,r,d):
    return len(list(filter(lambda z: (z[0]-a)**2+(z[1]-b)**2 < r**2,d)))
print(okr(int(input('Точка а: ')),int(input('Точка b: ')),int(input('Радиус: ')),
          [[int(i) for i in input('Координаты P: ').split()],
           [int(i) for i in input('Координаты F: ').split()],
           [int(i) for i in input('Координаты L: ').split()]]))
