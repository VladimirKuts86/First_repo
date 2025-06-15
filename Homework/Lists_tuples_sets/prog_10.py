students = [('Анна', [5, 5, 4]), ('Борис', [4, 3, 5]), ('Виктор', [5, 5, 5])]
best_student = ""
best = 0
for student in students:
    student_name = student[0]
    grade = student[1]
    current = sum(grade)
    if current > best:
        best = current
        best_student = student_name
print(best_student)