pnd=int(input('Количество тк в понедельник:'))
vt=int(input('Количество тк в вторник:'))
sr=int(input('Количество тк в среду:'))
cht=int(input('Количество тк в четверг:'))
pyat=int(input('Количество тк в пятницу:'))
c=pnd+vt+sr+cht+pyat
b=c//5
if c>= 10:
    print("Отличная работа")
else:
    print("Попробуй улучшить результат")
