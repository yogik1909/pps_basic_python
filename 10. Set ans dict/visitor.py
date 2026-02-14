# Посчитать для каждого дня - всего визитов, уникальных  визитов
# Найти йд≤ кто посетили оба дня
# Найти тех, кто посетил только первый день
# Найти тех, кто посетил только второй день
# Найти тех, кто были только 1 раз

visitors_day1 = [101, 102, 103, 101, 104, 102, 105, 101]
visitors_day2 = [101, 108, 100, 101, 105, 107]

print(f"Всего визитов в первый день: {len(visitors_day1)}")
print(f"Всего вижитов во второй день: {len(visitors_day2)}")

print(f"Уникальных визитов в первый день: {len(set(visitors_day1))}")
print(f"Уникальных визитов во второй день: {len(set(visitors_day2))}")

print(
    f"Кто посетил оба дня: {sorted(set(visitors_day1) & set(visitors_day2))}")
print(
    f"Кто посетил только первый день: {sorted(set(visitors_day1) - set(visitors_day2))}")
print(
    f"Кто посетил только второй день: {sorted(set(visitors_day2) - set(visitors_day1))}")
print(
    f"Кто были только 1 раз: {sorted(set(visitors_day1) ^ set(visitors_day2))}")
