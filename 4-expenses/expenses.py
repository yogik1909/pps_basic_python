# Создать список из трат за неделю(7 чисел)
# Посчитать сумму, среднее, минимум и максимум.
# Сохранить в кортеже(минимум, максимум, сумма) и вывести его.
list_of_expenses = [100, 200, 300, 400, 500, 600, 700]
min_expense = min(list_of_expenses)
max_expense = max(list_of_expenses)
sum_of_expenses = sum(list_of_expenses)
average_expense = sum_of_expenses / len(list_of_expenses)
result = (min_expense, max_expense, sum_of_expenses)
print(result)
