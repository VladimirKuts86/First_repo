# Задача с пометкой для самостоятельного изучения
# Напишите функцию create_html_tag(tag, content, style=None, id_name=None), 
# которая создает строку с HTML-тегом. Атрибуты style и id_name необязательны.
# <p> Простой параграф </p>
# <div id="main-block">Блок с ID</div>
# <span style="color: red;">Цветной текст</span>

def create_html_tag(tag, content, style=None, id_name=None):
    if tag == "p":
        return f"<{tag}> {content} </{tag}>"
    elif tag == 'div':
        return f'<{tag} id="{id_name}">{content}</{tag}>'
    elif tag == 'span':
        return f'<{tag} style="{style}">{content}</{tag}>'


print(create_html_tag(tag="p", content="Простой параграф", style=None, id_name=None))
print(create_html_tag(tag="div", content="Блок с ID", style=None, id_name="main-block"))
print(create_html_tag(tag="span", content="Цветной текст", style="color: red;"))


def create_html_tag(tag, content, style=None, id_name=None):
    opening_tag = f'<{tag}'
    if id_name is not None:
        opening_tag += f' id="{id_name}"'
    if style is not None:
        opening_tag += f' style="{style}"'
    closing_tag = f'>{content}</{tag}'
    return f'{opening_tag}{closing_tag}'

print(create_html_tag(tag="p", content="Простой параграф", style=None, id_name=None))
print(create_html_tag(tag="div", content="Блок с ID", style=None, id_name="main-block"))
print(create_html_tag(tag="span", content="Цветной текст", style="color: red;"))