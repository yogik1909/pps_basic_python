import random
import string

passwords = {}


def show_pass():
    print(passwords)


def generate_password(length: int, use_symbol: bool = False) -> str:
    if length < 3:
        return ""

    # Собираем все символы в одну строку
    characters = string.ascii_letters + string.digits

    if use_symbol:
        # Добавляем специальные символы
        characters += string.punctuation + "!@#$%&*^_=+"

    password = []
    while len(password) < length:
        char = random.choice(characters)
        if len(password) < len(characters) \
                and char in password:
            continue
        password.append(char)

    return "".join(password)


def add_pass() -> None:
    domain = input("Введите домен: ")
    password = input("Введите пароль: ")
    password = generate_password(password) if password == "" else password
    passwords[domain] = password


def delete_pass(domain: str) -> None:
    del passwords[domain]


def update_pass(domain: str) -> None:
    password = input("Введите новый пароль: ")
    password = generate_password(password) if password == "" else password
    passwords[domain] = password


def show_menu():
    print("1. Показать пароли")
    print("2. Добавить пароль")
    print("3. Удалить пароль")
    print("4. Обновить пароль")
    print("5. Выход")
    user_choice = int(input("Выберите опцию: "))
    match user_choice:
        case 1:
            show_pass()
        case 2:
            add_pass()
        case 3:
            domain = input("Введите домен: ")
            delete_pass(domain)
        case 4:
            domain = input("Введите домен: ")
            update_pass(domain)
        case 5:
            exit()


while True:
    show_menu()
