sta1 = int(input("Введите первое число: "))
sta2 = int(input("Введите второе число: "))
sta3 = int(input("Введите третье число: "))

max_stat = sta1 if sta1 >= sta2 else sta2
max_stat = max_stat if max_stat >= sta3 else sta3

print(f"Максимальное число: {max_stat}")
