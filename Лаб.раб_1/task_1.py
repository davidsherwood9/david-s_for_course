numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missed_number = numbers[4]    # Пропущенное число

sum_without_none = sum(numbers[:4]) + sum(numbers[5:])    # Сумма всех чисел без None

quantity_of_numbers = len(numbers[:4]) + len(numbers[4:])    # Количество значений в списке без None

average_number = sum_without_none / quantity_of_numbers

numbers[4] = average_number

print("Измененный список:", numbers)
