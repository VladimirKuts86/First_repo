# Напишите функцию format_header(text, level=1, char="=") 
# которая создает заголовок. level — количество строк из символов char до и после текста.
# Длина строки из символов = длине текста

def format_header(text, level=1, char="="):
    line = char * len(text) #'========='
    header_lines = [line] * level #['=========', '=========']
    final_line = '\n'.join(header_lines) #"=========\n========="
    return final_line + f"\n{text}\n" + final_line

print(format_header("Заголовок", 3, "_"))