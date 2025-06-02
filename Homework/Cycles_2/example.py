for i in range(26):
    print(f"{chr(ord('a')+i)}")



for i in range(26):
    for j in range(26):
        print(f"{chr(ord('a')+i)}{chr(ord('a')+j)}")

flag = False
for i in range(26):
    for j in range(26):
        text = f"{chr(ord('a')+i)}{chr(ord('a')+j)}"
        if text == "ya":
            print(text)
            flag = True
            break
        print(text)
    if flag == True:  # if flag:
        break

