text = "Hello World 23232 1321 brother"
vowels = 'aeiouy'
count_vowels = 0
count_consonants = 0
for char in text:
    if char.isalpha():
        if char.lower() in vowels:
            count_vowels += 1
        else:
            count_consonants += 1
print(f"Гласных: {count_vowels}, согласных: {count_consonants}")
