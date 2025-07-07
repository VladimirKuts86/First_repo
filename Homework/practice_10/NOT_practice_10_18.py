# Напишите функцию build_where_clause(**conditions) для генерации части WHERE SQL-запроса.
#  Функция должна принимать условия в виде ключ=значение и объединять их через AND.
#  Значения-строки должны быть в одинарных кавычках.

# # Пример использования:
# query_part = build_where_clause(user_id=101, status="active", is_verified=True)
# print(query_part)
# Вывод: WHERE user_id = 101 AND status = 'active' AND is_verified = True
