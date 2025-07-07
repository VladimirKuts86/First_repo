# Напишите функцию для расчета ежемесячного платежа по кредиту. 
# Формула аннуитетного платежа: 
# Платеж = Сумма * (Ставка * (1 + Ставка)^Срок) / ((1 + Ставка)^Срок - 1).
# Установите годовую ставку по умолчанию 10% (0.1) и срок в годах 5 лет.

def payment(summa, rate=0.1, period=5):
    month_rate = rate / 12
    period_in_months = period * 12
    return summa * (month_rate * (1 + month_rate)**period_in_months) / ((1 + month_rate)**period_in_months - 1)
print(payment(int(input())))