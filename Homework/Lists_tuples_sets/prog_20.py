data = {'user': {'name': 'Alice', 'profile': {'theme': 'dark'}}}
for key, value in data.items():
    for key1, value1 in value.items():
        if key1 == 'profile':
            for key2, value2 in value1.items():
                print(value2)


 

