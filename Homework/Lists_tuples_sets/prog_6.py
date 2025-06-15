list_of_goods = [('книга', 800), ('ручка', 50), ('рюкзак', 1500)]
budget_goods = []
for i in list_of_goods:
    if i[1] <= 800:
        budget_goods.append(i[0])
print(budget_goods)
