string = "This is a demonstration of how generator expressions work in Python"
words = (word for word in string.split() if len(word) > 4)
while True:
    try:
        print(next(words))
    except StopIteration:
        break