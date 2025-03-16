bugs = [
    "Ошибка 1 — High",
    "Ошибка 2 — Low",
    "Ошибка 3 — Medium",
    "Ошибка 4 — High",
    "Ошибка 5 — Low"
]

new_bug = input("Введите новый баг в формате 'Ошибка X — Приоритет': ")
bugs.append(new_bug)
print("Список после добавления нового бага:")
print(bugs)
for bug in bugs.copy():
    if "Low" in bug:
        bugs.remove(bug)
print("Список после удаления багов с низким приоритетом:")
print(bugs)

priority_order = {"High": 1, "Medium": 2, "Low": 3}
sorted_bugs = sorted(bugs, key=lambda bug: priority_order[bug.split(' — ')[1].strip()])
print("Отсортированный список багов:")
print(sorted_bugs)