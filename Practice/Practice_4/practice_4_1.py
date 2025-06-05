text = "hello world"
found = False
for char in text:
    if char.isupper():
        print(f'Первая заглавная буква {char}')
        found = True
        break
if not found:  # = found = False
    print("Нет заглавных букв")