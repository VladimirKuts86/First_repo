# 11. Построчная фильтрация логов через генератор. Фильтр на ERROR
logs = [
    "INFO: Start",
    "ERROR: Disk not found",
    "WARNING: Low memory",
    "ERROR: Timeout",
    "INFO: End"
]
errors = (word for word in logs if word.startswith("ERROR:"))
while True:
    try:
        print(next(errors))
    except StopIteration:
        break



