# Напишиите программу, которая вычисляет сумму скидки в зависимости от суммы продажи. Пусть скидки установлены следующим образом:
#
# Сумма продажи	Скидка
# 0-5000	5%
# 5000-15000	12%
# 15000-25000	20%
# свыше 25000	30%
# После вычисления скидки программа должна вывести саму скидку и сумму с вчетом скидки. Например:


sales_amount = int(input("Введите сумму продажи: "))
discount_amount = 0
if sales_amount > 25000:
    discount_amount = float((sales_amount / 100) * 30)
    print("Скидка:", discount_amount, "\nСумма с учётом скидки:", float(sales_amount - discount_amount))
elif 15000 < sales_amount <= 25000:
    discount_amount = float((sales_amount / 100) * 20)
    print("Скидка:", discount_amount, "\nСумма с учётом скидки:", float(sales_amount - discount_amount))
elif 5000 < sales_amount <= 15000:
    discount_amount = float((sales_amount / 100) * 12)
    print("Скидка:", discount_amount, "\nСумма с учётом скидки:", float(sales_amount - discount_amount))
elif 0 < sales_amount <= 5000:
    discount_amount = float((sales_amount / 100) * 5)
    print("Скидка:", discount_amount, "\nСумма с учётом скидки:", float(sales_amount - discount_amount))
else:
    print("Некорректная сумма")