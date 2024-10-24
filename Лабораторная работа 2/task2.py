salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = 0 # минимальная подушка безопасности
for cur_month in range(1, months+1):
    money_capital -= salary - spend # в данных условиях будет увеличиваться
    spend *= 1 + increase

# result = int(money_capital) + 1 * (int(money_capital) != money_capital)
result = int(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", result)
