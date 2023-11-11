lst = [10, 34, 23, 4, 12, 9]
print(lst)
save = lst[0]
save_pos = 0
for i in range(len(lst)):
    if save < lst[i]:
        save = lst[i]
        save_pos = i+1
print('Max elem = ', save)
print('Her position = ', save_pos)
