users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
unique_guests = set(users)    # уникальные посетители

guests_list = {"Общее количество": len(users), "Уникальные посещения": len(unique_guests)}

print(guests_list)
