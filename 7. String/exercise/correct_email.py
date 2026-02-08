# Цель: Проверить корректность e-mail путем проверки структуры. 
# Необходимо наличие локальной части, домена второго уровня, символа '@', 
#   точки и домена первого уровня (две буквы).

email = input("Введите e-mail: ")
# is_correct = True

# is_correct = is_correct and email.find("@") != -1
# is_correct = is_correct and email.count("@") == 1
# username, domain_name = email.split("@", 1)

# is_correct = is_correct and len(username) > 0
# is_correct = is_correct and domain_name.find(".") != -1
# is_correct = is_correct and len(domain_name.split(".")[-1]) < 2

if email.count("@") != 1:
    print("Некорректный e-mail")
    exit()

username, domain_name = email.split("@", 1)

if not username:
    print("Некорректный e-mail")
    exit()

if "." not in domain_name:
    print("Некорректный e-mail")
    exit()

if len(domain_name.split(".")[-1]) < 2:
    print("Некорректный e-mail")
    exit()

if len(domain_name.split(".")[0]) == 0:
    print("Некорректный e-mail")
    exit()

print("Корректный e-mail")