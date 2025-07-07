# Список уникальных слов в нижнем регистре ["Hello", "world", "HELLO", "World", "python"]
words = ["Hello", "world", "HELLO", "World", "python"]
unique_words = [word for word in words if word.islower()]
print(unique_words)