# Напишите функцию create_filtered_dict(allowed_keys, **kwargs), которая создает словарь 
# только из тех kwargs, чьи ключи есть в списке allowed_keys.

def create_filtered_dict(allowed_keys, **kwargs):
    filtered_dictionary = {}
    for key, value in kwargs.items():
        if str(key) in allowed_keys:
            filtered_dictionary.update({key: value})
        else:
            continue
    print(filtered_dictionary)
create_filtered_dict(fruit="orange", vegetables="cucumber", snake="mamba", allowed_keys = ["fruit", "vegetables", "berry"])
