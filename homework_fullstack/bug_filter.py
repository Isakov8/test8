bugs = [
    "Ошибка 1 — High",
    "Ошибка 2 — Medium",
    "Ошибка 3 — Low",
    "Ошибка 4 — High",
    "Ошибка 5 — Medium",
    "Ошибка 6 — Low",
    "Ошибка 7 — High"
]
a= input("Введите приоритет для поиска (High, Medium, Low): ")
b=[]
for bug in bugs:
    if a in bug:
        b.append(bug)
print('Найденные баги:',b)
if not b:
    print('Таких багов нет')