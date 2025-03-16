a={'Анна': 3, 'Иван': 5, 'Дмитрий': 7}
name= input()
if name in a:
    a[name] = a[name] + 1
else :
    a[name] = 1
print(a)