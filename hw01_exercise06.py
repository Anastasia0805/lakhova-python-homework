a = int(input('Введите результат пробежки в первый день в км'))
b = int(input('Введите количество км, которое вы хотите всего пробежать'))

day = 1
result = a

while result < b:
    a = a + 0.1 * a
    day += 1
    result = a

print("на {} й день спортсмен достиг результата — не менее {} км".format(day, b))
