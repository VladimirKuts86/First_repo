inventory = {'ручка': 20, 'книга': 800, 'рюкзак': 1500}
filtered_inventory = {}
for key, value in inventory.items():
    if value >= 800:
        filtered_inventory[key] = value
print(filtered_inventory)