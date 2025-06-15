employees = [('Иван', 'IT'), ('Мария', 'HR'), ('Петр', 'IT')]
it_team = []
hr_team = []
for i in employees:
    if i[1] == 'IT':
        it_team.append(i[0])
    else:
        hr_team.append(i[0])
print(f"Команда IT: {it_team}, команда HR: {hr_team}")