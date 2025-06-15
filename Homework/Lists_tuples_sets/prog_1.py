Ages = [25, 17, 18, 31, 16, 22]
Adults = []
for i in Ages:
    if i >= 18:
        Adults.append(i)
    else:
        continue
print(Adults) 