salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for _ in range(months):
    money_capital += spend - salary # записываем разницу в подушку безопасноости
    spend *= 1 + increase # увеличиваем траты на рост цен

print(round(money_capital))

