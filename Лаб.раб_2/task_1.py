money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0    # count of months without debts
balance = money_capital + salary - spend    # current (at 1st month) capital
while balance >= 0:    # as soon as balance is positive
    spend *= 1 + increase    # firstly, spend should increase every month by increase value
    balance += salary - spend    # bal. is changing towards negative thr. diff. btw const. salary and increasing spend
    months += 1    # after each repeat count of numbers increases by one
print("Количество месяцев, которое можно протянуть без долгов:", months)
