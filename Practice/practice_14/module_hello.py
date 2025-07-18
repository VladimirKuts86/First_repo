def hello(name):
    return f"Привет, {name}"

def main():
    print(hello(input('Введите своё имя: ')))

if __name__ == "__main__":
    main()