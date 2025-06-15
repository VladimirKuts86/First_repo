languages = [ {'английский', 'испанский'}, {'английский', 'французский'}, {'английский', 'немецкий'} ]
best_language = set()
current = set()
for i in languages:
    if current == set():
        current = i
        continue
    else:
        best_language = current.intersection(i)
print(best_language)


languages = [ {'английский', 'испанский'}, {'английский', 'французский'}, {'английский', 'немецкий'} ]
best_language = set()
for i in languages:
    if best_language == set():
        best_language = i
        continue
    else:
        best_language = best_language.intersection(i)
print(best_language)
