bugs = [
    "Ошибка 1 — High",
    "Ошибка 2 — Low",
    "Ошибка 3 — Medium",
    "Ошибка 4 — High",
    "Ошибка 5 — Low"
]
bugs.append(input("Введите новый баг:"))
print(bugs)
for bug in bugs:
    if "Low" in bug:
     bugs.remove(bug)
print(bugs)

