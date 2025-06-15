grades = {'Иванов': 55, 'Петров': 72, 'Сидоров': 48}
for key, value in grades.items():
    if value < 60:
        grades[key] += 5
print(grades)
