revenue = int(input ('Введите значение выручки в рублях'))
costs = int (input('Введите значение издержек в рублях'))

if revenue > costs:
    print ("Ваша компания работает с прибылью")
else:
    print("Ваша компания работает в убыток")

work_force = int(input('Введите численность сотрудников'))
profit = revenue - costs
profit_for_person = profit/work_force
if profit > 0:
    print ("Прибыль в расчете на одного сотрудника составляет", profit_for_person, "рублей")
else:
    print ("У вас нет прибыли в расчете на одного сотрудника")