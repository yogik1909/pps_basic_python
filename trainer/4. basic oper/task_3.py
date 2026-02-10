# **Описание**: Создайте программу для работы с логическими операторами и проверки различных условий
#
# **Входные данные**: Используйте встроенные переменные в коде:
# - Первое булево значение (True или False)
# - Второе булево значение (True или False)
# - Третье булево значение (True или False)
#
# **Выходные данные**: Выведите на экран результаты всех логических операций:
# - Результат первого AND второго
# - Результат первого OR второго
# - Результат NOT первого
# - Результат NOT второго
# - Результат (первое AND второе) OR третье
# - Результат первое AND (второе OR третье)
# - Результат NOT (первое OR второе)
#
# **Ограничения**:
# - Используйте только логические операторы and, or, not
# - Результат каждой операции сохраните в отдельную булеву переменную
# - Все переменные должны иметь понятные имена
#
# **Примеры**:
# Входные данные: a = True, b = False, c = True
# Выходные данные:
# a and b: False
# a or b: True
# not a: False
# not b: True
# (a and b) or c: True
# a and (b or c): True
# not (a or b): False
#
# Входные данные: a = False, b = False, c = False
# Выходные данные:
# a and b: False
# a or b: False
# not a: True
# not b: True
# (a and b) or c: False
# a and (b or c): False
# not (a or b): True

a, b, c = True, False, True

is_a_and_b = a and b
is_a_or_b = a or b
is_not_a = not a
is_not_b = not b
is_a_and_b_or_c = (a and b) or c
is_a_and_b_or_c_2 = a and (b or c)
is_not_a_or_b = not (a or b)
print(f"a and b: {is_a_and_b}")
print(f"a or b: {is_a_or_b}")
print(f"not a: {is_not_a}")
print(f"not b: {is_not_b}")
print(f"(a and b) or c: {is_a_and_b_or_c}")
print(f"a and (b or c): {is_a_and_b_or_c_2}")
print(f"not (a or b): {is_not_a_or_b}")
