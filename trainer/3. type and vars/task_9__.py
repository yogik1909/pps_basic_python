# **Описание**: Создайте переменные для хранения данных о спортивном событии и выполните проверку их идентичности
#
# **Входные данные**: Нет (используйте встроенные значения в коде)
#
# **Выходные данные**: Результаты сравнения переменных, выведенные с помощью функции print()
#
# **Ограничения**: Используйте только базовые типы данных Python: int, float, str, bool. Создайте несколько переменных и сравните их на идентичность с помощью оператора is
#
# **Примеры**:
# Вывод должен содержать результаты сравнения в формате:
# True
# False
# True
# False

FOOTBALL_MATCH = "Football Match"
STADIUM = "Stadium"
CORT = "Cort"

match_id_1 = 12321321
match_name_1 = FOOTBALL_MATCH
match_date_1 = "2024-01-01"
match_time_1 = "18:00"
match_location_1 = STADIUM

match_id_2 = 123213353324
match_name_2 = FOOTBALL_MATCH
match_date_2 = "2024-01-01"
match_time_2 = "18:00"
match_location_2 = CORT

print(match_id_1 is match_id_2)
print(match_name_1 is match_name_2)
print(match_date_1 is match_date_2)
print(match_time_1 is match_time_2)
print(match_location_1 is match_location_2)
