salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

neg_balance = salary - spend    # negative balance now (necessary capital later)
for _ in range(2, months + 1):
    spend *= 1 + increase
    neg_balance += salary - spend
money_capital = round(- neg_balance, 2)    # negative balance after cycle = necessary money capital now
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
