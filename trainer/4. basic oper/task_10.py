# **Описание**: Создайте программу для работы с операторами тождественности и проверки идентичности объектов
#
# **Входные данные**: Используйте встроенные переменные в коде:
# - Первое число (целое)
# - Второе число (целое)
# - Третье число, равное первому (целое)
# - Первая строка (строка)
# - Вторая строка, идентичная первой (строка)
#
# **Выходные данные**: Выведите на экран результаты всех проверок:
# - Результат первое is второе
# - Результат первое is третье
# - Результат первое is not второе
# - Результат первая_строка is вторая_строка
# - Результат первая_строка is not вторая_строка
# - Сравнение id() первого и второго числа
# - Сравнение id() первого и третьего числа
#
# **Ограничения**: 
# - Используйте только операторы is и is not
# - Результат каждой проверки сохраните в отдельную булеву переменную
# - Числа от 1 до 10
# - Строки должны быть короткими (до 5 символов)

# Входные данные
dig_first = 1
dig_second = 2
dig_third = 1
str_first = "hello"
str_second = "hello"

# Проверки тождественности
# - Результат первое is второе
is_first_is_second = dig_first is dig_second

# - Результат первое is третье
is_first_is_third = dig_first is dig_third

# - Результат первое is not второе
is_first_is_not_second = dig_first is not dig_second

# - Результат первая_строка is вторая_строка
is_str_first_is_str_second = str_first is str_second

# - Результат первая_строка is not вторая_строка
is_str_first_is_not_str_second = str_first is not str_second

# - Сравнение id() первого и второго числа
is_dig_first_is_dig_second = id(dig_first) == id(dig_second)

# - Сравнение id() первого и третьего числа
is_dig_first_is_dig_third = id(dig_first) is id(dig_third)


# Вывод результатов
print(f"Первое число: {dig_first}")
print(f"Второе число: {dig_second}")
print(f"Третье число: {dig_third}")
print(f"Первая строка: {str_first}")
print(f"Вторая строка: {str_second}")
print()
print(f"Результат первое is второе: {is_first_is_second}")
print(f"Результат первое is третье: {is_first_is_third}")
print(f"Результат первое is not второе: {is_first_is_not_second}")

print(f"Результат первая_строка is вторая_строка: {is_str_first_is_str_second}")
print(f"Результат первая_строка is not вторая_строка: {is_str_first_is_not_str_second}")
print(f"Сравнение id() первого и второго числа: {is_dig_first_is_dig_second}")
print(f"Сравнение id() первого и третьего числа: {is_dig_first_is_dig_third}")