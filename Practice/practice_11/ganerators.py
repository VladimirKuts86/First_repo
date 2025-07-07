def fib(n):
    n_1, n_2 = 1, 1
    for i in range(n):
        yield n_1
        n_1, n_2 = n_2, n_1 + n_2

# print(next(fib(10)))
# print(next(fib(10)))
# print(", ".join(str(x) for x in fib(10)))


# def fruit_generator():
#     for item in ["apple", "banana", "cherry"]:
#         yield item
# fruit = fruit_generator()
# print(next(fruit))
# print(next(fruit))
# print(next(fruit))

f = fib(30)
for i in range(22):
    print(next(f))